from __future__ import annotations

import shutil
from datetime import datetime as DateTime, timedelta as TimeDelta
import dataclasses
from pathlib import Path
from typing import ClassVar, ContextManager, Optional, Iterable, Mapping

from .util import non_unique, concat_lists, hash_path
from .executable import Executable, ComputeResources, Machine


@dataclasses.dataclass
class RegistryHub:
    registries: list[Registry]

    def __str__(self) -> str:
        return f"{self.__class__.__name__} [{', '.join(str(registry) for registry in self.registries)}]"

    @property
    def workflows(self) -> list[Workflow]:
        return concat_lists(registry.workflows for registry in self.registries)

    def check_invariants(self) -> Iterable[UserWarning]:
        for reg_i, reg_j, _, _ in non_unique(registry.url for registry in self.registries):
            yield UserWarning("Two registries have the same URL", reg_i, reg_j)
        for reg_i, reg_j, _, _ in non_unique(registry.display_name for registry in self.registries):
            yield UserWarning("Two registries have the same display_name", reg_i, reg_j)
        for registry in self.registries:
            yield from registry.check_invariants()


@dataclasses.dataclass
class Registry:
    display_name: str
    url: str
    workflows: list[Workflow]

    def __add__(self, other: Registry) -> Registry:
        if (other.display_name, other.url) != (self.display_name, self.url):
            raise RuntimeError(f"Cannot add different registries: {self} + {other}")
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name}"

    def check_invariants(self) -> Iterable[UserWarning]:
        for wf_i, wf_j, _, _ in non_unique(wf.url for wf in self.workflows):
            yield UserWarning("Two workflows have the same URL", wf_i, wf_j)
        for wf_i, wf_j, _, _ in non_unique(wf.display_name for wf in self.workflows):
            yield UserWarning("Two workflows have the same display_name", wf_i, wf_j)
        for wf in self.workflows:
            if wf.registry != self:
                yield UserWarning("Workflow does not point back to self", wf, self)
            yield from wf.check_invariants()


@dataclasses.dataclass
class Workflow:
    """Note that this is termed "computational experiment" when
    writing about this research (see docs/).

    """
    engine: str
    url: str
    display_name: str
    repo_url: str
    revisions: list[Revision]
    registry: Registry = dataclasses.field(compare=False)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name}"

    def __add__(self, other: Workflow) -> Workflow:
        raise NotImplementedError()
        url_to_revisions = {
            revision.url: revision
            for revision in self.revisions
        }
        for revision in other.revisions:
            if revision.url in url_to_revisions:
                url_to_revisions[revision.url].merge(revision)
            else:
                self.revisions.append(revision)

    def check_invariants(self) -> Iterable[UserWarning]:
        for revision in self.revisions:
            if revision.workflow != self:
                yield UserWarning("Revision does not point back to self", revision, self)
            yield from revision.check_invariants()


@dataclasses.dataclass
class Revision:
    display_name: str
    url: str
    rev: str
    datetime: DateTime
    executions: list[Execution]
    workflow: Optional[Workflow] = dataclasses.field(compare=False)

    def check_invariants(self) -> Iterable[UserWarning]:
        for execution in self.executions:
            if execution.revision != self:
                yield UserWarning("Execution does not point back to self", execution, self)
            yield from execution.check_invariants()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name} of {self.workflow}"

    def __add__(self, other: Revision) -> Revision:
        raise NotImplementedError
        machine_time_to_executions = {
            (execution.machine, execution.datetime): execution
            for execution in self.executions
        }
        for execution in other.executions:
            if (execution.machine, execution.datetime) in machine_time_to_executions:
                pass
            else:
                self.executions.append(execution)


@dataclasses.dataclass
class Execution:
    machine: Machine
    datetime: DateTime
    outputs: FileBundle
    logs: FileBundle
    conditions: ReproducibilityConditions
    resources: ComputeResources
    status_code: int
    revision: Revision = dataclasses.field(compare=False)

    def check_invariants(self) -> Iterable[UserWarning]:
        yield from self.outputs.check_invariants()
        yield from self.machine.check_invariants()
        yield from self.resources.check_invariants()
        yield from self.conditions.check_invariants()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} of {self.revision}"


@dataclasses.dataclass(frozen=True)
class ReproducibilityConditions:
    single_core: bool
    aslr: bool
    faketime: Optional[DateTime]
    dev_random: Optional[RandomStream]

    def check_invariants(self) -> Iterable[UserWarning]:
        pass


@dataclasses.dataclass(frozen=True)
class RandomStream:
    seed: int
    method: str = "stdlib"


@dataclasses.dataclass(frozen=True)
class FileBundle:
    contents: Mapping[Path, File]

    @staticmethod
    def create(root: Path) -> FileBundle:
        contents: dict[Path, File] = {}
        for dir_ in root.glob("**"):
            for path in dir_.iterdir():
                # note that root.glob already handles recursing into subdirs.
                if path.is_file() and not path.is_symlink():
                    contents[path.relative_to(root)] = File.create(path)
        return FileBundle(contents)

    def total_size(self) -> int:
        return sum(file.size for file in self.contents.values())

    def check_invariants(self) -> Iterable[UserWarning]:
        for file in self.contents.values():
            yield from file.check_invariants()


@dataclasses.dataclass(frozen=True)
class File:
    hash_algo: str
    hash_bits: int
    hash_val: int
    size: int
    contents_url: Optional[str] = dataclasses.field(compare=False, hash=False)

    @staticmethod
    def create(path: Path) -> File:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"{path} is not a regular file")
        return File(
            hash_algo="xxhash",
            hash_bits=64,
            hash_val=hash_path(path, size=64),
            size=path.stat().st_size,
            contents_url=None,
        )

    def check_invariants(self) -> Iterable[UserWarning]:
        if 0 <= self.hash_val < (1 << self.hash_bits):
            yield UserWarning("hash is bigger than hash_bits", self, self.hash_val, self.hash_bits)
        if self.size < 0:
            yield UserWarning("File cannot have negative size")

    def read_bytes(self) -> Optional[bytes]:
        """Return the bytes of this file, if we have them, else None."""
        # I guess we never have them :/
        return None
