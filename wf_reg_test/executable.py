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


"""
str vs bytes:
I prefer a mixed approach rather than all str or all bytes. Here is why:

- I don't think it is common or possible to have non-ANSI bytes in
  `os.environ`, `Path`, or executable strings. As such, these can be
  `str`, which interact better with Python (especially f-strings)

- It is quite possible to have non-ANSI bytes in stdout. I don't trust
  programs to be "nice". Therefore, these are bytes.

"""


@dataclasses.dataclass(frozen=True)
class Executable:
    command: list[str]
    cwd: Path = Path()
    read_only_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    read_write_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    env: Mapping[str, str] = dataclasses.field(default_factory=os.environ.copy)
    check: bool = False
    image: Optional[str] = None

    def prefix_command(self, prefix: list[str]) -> Executable:
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
            "timeout",
            "--kill-after={:.0f}".format(wall_time_hard_limit.total_seconds()),
            "{:.0f}".format(wall_time_soft_limit.total_seconds()),
        ])


    def taskset_executable(
            self,
            which_cores: list[int],
    ) -> Executable:
        core_list = ",".join(str(core) for core in which_cores)
        return self.prefix_command(["taskset", "--cpu-list", core_list])


    @staticmethod
    def _parse_time_file(temp_dir: Path) -> ComputeResources:
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
        return ComputeResources(
            wall_time=TimeDelta(seconds=float(wall_time)),
            user_cpu_time=TimeDelta(seconds=float(user_sec)),
            system_cpu_time=TimeDelta(seconds=float(system_sec)),
            max_rss=int(mem_kb) * 1024,
        )

    def local_execute(
            self: Executable,
            check: bool = True,
            capture_output: bool = True,
            time: int = False,
    ) -> CompletedProcess:
        with create_temp_dir() as temp_dir:
            if time:
                executable = self.prefix_command([
                    "time", f"--output={temp_dir!s}/time", "--format=%F %S %U %e %x",
                ])
            proc = subprocess.run(
                self.command,
                cwd=self.cwd,
                env=self.env,
                check=check,
                capture_output=capture_output,
            )
            return CompletedProcess(
                returncode=proc.returncode,
                stdout=proc.stdout,
                stderr=proc.stderr,
                resources=self._parse_time_file(temp_dir) if time else None,
            )


@dataclasses.dataclass(frozen=True)
class CompletedProcess:
    returncode: int
    stdout: bytes
    stderr: bytes
    resources: Optional[ComputeResources]


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
