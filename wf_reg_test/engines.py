import dataclasses
import logging
import os
import random
import re
import shlex
import subprocess
import sys
import warnings
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, TypeVar, cast

from .workflows2 import Execution2 as Execution
from .workflows2 import Machine2 as Machine
from .workflows2 import Revision2 as Revision

try:
    import docker  # type: ignore
except ImportError:

    class DockerClient:
        def __getattr__(self, attr: str) -> Any:
            raise RuntimeError("Python Docker is not installed.")

else:
    docker_client = docker.DockerClient(base_url="unix://var/run/docker.sock")


logger = logging.getLogger("wf_reg_test")


@dataclasses.dataclass
class WorkflowEngine:
    env: Callable[[], Mapping[str, str]]
    command: Callable[[Path], tuple[str, ...]]

    def run(
        self,
        workflow: Path,
        revision: Revision,
        walltime_limit: TimeDelta = TimeDelta(hours=1, minutes=30),
    ) -> Execution:
        output_dir = Path("data") / f"{random.randint(0, 1 << (16 << 2)):016x}"
        output_dir.mkdir()
        time_command = [
            "time",
            f"--output={output_dir!s}/time",
            "--format=%F %S %U %e %x",
            "timeout",
            "--kill-after={:.0f}".format(1.2 * walltime_limit.total_seconds()),
            "{:.0f}".format(walltime_limit.total_seconds()),
            *self.command(workflow),
        ]
        if logger.isEnabledFor(logging.INFO):
            logger.info("Running: %s", shlex.join(time_command))
        proc = subprocess.run(
            time_command,
            check=False,
            capture_output=True,
            cwd=output_dir,
            env=self.env(),
        )
        (output_dir / "stdout").write_bytes(proc.stdout)
        (output_dir / "stderr").write_bytes(proc.stderr)
        sys.stderr.buffer.write(proc.stderr)
        time_output = (
            Path(output_dir / "time").read_text().strip().split("\n")[-1].split(" ")
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
        return Execution(
            datetime=DateTime.now(),
            output=output_dir,
            status_code=int(exit_status),
            wall_time=TimeDelta(seconds=float(wall_time)),
            user_cpu_time=TimeDelta(seconds=float(user_sec)),
            system_cpu_time=TimeDelta(seconds=float(system_sec)),
            max_rss=int(mem_kb) * 1024,
            machine=Machine.current_host(),
            revision=revision,
        )


env_line = re.compile(
    "^(?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*)$", flags=re.MULTILINE
)


def parse_env(env: str) -> Mapping[str, str]:
    return {match.group("var"): match.group("val") for match in env_line.finditer(env)}


bashrc_line = re.compile(
    "^export (?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*)$", flags=re.MULTILINE
)


def parse_bashrc(env: str) -> Mapping[str, str]:
    return {
        match.group("var"): match.group("val") for match in bashrc_line.finditer(env)
    }


def get_nix_flake_env(flake: str) -> Mapping[str, str]:
    return parse_env(
        subprocess.run(
            ["nix", "develop", flake, "--command", "env"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )


def get_spack_env(env: Path) -> Mapping[str, str]:
    # TOOD: check that env is installed first
    return parse_bashrc(
        subprocess.run(
            ["spack", "env", "activate", "--dir", str(env), "--sh"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )


T = TypeVar("T")
def cached_thunk(thunk: Callable[[], T]) -> Callable[[], T]:
    result: Optional[T] = None
    valid = False
    def thunk_wrapper() -> T:
        nonlocal result
        nonlocal valid
        if not valid:
            result = thunk()
            valid = True
        return cast(T, result)
    return thunk_wrapper


engines = {
    "nextflow": WorkflowEngine(
        env=cached_thunk(lambda: {
            **get_spack_env(Path() / "engines" / "nextflow"),
            "HOME": os.environ["HOME"],
        }),
        command=lambda workflow: (
            "nextflow",
            "run",
            str(workflow),
            "-profile",
            "test,singularity",
            "--outdir",
            ".",
        ),
    ),
    "snakemake": WorkflowEngine(
        env=cached_thunk(lambda: {
            **get_spack_env(Path() / "engines" / "snakemake"),
        }),
        command=lambda workflow: (
            "snakemake",
            "--cores",
            "all",
            "--use-conda",
            "--use-singularity",
            str(workflow / "workflow"),
        ),
    ),
}
