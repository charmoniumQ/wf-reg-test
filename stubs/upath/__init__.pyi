import pathlib
from typing import Any
import urllib.parse

import fsspec


class UPath(pathlib.PurePosixPath):
    def __init__(self, url: str, **extra: Any) -> None: ...
    fs: fsspec.spec.AbstractFileSystem
    path: str
    _url: urllib.parse.ParseResult

    def __div__(self, other: str) -> UPath: ...
