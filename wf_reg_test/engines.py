import dataclasses
import functools
import logging
import os
import random
import re
import shlex
import subprocess
import sys
import warnings
from typing_extensions import Protocol
from datetime import datetime as DateTime, timedelta as TimeDelta
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, TypeVar, cast

from .util import create_temp_dir, expect_type
from .workflows import Execution, Revision, ReproducibilityConditions, FileBundle
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
    ) -> Executable:
        raise NotImplementedError


    def run(
            self,
            revision: Revision,
            conditions: ReproducibilityConditions,
            which_cores: list[int],
            wall_time_hard_limit: TimeDelta,
            wall_time_soft_limit: TimeDelta,
    ) -> Execution:
        if revision.workflow is None:
            raise ValueError(f"Can't run a revision that doesn't have workflow. {revision}")
        repo = get_repo(revision.workflow.repo_url)
        with repo.checkout(revision) as local_copy, create_temp_dir() as log_dir, create_temp_dir() as out_dir:
            now = DateTime.now()
            executable = self.get_executable(local_copy, log_dir, out_dir, len(which_cores))
            executable = taskset(executable, which_cores)
            executable = timeout(executable, wall_time_hard_limit, wall_time_soft_limit)
            with time(executable) as (executable, time_file):
                proc = executable.local_execute()
                resources = parse_time_file(time_file)
            (log_dir / "stdout.txt").write_bytes(proc.stdout)
            (log_dir / "stderr.txt").write_bytes(proc.stdout)
        return Execution(
            machine=Machine.current_machine(),
            datetime=now,
            outputs=FileBundle.create(out_dir),
            logs=FileBundle.create(log_dir),
            conditions=conditions,
            resources=resources,
            status_code=proc.returncode,
            revision=revision,
        )


class SnakemakeEngine(Engine):
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Executable:
        return Executable(
            command=[
                "snakemake",
                f"--cores={n_cores}",
                "--use-singularity",
                "--forcerun",
                # TODO: determine out_dir bundle
                workflow / "workflow",
            ],
            cwd=log_dir,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


class NextflowEngine(Engine):
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Executable:
        return Executable(
            command=[
                "nextflow",
                "run",
                workflow,
                f"-head-cpus={n_cores}",
                "-cache=false",
                "-profile=test,singularity",
                f"--out_dirdir",
                out_dir,
            ],
            cwd=log_dir,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


engine_constructors: Mapping[str, type[Engine]] = {
    "snakemake": SnakemakeEngine,
    "nextflow": NextflowEngine,
}


def get_engine(engine: str) -> Engine:
    return engine_constructors[engine]()
