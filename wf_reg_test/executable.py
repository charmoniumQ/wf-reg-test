from __future__ import annotations
import platform
import subprocess
import dataclasses
from datetime import timedelta as TimeDelta
from typing import Mapping, Optional, Iterable, ClassVar
from pathlib import Path


class Executable:
    command: list[bytes]
    cwd: Path
    read_only_mounts: Mapping[Path, Path]
    read_write_mounts: Mapping[Path, Path]
    env: Mapping[bytes, bytes]
    image: Optional[str]

    def check_invariants(self) -> Iterable[UserWarning]:
        pass


@dataclasses.dataclass(frozen=True)
class Machine:
    short_description: str
    long_description: str

    @staticmethod
    def current_machine() -> Machine:
        if Machine._CURRENT_MACHINE is None:
            Machine._CURRENT_MACHINE = Machine(
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
        return Machine._CURRENT_MACHINE

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.short_description}"

    _CURRENT_MACHINE: ClassVar[Optional[Machine]] = None

    def check_invariants(self) -> Iterable[UserWarning]:
        pass


class ComputeResources:
    user_cpu_time: TimeDelta
    system_cpu_time: TimeDelta
    wall_time: TimeDelta
    n_cores: int
    max_rss: int

    def check_invariants(self) -> Iterable[UserWarning]:
        if not all([
                self.user_cpu_time > TimeDelta(seconds=0),
                self.system_cpu_time > TimeDelta(seconds=0),
                self.wall_time > TimeDelta(seconds=0),
                self.n_cores > 0,
                self.max_rss > 0,
        ]):
            yield UserWarning("Negative values", self)
