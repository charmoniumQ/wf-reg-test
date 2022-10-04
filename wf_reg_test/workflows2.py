from __future__ import annotations
import abc
from typing import Mapping, DefaultDict, Optional, ContextManager, ClassVar
from pathlib import Path
from datetime import datetime as DateTime, timedelta as TimeDelta
from dataclasses import dataclass, fields
import platform
import subprocess
from typing import Any


@dataclass
class WorkflowApp2:
    workflow_engine_name: str
    url: str
    display_name: str
    repo_url: str
    revisions: list[Revision2]
    def __str__(self) -> str:
        return f"WorkflowApp2 {self.display_name}"


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

    def __str__(self) -> str:
        return f"Machine2 {self.short_description}"

    _CURRENT_MACHINE: ClassVar[Optional[Machine2]] = None
    _machine_cache: ClassVar[dict[str, Machine2]] = {}

_data_path = Path("data")
_data_key_digits = 16

_data_path.mkdir(exist_ok=True)

class RepoAccessor(abc.ABC):
    @abc.abstractmethod
    def get_revisions(self, wf_app: WorkflowApp2) -> list[Revision2]:
        ...

    @abc.abstractmethod
    def checkout(self, url: str) -> ContextManager[Path]:
        ...
