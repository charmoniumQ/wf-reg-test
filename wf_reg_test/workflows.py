from __future__ import annotations
import abc
import dataclasses
from pathlib import Path
from typing import Mapping, Optional


from .util import hash_path, walk
from .repos import Repo


@dataclasses.dataclass
class WorkflowApp:
    repo: Repo
    workflow_engine: WorkflowEngine
    url: Optional[str] = None


class WorkflowEngine(abc.ABC):
    @abc.abstractmethod
    def run(self, workflow: Path) -> Execution:
        ...


@dataclasses.dataclass
class Execution:
    input_blobs: FileBundle
    output_blobs: FileBundle
    success: bool


@dataclasses.dataclass
class FileBundle:
    contents: Mapping[Path, Blob]

    @staticmethod
    def create(path: Path) -> FileBundle:
        return FileBundle(contents={
            subpath: Blob(hash_path(subpath))
            for subpath in walk(path)
            if subpath.is_file()
        })


@dataclasses.dataclass(eq=True, frozen=True)
class Blob:
    hash: bytes
