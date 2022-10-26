import contextlib
import tempfile
from pathlib import Path
from typing import Callable, Generator, Iterable, TypeVar, Union, cast, Mapping, Any
import itertools

import xxhash
from gitignore_parser import parse_gitignore  # type: ignore


@contextlib.contextmanager
def create_temp_dir() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def hash_path(path: Union[Path, str, bytes], size: int = 128) -> int:
    hasher = {
        128: xxhash.xxh128(),
        64: xxhash.xxh64(),
        32: xxhash.xxh32(),
    }[size]
    block_size = 1 << 14
    with open(path, "rb") as file:
        while True:
            buffer = file.read(block_size)
            if not buffer:
                break
            hasher.update(buffer)
    return hasher.intdigest()


def hash_bytes(buffer: bytes, size: int = 128) -> int:
    hasher = {
        128: xxhash.xxh128(),
        64: xxhash.xxh64(),
        32: xxhash.xxh32(),
    }[size]
    hasher.update(buffer)
    return hasher.intdigest()


def _ignore_vcs(path: str) -> bool:
    return path == ".git" or path.endswith("/.git")


_T = TypeVar("_T")
_V = TypeVar("_V")


def walk(
    mapper: Callable[[Path, list[_T]], _T],
    path: Path,
    ignore_preds: tuple[Callable[[str], bool], ...] = (_ignore_vcs,),
) -> _T:
    if path.is_dir():
        ignore_file = path / ".gitignore"
        if ignore_file.exists():
            ignore_preds = (
                *ignore_preds,
                cast(Callable[[str], bool], parse_gitignore(ignore_file)),
            )
        children = [
            walk(mapper, subpath, ignore_preds)
            for subpath in path.iterdir()
            if not any(ignore_pred(str(subpath)) for ignore_pred in ignore_preds)
        ]
    else:
        children = []
    return mapper(path, children)


def sorted_and_dropped(inp: Iterable[tuple[_T, _V]], reverse: bool = False) -> list[_V]:
    return [y for x, y in sorted(inp, reverse=reverse)]


def groupby_dict(data: Iterable[_T], key: Callable[[_T], _V]) -> Mapping[_V, list[_T]]:
    return {
        key: list(group)
        for key, group in itertools.groupby(data, key)
    }


def non_unique(data: Iterable[_T]) -> Iterable[tuple[_T, _T, int, int]]:
    for ix, x in enumerate(data):
        for iy, y in enumerate(data):
            if x == y and ix != iy:
                yield (x, y, ix, iy)


def expect_type(typ: type[_T], data: Any) -> _T:
    if not isinstance(type, data):
        raise TypeError(f"Expected type {typ} for {data}")
    return cast(_T, data)
