import abc
import dataclasses
from datetime import datetime
from pathlib import Path

import docker  # type: ignore

from .util import create_temp_dir
from .workflows import Execution, MerkleTreeNode

docker_client = docker.DockerClient(base_url="unix://var/run/docker.sock")


class WorkflowEngine:
    @abc.abstractmethod
    def run(self, workflow: Path) -> Execution:
        ...


@dataclasses.dataclass
class DockerWorkflowEngine(WorkflowEngine):
    name: str
    url: str
    image: str

    def run(self, workflow: Path) -> Execution:
        with create_temp_dir() as output_dir:
            output = docker_client.containers.run(
                image=self.image,
                command=self.get_command(workflow, output_dir),
                volumes={
                    str(workflow): {
                        "bind": str(workflow),
                        "mode": "rw",
                    },
                    str(output_dir): {
                        "bind": str(output_dir),
                        "mode": "rw",
                    },
                    "/var/run/docker.sock": {
                        "bind": "/var/run/docker.sock",
                        "mode": "rw",
                    },
                },
                working_dir="/workdir",
                remove=True,
                detach=False,
                log_config=docker.types.LogConfig(
                    type=docker.types.LogConfig.types.JSON,
                    config={},
                ),
                stdout=True,
                stderr=True,
            )
            (output_dir / "output").write_bytes(output)
            output_blobs = MerkleTreeNode.from_path(output_dir)
        return Execution(
            datetime=datetime.now(),
            output=output_blobs,
            success=True,  # TODO: fix this
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
        return ["sh", "-c", f"cp {workflow}/main.nf {output_dir}"]
        # return [
        #     "nextflow",
        #     "run",
        #     str(workflow),
        #     "-profile",
        #     "test,docker",
        #     "--outdir",
        #     str(output_dir),
        # ]
