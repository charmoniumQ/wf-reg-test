from __future__ import annotations

import collections
import contextlib
import dataclasses
import datetime
import functools
import logging
import pathlib
import random
import re
import shlex
import shutil
import subprocess
import sys
import urllib
import warnings
from typing_extensions import Protocol
from typing import Any, Callable, ClassVar, Mapping, Optional, TypeVar, cast, ContextManager, Iterator, Union

import charmonium.time_block as ch_time_block
import yaml
import upath

from .util import create_temp_dir, expect_type, walk_files, random_str, fs_escape
from .workflows import Execution, Revision, Condition, WorkflowError, FileBundle
from .executable import Machine, Executable, ComputeResources, time, timeout, taskset, parse_time_file
from .repos import get_repo


logger = logging.getLogger("wf_reg_test")


class Engine:
    def get_executable(
            self,
            workflow: pathlib.Path,
            log_dir: pathlib.Path,
            out_dir: pathlib.Path,
            n_cores: int,
    ) -> ContextManager[Executable]:
        raise NotImplementedError

    def parse_error(
            self,
            log_dir: pathlib.Path,
            code_dir: pathlib.Path,
            resources: ComputeResources,
            status_code: int,
    ) -> Optional[WorkflowError]:
        raise NotImplementedError


    def run(
            self,
            revision: Revision,
            condition: Condition,
            which_cores: list[int],
            wall_time_limit: datetime.timedelta,
            storage: upath.UPath,
    ) -> Execution:
        if revision.workflow is None:
            raise ValueError(f"Can't run a revision that doesn't have workflow. {revision}")
        if condition.single_core != (len(which_cores) == 1):
            raise ValueError(f"Requested single-core={condition.single_core}, but assigned {len(which_cores)} cores")
        if condition.aslr or condition.faketime or condition.dev_random is not None or condition.rr_record or condition.rr_replay is not None:
            raise NotImplementedError()
        repo = get_repo(revision.workflow.repo_url)
        with create_temp_dir() as path:
            code_dir = path / "code"
            log_dir = path / "log"
            out_dir = path / "out"
            for dir in [code_dir, log_dir, out_dir]:
                dir.mkdir()
            repo.checkout(revision, code_dir)
            with self.get_executable(code_dir, log_dir, out_dir, len(which_cores)) as executable:
                # It takes a lot of effort in logic and coordination to get which_cores to work correctly.
                # I think the Linux scheduler should be good enough
                #executable = taskset(executable, which_cores)
                executable = timeout(executable, wall_time_limit)
                with time(executable) as (executable, time_file):
                    with ch_time_block.ctx(f"execute {revision.workflow}"):
                        now = datetime.datetime.now()
                        proc = executable.local_execute(check=False, capture_output=True)
                        resources = parse_time_file(time_file)
                (log_dir / "stdout.txt").write_bytes(proc.stdout)
                (log_dir / "stderr.txt").write_bytes(proc.stderr)
                (log_dir / "command.sh").write_text("\n".join([
                    *map(shlex.join, repo.get_checkout_cmd(revision, code_dir)),
                    shlex.join(executable.to_env_command())
                ]))
                (log_dir / "status.yaml").write_text(yaml.dump({
                    "status": proc.returncode,
                    "resources": resources,
                }))
            run_path = storage / fs_escape(revision.workflow.display_name) / random_str(8)
            workflow_error = self.parse_error(log_dir, code_dir, resources, proc.returncode)
            outputs = FileBundle.from_path(out_dir, run_path / "output.tar.xz")
            logs = FileBundle.from_path(log_dir, run_path / "logs.tar.xz")
        return Execution(
            machine=None,
            datetime=now,
            outputs=outputs,
            logs=logs,
            condition=condition,
            resources=resources,
            status_code=proc.returncode,
            workflow_error=workflow_error,
            revision=None,
        )


def yaml_load_or(yaml_src: str, default: Any) -> Any:
    try:
        return yaml.safe_load(yaml_src)
    except yaml.YAMLError:
        return default


class SnakemakeEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            code_dir: pathlib.Path,
            log_dir: pathlib.Path,
            out_dir: pathlib.Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        start_time = datetime.datetime.now()
        github_ci_dir = pathlib.Path(code_dir / ".github/workflows")
        steps = []
        if github_ci_dir.exists():
            # Exclude --report and --lint runs, which may have different args than the main run
            # There still could be multiple arg sets, of which, we simply choose the first.
            steps = [
                step
                for path in [*github_ci_dir.glob("*.yaml"), *github_ci_dir.glob("*.yml")]
                for job in yaml_load_or(path.read_text(), {}).get("jobs", {}).values()
                for step in job.get("steps", [])
                if step.get("uses", "").startswith("snakemake/snakemake-github-action")
                   and "--report" not in step.get("with", {}).get("args", {})
                   and "--lint" not in step.get("with", {}).get("args", {})
                   and "--conda-create-envs-only" not in step.get("with", {}).get("args", {})
            ]
        if steps:
            main_step = steps[0]
            directory = main_step.get("with", {}).get("directory", ".test")
            snakefile = main_step.get("with", {}).get("snakefile", "Snakefile")
            # This extra_args might have --conda-frontend=mamba and is generally too unpredictable to include
            #extra_args = shlex.split(main_step.get("with", {}).get("args", ""))
            extra_args = []
        else:
            directory = code_dir
            # See for typical snakefile locations:
            # https://github.com/friendsofstrandseq/mosaicatcher-pipeline/tree/1.4.1/ -> ./Snakefile
            # https://github.com/friendsofstrandseq/mosaicatcher-pipeline/tree/1.8.4/ -> ./workflow/Snakefile
            possible_snakefiles = ["snakefile", "Snakefile", "workflow/snakefile", "workflow/Snakefile"]
            # This suppresses the "UnboundLocalError: local variable 'snakefile' referenced before assignment"
            # even though Snakefile will certainly be overwritten before use
            snakefile = pathlib.Path(possible_snakefiles[0])
            try:
                snakefile = next(
                    pathlib.Path(path)
                    for path in possible_snakefiles
                    if (code_dir / path).exists()
                )
            except StopIteration as exc:
                yield Executable(
                    command=["/usr/bin/false", "Could not find [Ss]nakefile"],
                    cwd=code_dir,
                )
                return
            extra_args = []
        catalog_file = code_dir / ".snakemake-workflow-catalog.yml"
        # This extra args, however, is used more conservatively.
        # This are labelled "mandatory"
        extra_args += shlex.split((yaml_load_or(catalog_file.read_text(), {}) if catalog_file.exists() else {}).get("mandatory-flags", {}).get("flags", ""))
        conda_path = code_dir.resolve().parent / "conda"
        conda_path.mkdir()
        singularity_dir = code_dir.resolve().parent / "singularity"
        singularity_dir.mkdir()
        singularity_tmp_dir = code_dir.resolve().parent / "singularity-tmp"
        singularity_tmp_dir.mkdir()
        yield Executable(
            command=[
                # See https://github.com/snakemake/snakemake-github-action/blob/master/entrypoint.sh
                "snakemake",
                f"--cores={n_cores}",
                f"--directory={directory}",
                "--use-singularity",
                "--use-conda",
                "--conda-frontend=conda",
                "--forceall",
                f"--snakefile={snakefile!s}",
                *extra_args,
            ],
            cwd=code_dir,
            env_override={
                "CONDA_ENVS_PATH": str(conda_path),
                "SINGULARITY_CACHE": str(singularity_dir),
                "SINGULARITY_TMPDIR": str(singularity_tmp_dir),
                "SINGULARITY_LOCALCACHEDIR": str(singularity_tmp_dir),
                "TMPDIR": str(singularity_tmp_dir),
            },
            read_write_mounts={
                code_dir: code_dir,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )
        # See https://github.com/snakemake-workflows/dna-seq-benchmark
        # do `snakemake workflow/Snakefile --summary` for typical outputs
        # do `snakemake workflow/Snakefile` for typical logs
        for log_file in [".snakemake", "logs"]:
            if (code_dir / log_file).exists():
                shutil.move(code_dir / log_file, log_dir / log_file)
        for out_file in ["results", "resources"]:
            if (code_dir / out_file).exists():
                shutil.move(code_dir / out_file, out_dir / out_file)
        # Fallthrough, everything else goes to results.
        for fil in walk_files(code_dir):
            if fil.exists() and fil.is_file() and datetime.datetime.fromtimestamp(fil.stat().st_mtime) >= start_time:
                (out_dir / fil).parent.mkdir(exist_ok=True, parents=True)
                shutil.move(code_dir / fil, out_dir / fil)

    def parse_error(self, log_dir: pathlib.Path, code_dir: pathlib.Path, resources: ComputeResources, status_code: int) -> Optional[WorkflowError]:
        # TODO: don't hardcode the limit here
        if resources.wall_time > datetime.timedelta(seconds=3590) and status_code == 124:
            return WorkflowTimeoutError("timeout")
        log_files = list((log_dir / ".snakemake/log").glob("*.snakemake.log"))
        logs = max(log_files).read_text() if log_files else ""
        stderr = (log_dir / "stderr.txt").read_text()
        err: Optional[WorkflowError]
        if "Could not find [Ss]nakefile" in (log_dir / "command.sh").read_text():
            return NoSnakefileError(kind="NoSnakefileError")
        elif err := SnakemakePythonError._from_text(logs, stderr, code_dir):
            return err
        elif err := SnakemakeRuleError._from_text(logs, stderr, code_dir):
            return err
        elif err := SnakemakeCondaError._from_text(logs, stderr):
            return err
        elif err := SnakemakeWorkflowError._from_text(logs, stderr):
            return err
        elif err := SnakemakeInternalError._from_text(stderr):
            # TODO: some InternalErrors also cause PythonErrors
            # But they get parsed incorrectly as PythonErrors
            # But moving this block above that makes true PythonErrors get parsed incorrectly as InternalError.
            return err
        elif err := SnakemakeInternalError2._from_text(stderr):
            return err
        else:
            return None


@dataclasses.dataclass(frozen=True)
class WorkflowTimeoutError(WorkflowError):
    pass


@dataclasses.dataclass(frozen=True)
class NoSnakefileError(WorkflowError):
    pass

@dataclasses.dataclass(frozen=True)
class SnakemakeCondaError(WorkflowError):
    rest: str
    _pattern: ClassVar[re.Pattern[str]] = re.compile("(?:CreateCondaEnvironmentException|UnsatisfiableError):\n(.*)", re.MULTILINE | re.DOTALL)

    @staticmethod
    def _from_text(logs: str, stderr: str) -> Optional[SnakemakeCondaError]:
        for string in [logs, stderr]:
            if match := SnakemakeCondaError._pattern.search(string):
                return SnakemakeCondaError("CreateCondaEnvironmentException", match.group(1).strip())
        else:
            return None

@dataclasses.dataclass(frozen=True)
class SnakemakePythonError(WorkflowError):
    line_no: int
    file: Union[str, pathlib.Path]
    rest: str
    _pattern: ClassVar[re.Pattern[str]] = re.compile("(.*(?:Exception|Error|Exit)) in line (\\d*) of (.*):([\\s\\S]*)", re.MULTILINE)

    @staticmethod
    def _from_text(logs: str, stderr: str, code_dir: pathlib.Path) -> Optional[SnakemakePythonError]:
        for string in [logs, stderr]:
            if match := SnakemakePythonError._pattern.search(string):
                raw_file = match.group(3)
                file: Union[pathlib.Path, str]
                if raw_file.startswith("/"):
                    path = pathlib.Path(raw_file)
                    if path.is_relative_to(code_dir):
                        path = path.relative_to(code_dir)
                    file = path
                else:
                    file = raw_file
                return SnakemakePythonError(
                    match.group(1), int(match.group(2)), file, match.group(4).strip(),
                )
        else:
            return None


@dataclasses.dataclass(frozen=True)
class SnakemakeRuleError(WorkflowError):
    rule: str
    file: Union[str, pathlib.Path]
    rest: str
    _pattern: ClassVar[re.Pattern[str]] = re.compile("(.*(?:Exception|Error|Exit)) in rule (.*) .*of (.*):\n([\\s\\S]*)(?:\\Z|\n\n)", re.MULTILINE)

    @staticmethod
    def _from_text(logs: str, stderr: str, code_dir: pathlib.Path) -> Optional[SnakemakeRuleError]:
        for string in [logs, stderr]:
            if match := SnakemakeRuleError._pattern.search(string):
                raw_file = match.group(3)
                file: Union[pathlib.Path, str]
                if raw_file.startswith("/"):
                    path = pathlib.Path(raw_file)
                    if path.is_relative_to(code_dir):
                        path = path.relative_to(code_dir)
                    file = path
                else:
                    file = raw_file
                return SnakemakeRuleError(match.group(1), match.group(2), file, match.group(4).strip())
        else:
            return None


@dataclasses.dataclass(frozen=True)
class SnakemakeWorkflowError(WorkflowError):
    rest: str
    _pattern: ClassVar[re.Pattern[str]] = re.compile("WorkflowError:(.*)", re.MULTILINE | re.DOTALL)

    @staticmethod
    def _from_text(logs: str, stderr: str) -> Optional[SnakemakeWorkflowError]:
        for string in [logs, stderr]:
            if match := SnakemakeWorkflowError._pattern.search(string):
                return SnakemakeWorkflowError("SnakemakeError", match.group(1))
        else:
            return None


@dataclasses.dataclass(frozen=True)
class SnakemakeInternalError(WorkflowError):
    rest: str
    _pattern: ClassVar[re.Pattern[str]] = re.compile("Traceback \\(most recent call last\\):\n(.*\n\S.*\n)", re.MULTILINE | re.DOTALL)

    @staticmethod
    def _from_text(string: str) -> Optional[SnakemakeInternalError]:
        if match := SnakemakeInternalError._pattern.search(string):
            return SnakemakeInternalError("SnakemakeInternalError", match.group(1).strip())
        else:
            return None


@dataclasses.dataclass(frozen=True)
class SnakemakeInternalError2(WorkflowError):
    msg: str

    _pattern: ClassVar[re.Pattern[str]] = re.compile("\n([a-zA-Z0-9.]*(?:Exception|Error|Exit)):[ \n](.*)", re.MULTILINE)

    @staticmethod
    def _from_text(string: str) -> Optional[SnakemakeInternalError2]:
        if match := SnakemakeInternalError2._pattern.search(string):
            return SnakemakeInternalError2(match.group(1), match.group(2).strip())
        else:
            return None

class NextflowEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            code_dir: pathlib.Path,
            log_dir: pathlib.Path,
            out_dir: pathlib.Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        start_time = datetime.datetime.now()
        singularity_dir = code_dir.resolve().parent / "singularity"
        singularity_dir.mkdir()
        singularity_tmp_dir = code_dir.resolve().parent / "singularity-tmp"
        singularity_tmp_dir.mkdir()
        yield Executable(
            command=[
                "nextflow",
                "run",
                code_dir.resolve(),
                "-profile",
                "test,singularity",
                f"-process.cpus={n_cores}",
                f"--outdir",
                out_dir.resolve(),
            ],
            env_override={
                "SINGULARITY_CACHEDIR": str(singularity_dir),
                "NXF_SINGULARITY_CACHEDIR": str(singularity_dir),
                "SINGULARITY_TMPDIR": str(singularity_tmp_dir),
                "SINGULARITY_LOCALCACHEDIR": str(singularity_tmp_dir),
                "TMPDIR": str(singularity_tmp_dir),
            },
            cwd=code_dir.resolve(),
            read_write_mounts={
                code_dir: code_dir,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )
        for log_file in ["pipeline_info", ".nextflow", "work", ".nextflow.log"]:
            if (code_dir / log_file).exists():
                shutil.move(code_dir / log_file, log_dir / log_file)
        # Fallthrough, everything else goes to results.
        for fil in walk_files(code_dir):
            if fil.exists() and fil.is_file() and datetime.datetime.fromtimestamp(fil.stat().st_mtime) >= start_time:
                (out_dir / fil).parent.mkdir(exist_ok=True, parents=True)
                shutil.move(code_dir / fil, out_dir / fil)

    def parse_error(self, log_dir: pathlib.Path, code_dir: pathlib.Path, resources: ComputeResources, status_code: int) -> Optional[WorkflowError]:
        log_file = log_dir / ".nextflow.log"
        if not log_file.exists():
            return None
        log = log_file.read_text()
        err: Optional[WorkflowError]
        if err := NextflowCommandError._from_text(log, code_dir):
            return err
        elif err := NextflowJavaError._from_text(log):
            return err
        elif err := NextflowMiscError._from_text(log):
            return err
        elif err := NextflowSigterm._from_text(log):
            return err
        else:
            return None


@dataclasses.dataclass(frozen=True)
class NextflowCommandError(WorkflowError):
    process: str
    command_executed: str
    exit_status: int
    output: str
    error: str
    work_dir: pathlib.Path

    @staticmethod
    def _strip_indent(string: str, n: int) -> str:
        return "\n".join(line[n:] for line in string.split("\n")).strip()

    @staticmethod
    def _from_text(string: str, code_dir: pathlib.Path) -> Optional[NextflowCommandError]:
        if match := NextflowCommandError._pattern.search(string):
            work_dir = pathlib.Path(match.group(6))
            return NextflowCommandError(
                "CalledProcessError",
                match.group(1),
                NextflowCommandError._strip_indent(match.group(2), 2).strip(),
                int(match.group(3)),
                NextflowCommandError._strip_indent(match.group(4), 2),
                NextflowCommandError._strip_indent(match.group(5), 2),
                work_dir.relative_to(code_dir) if work_dir.is_relative_to(code_dir) else work_dir,
            )
        else:
            return None

    _pattern: ClassVar[re.Pattern[str]] = re.compile("Caused by:\n  (.*)\n\nCommand executed:\n([\\s\\S]*)\n\nCommand exit status:\n  (\\d*)\n\nCommand output:\n([\\s\\S]*)\n\nCommand error:\n([\\s\\S]*)\n\nWork dir:\n  (.*)\n", re.MULTILINE)


@dataclasses.dataclass(frozen=True)
class NextflowJavaError(WorkflowError):
    msg: str
    rest: str

    _pattern: ClassVar[re.Pattern[str]] = re.compile("\n([a-zA-Z0-9.]*(?:Exception|Error|Exit)): (.*)\n([\\s\\S]*)(?:\\Z|\n\n)", re.MULTILINE)

    @staticmethod
    def _from_text(string: str) -> Optional[NextflowJavaError]:
        if match := NextflowJavaError._pattern.search(string):
            return NextflowJavaError(match.group(1), match.group(2).strip(), match.group(3).strip())
        else:
            return None


@dataclasses.dataclass(frozen=True)
class NextflowMiscError(WorkflowError):
    date: str
    process: str
    class_: str
    rest: str

    _pattern: ClassVar[re.Pattern[str]] = re.compile("^([A-Z][a-z][a-z]-\\d\\d \\d\\d:\\d\\d:\\d\\d.\\d\\d\\d) \\[(.*)\\] ERROR (.*) - (.*)$", re.MULTILINE)

    @staticmethod
    def _from_text(string: str) -> Optional[NextflowMiscError]:
        if match := NextflowMiscError._pattern.search(string):
            return NextflowMiscError("NextflowMiscError", match.group(1), match.group(2), match.group(3), match.group(4).strip())
        else:
            return None


@dataclasses.dataclass(frozen=True)
class NextflowSigterm(WorkflowError):
    date: str

    _pattern: ClassVar[re.Pattern[str]] = re.compile("^([A-Z][a-z][a-z]-\\d\\d \\d\\d:\\d\\d:\\d\\d.\\d\\d\\d) \\[SIGTERM handler\\]", re.MULTILINE)

    @staticmethod
    def _from_text(string: str) -> Optional[NextflowSigterm]:
        if match := NextflowSigterm._pattern.search(string):
            return NextflowSigterm("Sigterm", match.group(1))
        else:
            return None


engines = {
    "snakemake": SnakemakeEngine(),
    "nextflow": NextflowEngine(),
}
