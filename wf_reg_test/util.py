from __future__ import annotations
import random
import dataclasses
import contextlib
import tempfile
from pathlib import Path
import pprint
from typing import Callable, Generator, Iterable, TypeVar, Union, cast, Mapping, Any, Optional
import itertools
import xml.etree.ElementTree

import xxhash


@contextlib.contextmanager
def create_temp_dir() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


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


def walk_files(path: Path) -> Iterable[Path]:
    yield from _walk_files(path, path)


def _walk_files(
    path: Path,
    root_path: Path,
) -> Iterable[Path]:
    if path.is_dir():
        for subpath in path.iterdir():
            yield from _walk_files(subpath, root_path)
    else:
        yield path.relative_to(root_path)


def map_dirs(
    mapper: Callable[[Path, list[_T]], _T],
    path: Path,
) -> _T:
    if path.is_dir():
        children = [
            map_dirs(mapper, subpath)
            for subpath in path.iterdir()
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
    if not isinstance(data, typ):
        raise TypeError(f"Expected type {typ} for {data}")
    # mypy considers this a redundant cast.
    # Apparently they're pretty smart.
    # return cast(_T, data)
    return data


def concat_lists(lists: Iterable[list[_T]]) -> list[_T]:
    ret: list[_T] = []
    for list_ in lists:
        ret.extend(list_)
    return ret


def cached_thunk(thunk: Callable[[], _T]) -> Callable[[], _T]:
    result: Optional[_T] = None
    valid = False
    def thunk_wrapper() -> _T:
        nonlocal result
        nonlocal valid
        if not valid:
            result = thunk()
            valid = True
        return cast(_T, result)
    return thunk_wrapper


def functional_shuffle(lst: list[_T], seed: int = 0) -> list[_T]:
    rand = random.Random(seed)
    lst = lst[:]
    rand.shuffle(lst)
    return lst


def xml_to_dict(elem: xml.etree.ElementTree.Element) -> Any:
    text = elem.text.strip() if elem.text else ""
    tail = elem.tail.strip() if elem.tail else ""
    children = tuple(xml_to_dict(child) for child in elem)
    return (
        elem.tag,
        frozenset(elem.attrib.items()),
        *((text,) if text else ()),
        *((children,) if children else ()),
        *((tail,) if tail else ()),
    )


persistent_data = Path(".persistent")
persistent_data.mkdir(exist_ok=True)
def persistent_random_path() -> Path:
    digits = 10
    return persistent_data / "{:0{digits}x}".format(random.randint(16**digits))
