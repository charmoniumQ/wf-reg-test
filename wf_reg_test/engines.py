import dataclasses
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

from .util import create_temp_dir
from .workflows import Execution, Revision, ReproducibilityConditions
from .executable import Machine, Executable
from .repos import get_repo


logger = logging.getLogger("wf_reg_test")


class Engine(Protocol):
    def get_executable(self, workflow: Path, log_dir: Path, out_dir: Path, n_cores: int) -> Executables: ...

    def run(
            self,
            revision: Revision,
            conditions: ReproducibilityConditions,
            which_cores: list[int],
            wall_time_hard_limit: TimeDelta,
            wall_time_soft_limit: TimeDelta,
    ) -> Execution:
        repo = get_repo(revision.workflow.repo_url)
        with repo.checkout(revision) as local_copy, create_temp_dir() as log_dir, create_temp_dir() as out_dir:
            executable = self.get_executable(local_copy, log_dir, out_dir, len(which_cores))
            executable = taskset_executable(executable, which_cores)
            executable = timeout_executable(executable, wall_time_hard_limit, wall_time_soft_limit)
            proc, resources = executable.time_local_executable()
            (log_dir / "stdout.txt").write_bytes(proc.stdout)
            (log_dir / "stderr.txt").write_bytes(proc.stdout)


class SnakeMakeExecutor:
    def __init__(self) -> None:
        self.env = get_spack_env(Path() / "engines" / "snakemake")

    def run(self, workflow: Path, log_dir: Path, out_dir: Path, n_cores: int) -> Executable:
        return Executable(
            command=[
                b"snakemake",
                b"--cores",
                str(n_cores).encode(),
                b"--use-singularity",
                b"--forcerun",
                # TODO: determine out_dir bundle
                bytes(workflow / "workflow"),
            ],
            cwd=log_dir,
            env=self.env,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


class NextflowExecutor:
    def __init__(self) -> None:
        self.env = get_spack_env(Path() / "engines" / "nextflow")

    def run(self, workflow: Path, log_dir: Path, out_dir: Path, n_cores: int) -> Executable:
        return Executable(
            command=[
                b"nextflow",
                b"run",
                str(workflow).encode(),
                f"-head-cpus={n_cores}".encode(),
                b"-cache=false",
                b"-profile=test,singularity",
                f"--out_dirdir={out_dir}".encode(),
            ],
            cwd=log_dir,
            read_write_mounts={
                workflow: workflow,
                log_dir: log_dir,
                out_dir: out_dir,
            },
        )


env_line = re.compile(
    b"^(?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*)$", flags=re.MULTILINE
)


def parse_env(env: bytes) -> Mapping[bytes, bytes]:
    return {
        match.group("var"): match.group("val")
        for match in env_line.finditer(env)
    }


bashrc_line = re.compile(
    b"^export (?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*);?$", flags=re.MULTILINE
)


def parse_bashrc(env: bytes) -> Mapping[bytes, bytes]:
    return {
        match.group("var"): match.group("val")
        for match in bashrc_line.finditer(env)
    }


def get_nix_flake_env(flake: str) -> Mapping[bytes, bytes]:
    return parse_env(
        subprocess.run(
            ["nix", "develop", flake, "--command", "env"],
            check=True,
            capture_output=True,
        ).stdout
    )


def get_spack_env(env: Path) -> Mapping[bytes, bytes]:
    # TOOD: check that env is installed first
    return parse_bashrc(
        subprocess.run(
            ["spack", "env", "activate", "--dir", str(env), "--sh"],
            check=True,
            capture_output=True,
        ).stdout
    )
