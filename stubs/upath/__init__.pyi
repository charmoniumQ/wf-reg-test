import pathlib
import fsspec


class UPath(pathlib.PurePosixPath):
    def __init__(self, url: str) -> None: ...
    fs: fsspec.spec.AbstractFileSystem
    path: str

    def __div__(self, other: str) -> UPath: ...
