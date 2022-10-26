from __future__ import annotations

import shutil
from datetime import datetime as DateTime, timedelta as TimeDelta
import dataclasses
from pathlib import Path
from typing import ClassVar, ContextManager, Optional, Iterable, Mapping
from typing_extensions import Protocol
from .util import non_unique
from .executable import Executable, ComputeResources, Machine


@dataclasses.dataclass
class RegistryHub:
    registries: list[Registry]
    workflow_engines: Mapping[str, WorkflowEngine]

    def __str__(self) -> str:
        return f"{self.__class__.__name__} [{', '.join(str(registry) for registry in self.registries)}]"

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
    workflows: list[Workflow] = []

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
    engine: WorkflowEngine
    url: str
    display_name: str
    repo_url: str
    revisions: list[Revision]
    registry: Registry

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
        yield from self.engine.check_invariants()
        for revision in self.revisions:
            if revision.workflow != self:
                yield UserWarning("Revision does not point back to self", revision, self)
            yield from revision.check_invariants()


class WorkflowEngine(Protocol):
    def check_invariants(self) -> Iterable[UserWarning]:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name}"

    @property
    def display_name(self) -> str: ...

    def run(self, path: Path) -> Executable: ...


@dataclasses.dataclass
class Revision:
    display_name: str
    url: str
    datetime: DateTime
    executions: list[Execution]
    workflow: Workflow

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
    output: FileTree
    conditions: ReproducibilityConditions
    resources: ComputeResources
    status_code: int
    revision: Revision

    def check_invariants(self) -> Iterable[UserWarning]:
        yield from self.output.check_invariants()
        yield from self.machine.check_invariants()
        yield from self.resources.check_invariants()
        yield from self.conditions.check_invariants()
        if self.conditions.single_core == (self.resources.n_cores == 1):
            yield UserWarning("self.conditions.single_core != (self.resources.n_cores == 1)", self, self.conditions, self.resources)

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
class FileTree:
    hash_algorithm: str
    hash_bits: int
    hashes: Mapping[Path, int]
    contents: Mapping[Path, FileBytesObject]

    def check_invariants(self) -> Iterable[UserWarning]:
        for path, hash_val in self.hashes.items():
            if 0 <= hash_val < (1 << self.hash_bits):
                yield UserWarning("hash is bigger than hash_bits", self, path, hash_val, self.hash_bits)

        remainder = self.contents.keys() - self.hashes.keys()
        if remainder:
            yield UserWarning("contents has paths which are not hashed", self, remainder)


class FileBytesObject(Protocol):
    def read_bytes(self) -> bytes: ...

    def check_invariants(self) -> Iterable[UserWarning]:
        pass
