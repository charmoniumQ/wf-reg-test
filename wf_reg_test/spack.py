import functools
from pathlib import Path
import re
import subprocess
import os
from typing import Mapping

from .executable import Executable


bashrc_line = re.compile(
    "^export (?P<var>[a-zA-Z_][a-zA-Z_0-9]*)=(?P<val>.*);?$", flags=re.MULTILINE
)


def parse_bashrc(env: str) -> Mapping[str, str]:
    return {
        match.group("var"): match.group("val")
        for match in bashrc_line.finditer(env)
    }


@functools.cache
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


@functools.cache
def get_spack_executable(env: Path, executable: str, args: list[str]) -> Executable:
    env_vars = get_spack_env(env)
    paths = env_vars.get("PATH", os.environ.get("PATH", ""))
    for path in paths.split(":"):
        if path:
            for path_to_executable in Path(path).iterdir():
                if path_to_executable.name == executable:
                    break
    else:
        raise ValueError(f"{executable} is not on any of {paths}")
    return Executable(
        command=[str(path_to_executable), *args],
        env=env_vars,
    )
