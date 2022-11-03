from __future__ import annotations
import os
import platform
import subprocess
import dataclasses
from datetime import timedelta as TimeDelta
import contextlib
from typing import Mapping, Optional, Iterable, Iterator, ClassVar, Union, Any
from pathlib import Path
import warnings
import xml.etree.ElementTree

import charmonium.freeze

from .util import create_temp_dir, xml_to_dict


"""
# str vs bytes

I prefer a mixed approach rather than all str or all bytes. Here is why:

- I don't think it is common or possible to have non-ANSI bytes in `os.environ`,
  `Path`, or executable strings. These can be `str`, which interact better with
  Python (especially f-strings). `os.environ` already follows this convention
  and returns str.

- It is quite possible to have non-ANSI bytes in stdout. I don't trust programs
  to be "nice". Therefore, these are bytes.

"""


@dataclasses.dataclass(frozen=True)
class Executable:
    command: list[Union[str, Path]]
    cwd: Optional[Path] = None
    read_only_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    read_write_mounts: Mapping[Path, Path] = dataclasses.field(default_factory=dict)
    fresh_env: bool = False
    env_override: Mapping[str, str] = dataclasses.field(default_factory=dict)
    check: bool = False
    image: Optional[str] = None

    def local_execute(
            self: Executable,
            check: bool = True,
            capture_output: bool = True,
            time: int = False,
    ) -> CompletedProcess:
        proc = subprocess.run(
            [str(arg) for arg in self.command],
            cwd=self.cwd,
            env={
                **({} if self.fresh_env else dict(os.environ.items())),
                **{
                    var: val
                    for var, val in self.env_override.items()
                },
            },
            check=check,
            capture_output=capture_output,
        )
        return CompletedProcess(
            returncode=proc.returncode,
            stdout=proc.stdout,
            stderr=proc.stderr,
        )

    def to_env_command(self) -> list[str]:
        command = [str(arg) for arg in self.command]
        if self.fresh_env or self.env_override or self.cwd:
            prefix = ["env"]
            if self.cwd is not None:
                prefix += [f"--chdir={self.cwd.resolve()}"]
            if self.fresh_env:
                prefix += ["-"]
            if self.env_override:
                prefix += [
                    f"{key}={val}"
                    for key, val in self.env_override.items()
                ]
            return prefix + command
        else:
            return command


@dataclasses.dataclass(frozen=True)
class CompletedProcess:
    returncode: int
    stdout: bytes
    stderr: bytes


@dataclasses.dataclass(frozen=True)
class Machine:
    short_description: str
    details: Mapping[str, Any]

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
                details=xml_to_dict(
                    xml.etree.ElementTree.fromstring(
                        subprocess.run(
                            ["lstopo", "--output-format", "xml"],
                            check=True,
                            capture_output=True,
                            text=True,
                        ).stdout
                    )
                ),
            )
        return Machine._CURRENT_MACHINE

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.short_description}"

    _CURRENT_MACHINE: ClassVar[Optional[Machine]] = None


charmonium.freeze.config.constant_classes.add(("wf_reg_test.executable", "Machine"))


def taskset(
        executable: Executable,
        which_cores: list[int],
) -> Executable:
    core_list = ",".join(str(core) for core in which_cores)
    return Executable(
        command=["taskset", "--cpu-list", core_list, *executable.to_env_command()],
    )


def timeout(
        executable: Executable,
        wall_time_soft_limit: TimeDelta,
        wall_time_hard_limit: TimeDelta,
) -> Executable:
    return Executable(
        command=[
            "timeout",
            "--kill-after={:.0f}".format(wall_time_hard_limit.total_seconds()),
            "{:.0f}".format(wall_time_soft_limit.total_seconds()),
            *executable.to_env_command(),
        ],
    )


@contextlib.contextmanager
def time(executable: Executable) -> Iterator[tuple[Executable, Path]]:
    with create_temp_dir() as temp_dir:
        time_file = temp_dir.resolve() / "time"
        yield Executable(
            command=[
                "time",
                "--output",
                time_file,
                "--format=%M %S %U %e %x",
                *executable.to_env_command(),
            ],
        ), time_file


def parse_time_file(time_file: Path) -> ComputeResources:
    time_output = (
        time_file.read_text().strip().split("\n")[-1].split(" ")
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

@dataclasses.dataclass
class ComputeResources:
    user_cpu_time: TimeDelta
    system_cpu_time: TimeDelta
    wall_time: TimeDelta
    max_rss: int

    def check_invariants(self) -> Iterable[UserWarning]:
        if not all([
                self.user_cpu_time >= TimeDelta(seconds=0),
                self.system_cpu_time >= TimeDelta(seconds=0),
                self.wall_time >= TimeDelta(seconds=0),
                self.max_rss >= 0,
        ]):
            yield UserWarning("Negative values", self)
