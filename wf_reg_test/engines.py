import abc
import dataclasses
import getpass
import itertools
import logging
import os
import shlex
import subprocess
import sys
import warnings
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Optional

import docker  # type: ignore
import requests
from sqlalchemy.orm import Session

from .util import create_temp_dir
from .workflows import Execution, Machine, MerkleTreeNode

docker_client = docker.DockerClient(base_url="unix://var/run/docker.sock")

logger = logging.getLogger("wf_reg_test")


class WorkflowEngine:
    @abc.abstractmethod
    def run(self, workflow: Path, session: Session) -> Execution:
        ...


def docker_command(
        image: str,
        command: Optional[list[str]] = None,
        volumes: Optional[Mapping[str, Mapping[str, str]]] = None,
        workdir: Optional[str] = None,
        detach: bool = False,
        remove: bool = False,
) -> str:
    return shlex.join([
        "docker",
        "run",
        *(["--rm"] if remove else []),
        *(["--detach"] if detach else []),
        *(list(itertools.chain.from_iterable(
            ["--volume", ":".join([path, volume["bind"], volume["mode"]])]
            for path, volume in volumes.items()
        )) if volumes is not None else []),
        *(["--workdir", workdir] if workdir is not None else []),
        image,
        *(command if command is not None else []),
    ])


def docker_chown(paths: list[Path]) -> None:
    username = getpass.getuser()
    # gid = os.getgid()
    uid = os.getuid()
    command0 = shlex.join(["adduser", "--uid", str(uid), str(username)])
    command1 = shlex.join(
        [
            "chown",
            "--recursive",
            str(username),
            *[str(path.resolve()) for path in paths],
        ]
    )
    print(f"docker run --rm ubuntu:22.04 sh -c '{command0} && {command1}'")
    docker_client.containers.run(
        image="ubuntu:22.04",
        command=f"sh -c '{command0} && {command1}'",
        remove=True,
        detach=False,
        volumes={
            str(path.resolve()): {
                "bind": str(path.resolve()),
                "mode": "rw",
            }
            for path in paths
        },
    )


def docker_monitor_stats(
    container: docker.models.containers.Container,
) -> Mapping[str, Any]:
    user_cpu_time = 0
    kernel_cpu_time = 0
    max_rss = 0
    start_time = datetime.now()
    for stats in container.stats(stream=True, decode=True):
        user_cpu_time = max(
            user_cpu_time, stats["cpu_stats"]["cpu_usage"]["usage_in_usermode"]
        )
        kernel_cpu_time = max(
            kernel_cpu_time, stats["cpu_stats"]["cpu_usage"]["usage_in_kernelmode"]
        )
        max_rss = max(max_rss, stats["memory_stats"].get("usage", 0))
        try:
            exit_info = container.wait(timeout=1)
        except requests.ConnectionError:
            # Hit timeout
            pass
        else:
            break
    elapsed_wall_time = datetime.now() - start_time
    stdout = container.attach(stdout=True, stderr=False, stream=False, logs=True)
    stderr = container.attach(stdout=False, stderr=True, stream=False, logs=True)
    container.remove()
    return {
        "user_cpu_time": timedelta(microseconds=user_cpu_time // 1000),
        "kernel_cpu_time": timedelta(microseconds=kernel_cpu_time // 1000),
        "max_rss": max_rss,
        "wall_time": elapsed_wall_time,
        "status_code": exit_info["StatusCode"],
        "stdout": stdout,
        "stderr": stderr,
    }


@dataclasses.dataclass
class DockerWorkflowEngine(WorkflowEngine):
    name: str
    url: str
    image: str

    def run(self, workflow: Path, session: Session) -> Execution:
        with create_temp_dir() as output_dir:
            docker_args = {
                "image": self.image,
                "command": self.get_command(workflow, output_dir),
                "volumes": {
                    str(workflow.resolve()): {
                        "bind": str(workflow.resolve()),
                        "mode": "rw",
                    },
                    str(output_dir.resolve()): {
                        "bind": str(output_dir.resolve()),
                        "mode": "rw",
                    },
                    "/var/run/docker.sock": {
                        "bind": "/var/run/docker.sock",
                        "mode": "rw",
                    },
                },
                "working_dir": "/workdir",
                "detach": True,
                "log_config": docker.types.LogConfig(
                    type=docker.types.LogConfig.types.JSON,
                    config={},
                ),
            }
            if logger.isEnabledFor(logging.INFO):
                logger.info("Running: " + docker_command(**docker_args))
            container = docker_client.containers.run(**docker_args)
            stats = docker_monitor_stats(container)
            docker_chown([workflow, output_dir])
            (output_dir / "stdout").write_bytes(stats["stdout"])
            (output_dir / "stderr").write_bytes(stats["stderr"])
            sys.stderr.buffer.write(stats["stderr"])
            return Execution(
                datetime=datetime.now(),
                output=MerkleTreeNode.from_path(output_dir, session, {}, {}),
                status_code=stats["status_code"],
                wall_time=stats["wall_time"],
                user_cpu_time=stats["user_cpu_time"],
                system_cpu_time=stats["kernel_cpu_time"],
                max_rss=stats["max_rss"],
                machine=Machine.current_host(session),
            )

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        raise NotImplementedError("Override and implement in a subclass")


@dataclasses.dataclass
class NixWorkflowEngine(WorkflowEngine):
    name: str
    url: str
    flake: Path
    keep_env_vars: tuple[str, ...] = ()

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        raise NotImplementedError("Override and implement in a subclass")

    def run(self, workflow: Path, session: Session) -> Execution:
        with create_temp_dir() as output_dir:
            command = self.get_command(workflow, output_dir)
            time_command = [
                "time",
                f"--output={output_dir!s}/time",
                "--format=%F %S %U %e %x",
                *command,
            ]
            nix_time_command = [
                "nix",
                "develop",
                "--ignore-environment",
                str(self.flake.resolve()),
                *itertools.chain.from_iterable(
                    ["--keep", env_var] for env_var in self.keep_env_vars
                ),
                "--command",
                *time_command,
            ]
            if logger.isEnabledFor(logging.INFO):
                logger.info("Running: " + shlex.join(nix_time_command))
            proc = subprocess.run(
                nix_time_command,
                check=False,
                capture_output=True,
            )
            (output_dir / "stdout").write_bytes(proc.stdout)
            (output_dir / "stderr").write_bytes(proc.stderr)
            sys.stderr.buffer.write(proc.stderr)
            time_output = Path(output_dir / "time").read_text().strip().split("\n")[-1].split(" ")
            try:
                mem_kb, system_sec, user_sec, wall_time, exit_status = time_output
            except ValueError:
                mem_kb = "0"
                system_sec = "0.0"
                user_sec = "0.0"
                wall_time = "0.0"
                exit_status = "0"
                warnings.warn(
                    f"Could not parse time output: {time_output!r}; setting those fields to 0"
                )
            return Execution(
                datetime=datetime.now(),
                output=MerkleTreeNode.from_path(output_dir, session, {}, {}),
                status_code=int(exit_status),
                wall_time=timedelta(seconds=float(wall_time)),
                user_cpu_time=timedelta(seconds=float(user_sec)),
                system_cpu_time=timedelta(seconds=float(system_sec)),
                max_rss=int(mem_kb) * 1024,
                machine=Machine.current_host(session),
            )


class NextflowDocker(DockerWorkflowEngine):
    def __init__(self) -> None:
        super().__init__(
            name="Nextflow",
            url="https://www.nextflow.io/",
            image="index.docker.io/nextflow/nextflow:22.09.3-edge",
        )

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        return [
            "nextflow",
            "run",
            str(workflow.resolve()),
            "-profile",
            "test,docker",
            "--outdir",
            str(output_dir.resolve()),
        ]


class NextflowNix(NixWorkflowEngine):
    def __init__(self) -> None:
        super().__init__(
            name="Nextflow",
            url="https://www.nextflow.io/",
            flake=Path() / "engines" / "nextflow",
            keep_env_vars=("HOME",),
        )

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        return [
            "nextflow",
            "run",
            str(workflow.resolve()),
            "-profile",
            "test,docker",
            "--outdir",
            str(output_dir.resolve()),
        ]
        # return [
        #     "sh",
        #     "-c",
        #     "head --bytes 8388608 /dev/urandom | xz -9e - | unxz - | wc -c",
        # ]


engines = {
    "nextflow-docker": NextflowDocker(),
    "nextflow": NextflowNix(),
}
