import dataclasses
import pathlib
from typing import Mapping

from .workflows import Execution


@dataclasses.dataclass
class Error:
    file: pathlib.Path
    error_type: str
    command: list[str]
    rest: Mapping[str, str]


#def classify_errors(execution: Execution) -> None:
