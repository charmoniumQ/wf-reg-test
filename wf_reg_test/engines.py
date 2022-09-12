import abc
import dataclasses
from datetime import datetime, timedelta
from pathlib import Path
import sys
from typing import Mapping, Any

import docker  # type: ignore
import requests
from sqlalchemy.orm import Session

from .util import create_temp_dir
from .workflows import Execution, MerkleTreeNode

docker_client = docker.DockerClient(base_url="unix://var/run/docker.sock")


class WorkflowEngine:
    @abc.abstractmethod
    def run(self, workflow: Path, session: Session) -> Execution:
        ...


def monitor_stats(container: docker.models.containers.Container) -> Mapping[str, Any]:
    user_cpu_time = 0
    kernel_cpu_time = 0
    max_rss = 0
    start_time = datetime.now()
    for stats in container.stats(stream=True, decode=True):
        user_cpu_time = max(user_cpu_time, stats["cpu_stats"]["cpu_usage"]["usage_in_usermode"])
        kernel_cpu_time = max(kernel_cpu_time, stats["cpu_stats"]["cpu_usage"]["usage_in_kernelmode"])
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
            container = docker_client.containers.run(
                image=self.image,
                command=self.get_command(workflow, output_dir),
                volumes={
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
                working_dir="/workdir",
                detach=True,
                log_config=docker.types.LogConfig(
                    type=docker.types.LogConfig.types.JSON,
                    config={},
                ),
            )
            stats = monitor_stats(container)
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
            )

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        raise NotImplementedError("Override and implement in a subclass")


class Nextflow(DockerWorkflowEngine):
    def __init__(self) -> None:
        super().__init__(
            name="Nextflow",
            url="https://www.nextflow.io/",
            image="index.docker.io/nextflow/nextflow:22.09.1-edge",
        )

    def get_command(self, workflow: Path, output_dir: Path) -> list[str]:
        return ["sh", "-c", f"cp {workflow.resolve()!s}/main.nf {output_dir.resolve()!s}"]
        # return [
        #     "nextflow",
        #     "run",
        #     str(workflow),
        #     "-profile",
        #     "test,docker",
        #     "--outdir",
        #     str(output_dir),
        # ]


engines = {
    "nextflow": Nextflow(),
}
