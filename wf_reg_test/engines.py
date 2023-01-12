import contextlib
import dataclasses
import datetime
import functools
import logging
import random
import re
import shlex
import shutil
import subprocess
import sys
import warnings
from typing_extensions import Protocol
from datetime import datetime as DateTime, timedelta as TimeDelta
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, TypeVar, cast, ContextManager, Iterator

import charmonium.time_block as ch_time_block
import yaml
from upath import UPath

from .util import create_temp_dir, expect_type, walk_files, random_str, fs_escape
from .workflows import Execution, Revision, Condition, FileBundle
from .executable import Machine, Executable, ComputeResources, time, timeout, taskset, parse_time_file
from .repos import get_repo


logger = logging.getLogger("wf_reg_test")


class Engine:
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> ContextManager[Executable]:
        raise NotImplementedError


    def run(
            self,
            revision: Revision,
            condition: Condition,
            which_cores: list[int],
            wall_time_limit: TimeDelta,
            storage: UPath,
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
                executable = taskset(executable, which_cores)
                executable = timeout(executable, wall_time_limit)
                with time(executable) as (executable, time_file):
                    with ch_time_block.ctx(f"execute {revision.workflow}"):
                        now = DateTime.now()
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
            outputs = FileBundle.create_in_storage(out_dir, run_path / "output.tar.xz")
            logs = FileBundle.create_in_storage(log_dir, run_path / "logs.tar.xz")
        return Execution(
            machine=None,
            datetime=now,
            outputs=outputs,
            logs=logs,
            condition=condition,
            resources=resources,
            status_code=proc.returncode,
            revision=None,
        )


class SnakemakeEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            code_dir: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        start_time = datetime.datetime.now()
        # See for typical snakefile locations:
        # https://github.com/friendsofstrandseq/mosaicatcher-pipeline/tree/1.4.1/ -> ./Snakefile
        # https://github.com/friendsofstrandseq/mosaicatcher-pipeline/tree/1.8.4/ -> ./workflow/Snakefile
        possible_snakefiles = ["snakefile", "Snakefile", "workflow/snakefile", "workflow/Snakefile"]
        try:
            snakefile = next(
                path
                for path in possible_snakefiles
                if (code_dir / path).exists()
            )
        except StopIteration as exc:
            yield Executable(
                command=["/usr/bin/echo", "Could not find [Ss]nakefile"],
                cwd=code_dir,
            )
        yield Executable(
            command=[
                "snakemake",
                f"--cores={n_cores}",
                "--use-singularity",
                "--use-conda",
                "--forceall",
                f"--snakefile={snakefile!s}",
            ],
            cwd=code_dir,
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
            if fil.exists() and fil.is_file() and DateTime.fromtimestamp(fil.stat().st_mtime) >= start_time:
                (out_dir / fil).parent.mkdir(exist_ok=True, parents=True)
                shutil.move(code_dir / fil, out_dir / fil)


class NextflowEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            code_dir: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        start_time = datetime.datetime.now()
        yield Executable(
            command=[
                "nextflow",
                "run",
                code_dir.resolve(),
                "-profile",
                "test,singularity",
                f"--outdir",
                out_dir.resolve(),
            ],
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
            if fil.exists() and fil.is_file() and DateTime.fromtimestamp(fil.stat().st_mtime) >= start_time:
                (out_dir / fil).parent.mkdir(exist_ok=True, parents=True)
                shutil.move(code_dir / fil, out_dir / fil)


engines = {
    "snakemake": SnakemakeEngine(),
    "nextflow": NextflowEngine(),
}
