from __future__ import annotations
import os
import platform
import subprocess
import dataclasses
from datetime import timedelta as TimeDelta
from typing import Mapping, Optional, Iterable, ClassVar
from pathlib import Path
import warnings

from .util import create_temp_dir


@dataclasses.dataclass(frozen=True)
class Executable:
    command: list[bytes]
    cwd: Path = Path()
    read_only_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    read_write_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    env: Mapping[bytes, bytes] = dataclasses.field(default_factory=os.environ.copy)
    image: Optional[str] = None

    def prefix_command(self, prefix: list[bytes]) -> Executable:
        return Executable(
            command=prefix + self.command,
            cwd=self.cwd,
            read_only_mounts=self.read_only_mounts,
            read_write_mounts=self.read_write_mounts,
            env=self.env,
            image=self.image,
        )

    def timeout_executable(
            self,
            wall_time_soft_limit: TimeDelta,
            wall_time_hard_limit: TimeDelta,
    ) -> Executable:
        return self.prefix_command([
            b"timeout",
            "--kill-after={:.0f}".format(wall_time_hard_limit.total_seconds()).encode(),
            "{:.0f}".format(wall_time_soft_limit.total_seconds()).encode(),
        ])


    def taskset_executable(
            self,
            which_cores: list[int],
    ) -> Executable:
        core_list = b",".join(str(core).encode() for core in which_cores)
        return self.prefix_command([b"taskset", b"--cpu-list", core_list,])


    def time_local_execute(self) -> tuple[subprocess.CompletedProcess, ComputeResources]:
        with create_temp_dir() as temp_dir:
            executable = self.prefix([
                "time", f"--output={temp_dir!s}/time", "--format=%F %S %U %e %x",
            ])
            if executable.image is not None:
                raise NotImplementedError("This is not implemented for containerized images yet")
            proc = self.local_execute()
            time_output = (
                Path(temp_dir / "time").read_text().strip().split("\n")[-1].split(" ")
            )
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
        return (proc, ComputeResources(
            wall_time=TimeDelta(seconds=float(wall_time)),
            user_cpu_time=TimeDelta(seconds=float(user_sec)),
            system_cpu_time=TimeDelta(seconds=float(system_sec)),
            max_rss=int(mem_kb) * 1024,
        ))

    def local_execute(self: Executable) -> subprocess.CompletedProcess:
        proc = subprocess.run(
            self.command,
            cwd=self.cwd,
            env=self.env,
            check=False,
            capture_output=True,
        )
        return proc



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


@dataclasses.dataclass
class ComputeResources:
    user_cpu_time: TimeDelta
    system_cpu_time: TimeDelta
    wall_time: TimeDelta
    max_rss: int

    def check_invariants(self) -> Iterable[UserWarning]:
        if not all([
                self.user_cpu_time > TimeDelta(seconds=0),
                self.system_cpu_time > TimeDelta(seconds=0),
                self.wall_time > TimeDelta(seconds=0),
                self.max_rss > 0,
        ]):
            yield UserWarning("Negative values", self)
