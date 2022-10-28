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
from .executable import Machine, Executable, ComputeResources
from .repos import get_repo


logger = logging.getLogger("wf_reg_test")


class Engine:
    def get_executable(
            self,
            workflow: Path,
            log_dir: Path,
            out_dir: Path,
            n_cores: int,
    ) -> Executable: ...


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
            executable = executable.taskset_executable(which_cores)
            executable = executable.timeout_executable(wall_time_hard_limit, wall_time_soft_limit)
            proc = executable.local_execute()
            (log_dir / "stdout.txt").write_bytes(proc.stdout)
            (log_dir / "stderr.txt").write_bytes(proc.stdout)
        return Execution(
            machine=Machine.current_machine(),
            datetime=now,
            outputs=FileBundle.create(out_dir),
            logs=FileBundle.create(log_dir),
            conditions=conditions,
            resources=expect_type(ComputeResources, proc.resources),
            status_code=proc.returncode,
            revision=revision,
        )


class SnakemakeEngine(Engine):
    def __init__(self) -> None:
        self.env = get_spack_env(Path() / "engines" / "snakemake")

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
                str(workflow / "workflow"),
            ],
            cwd=log_dir,
            env=self.env,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


class NextflowEngine(Engine):
    def __init__(self) -> None:
        self.env = get_spack_env(Path() / "engines" / "nextflow")

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
                f"{workflow}",
                f"-head-cpus={n_cores}",
                "-cache=false",
                "-profile=test,singularity",
                f"--out_dirdir={out_dir}",
            ],
            cwd=log_dir,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


env_line = re.compile(
    "^(?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*)$", flags=re.MULTILINE
)


def parse_env(env: str) -> Mapping[str, str]:
    return {
        match.group("var"): match.group("val")
        for match in env_line.finditer(env)
    }


bashrc_line = re.compile(
    "^export (?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*);?$", flags=re.MULTILINE
)


def parse_bashrc(env: str) -> Mapping[str, str]:
    return {
        match.group("var"): match.group("val")
        for match in bashrc_line.finditer(env)
    }


def get_nix_flake_env(flake: str) -> Mapping[str, str]:
    return parse_env(
        subprocess.run(
            ["nix", "develop", flake, "--command", "env"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )


def get_spack_env(env: Path) -> Mapping[str, str]:
    # TOOD: check that env is installed first
    return parse_bashrc(
        subprocess.run(
            ["spack", "env", "activate", "--dir", str(env), "--sh"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )


engine_constructors: Mapping[str, type[Engine]] = {
    "snakemake": SnakemakeEngine,
    "nextflow": NextflowEngine,
}


@functools.cache
def get_engine(engine: str) -> Engine:
    return engine_constructors[engine]()
