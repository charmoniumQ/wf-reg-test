import pathlib
from typing import Any, Mapping
import urllib.parse

import fsspec

from . import implementations as implementations


class UPath(pathlib.Path):
    fs: fsspec.spec.AbstractFileSystem
    path: str
    _url: urllib.parse.ParseResult
    _kwargs: Mapping[str, Any]

    def __init__(self, url: str, **extra: Any) -> None: ...

    def __div__(self, other: str) -> UPath: ...

    def iterdir(self) -> Iterable[UPath]: ...

    def glob(self, pattern: str) -> Iterable[UPath]: ...
