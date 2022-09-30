from __future__ import annotations
import abc
from typing import Mapping, DefaultDict, Optional, ContextManager, ClassVar
from pathlib import Path
from datetime import datetime as DateTime, timedelta as TimeDelta
from dataclasses import dataclass, fields
import platform
import subprocess
from typing import Any
WorkflowApp1 = Any
Revision1 = Any
Execution1 = Any
Machien1 = Any
MerkleTreeNode = Any
Blob = Any
# from .workflows import (
#     WorkflowApp as WorkflowApp1,
#     Revision as Revision1,
#     Execution as Execution1,
#     Machine as Machine1,
#     MerkleTreeNode,
#     Blob,
# )

@dataclass
class WorkflowApp2:
    workflow_engine_name: str
    url: str
    display_name: str
    repo_url: str
    revisions: list[Revision2]
    def __str__(self) -> str:
        return f"WorkflowApp2 {self.display_name}"

    @staticmethod
    def convert(wf_app1: WorkflowApp1) -> WorkflowApp2:
        wf_app = WorkflowApp2(
            workflow_engine_name=wf_app1.workflow_engine_name,
            url=wf_app1.url,
            display_name=wf_app1.display_name,
            repo_url=wf_app1.repo_url,
            revisions=[],
        )
        for revision in wf_app1.revisions:
            wf_app.revisions.append(Revision2.convert(revision, wf_app))
        return wf_app


@dataclass
class Revision2:
    display_name: str
    url: str
    datetime: DateTime
    tree: Optional[Path]
    executions: list[Execution2]
    workflow_app: WorkflowApp2

    def __str__(self) -> str:
        return f"Revision2 {self.display_name} of {self.workflow_app}"

    @staticmethod
    def convert(revision1: Revision1, workflow_app: WorkflowApp2) -> Revision2:
        revision = Revision2(
            display_name=revision1.display_name,
            url=revision1.url,
            datetime=revision1.datetime,
            tree=None,
            workflow_app=workflow_app,
            executions=[],
        )
        for execution in revision1.executions:
            revision.executions.append(Execution2.convert(execution, revision))
        return revision

@dataclass
class Execution2:
    machine: Machine2
    datetime: DateTime
    output: Path
    status_code: int
    user_cpu_time: TimeDelta
    system_cpu_time: TimeDelta
    max_rss: int
    wall_time: TimeDelta
    revision: Revision2

    def __str__(self) -> str:
        return f"Execution2 of {self.revision}"

    @staticmethod
    def convert(execution: Execution1, revision: Revision2) -> Execution2:
        return Execution2(
            revision=revision,
            machine=Machine2.convert(execution.machine),
            datetime=execution.datetime,
            output=serialize_tree(execution.output),
            status_code=execution.status_code,
            user_cpu_time=execution.user_cpu_time,
            system_cpu_time=execution.system_cpu_time,
            max_rss=execution.max_rss,
            wall_time=execution.wall_time,
        )

@dataclass(frozen=True)
class Machine2:
    short_description: str
    long_description: str

    @staticmethod
    def current_host() -> Machine2:
        if Machine2._CURRENT_MACHINE is None:
            Machine2._CURRENT_MACHINE = Machine2(
                short_description="-".join(
                    [
                        platform.node(),
                        platform.platform(),
                    ]
                ),
                long_description=subprocess.run(
                    ["lstopo", "--output-format", "xml"],
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout,
            )
        return Machine2._CURRENT_MACHINE

    @staticmethod
    def convert(machine: Machine1) -> Machine2:
        return Machine2._machine_cache.setdefault(
            machine.short_description,
            Machine2(
                short_description=machine.short_description,
                long_description=machine.long_description,
            ),
        )

    def __str__(self) -> str:
        return f"Machine2 {self.short_description}"

    _CURRENT_MACHINE: ClassVar[Optional[Machine2]] = None
    _machine_cache: ClassVar[dict[str, Machine2]] = {}

_data_path = Path("data")
_data_key_digits = 16

_data_path.mkdir(exist_ok=True)

def serialize_tree(mtn: MerkleTreeNode) -> Path:
    result_path = _data_path / "{:016x}".format(mtn.hash + (1 << 63))
    mtn.name = "."
    serialize_rooted_tree(mtn, result_path)
    return result_path

def serialize_rooted_tree(mtn: MerkleTreeNode, root: Path) -> None:
    if mtn.blob is not None:
        assert not mtn.children
        (root / mtn.name).write_bytes(mtn.blob.data)
    else:
        (root / mtn.name).mkdir()
        for child in mtn.children:
            serialize_rooted_tree(child, root / mtn.name)


class RepoAccessor(abc.ABC):
    @abc.abstractmethod
    def get_revisions(self, wf_app: WorkflowApp2) -> list[Revision2]:
        ...

    @abc.abstractmethod
    def checkout(self, url: str) -> ContextManager[Path]:
        ...
