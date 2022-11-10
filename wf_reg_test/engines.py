import contextlib
import dataclasses
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

from .util import create_temp_dir, expect_type, walk_files
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
            path: Path,
            which_cores: list[int],
            wall_time_hard_limit: TimeDelta,
            wall_time_soft_limit: TimeDelta,
    ) -> Execution:
        if revision.workflow is None:
            raise ValueError(f"Can't run a revision that doesn't have workflow. {revision}")
        if condition.single_core != (len(which_cores) == 1):
            raise ValueError(f"Requested single-core={condition.single_core}, but assigned {len(which_cores)} cores")
        if condition.aslr or condition.faketime or condition.dev_random is not None or condition.rr_record or condition.rr_replay is not None:
            raise NotImplementedError()
        repo = get_repo(revision.workflow.repo_url)
        code = path / "code"
        log_dir = path / "log"
        out_dir = path / "out"
        now = DateTime.now()
        repo.checkout(revision, code)
        with self.get_executable(code, log_dir, out_dir, len(which_cores)) as executable:
            executable = taskset(executable, which_cores)
            executable = timeout(executable, wall_time_hard_limit, wall_time_soft_limit)
            with time(executable) as (executable, time_file):
                with ch_time_block.ctx(f"execute {revision.workflow}"):
                    proc = executable.local_execute(check=False, capture_output=True)
                    resources = parse_time_file(time_file)
            (log_dir / "stdout.txt").write_bytes(proc.stdout)
            (log_dir / "stderr.txt").write_bytes(proc.stdout)
        return Execution(
            machine=None,
            datetime=now,
            outputs=FileBundle.create(out_dir),
            logs=FileBundle.create(log_dir),
            condition=condition,
            resources=resources,
            status_code=proc.returncode,
            revision=None,
        )


class SnakemakeEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        test_file = log_dir / "test"
        test_file.touch()
        now = test_file.stat().st_mtime
        test_file.unlink()
        yield Executable(
            command=[
                "snakemake",
                f"--cores={n_cores}",
                "--use-singularity",
                "--forceall",
                "--shadow-prefix",
                log_dir.resolve(),
                "--snakefile",
                (workflow / "workflow/snakefile").resolve(),
            ],
            cwd=workflow,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )
        for fil in walk_files(workflow):
            if fil.stat().st_mtime >= now:
                shutil.move(workflow / fil, out_dir / fil)


class NextflowEngine(Engine):
    @contextlib.contextmanager
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Iterator[Executable]:
        yield Executable(
            command=[
                "nextflow",
                "run",
                workflow.resolve(),
                "-profile",
                "test,singularity",
                f"--outdir",
                out_dir.resolve(),
            ],
            cwd=log_dir.resolve(),
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


engines = {
    "snakemake": SnakemakeEngine(),
    "nextflow": NextflowEngine(),
}
