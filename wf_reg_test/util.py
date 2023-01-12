from __future__ import annotations
import random
import string
from pathlib import Path
import random
import datetime
import dataclasses
import contextlib
import random
import functools
import subprocess
import tempfile
from pathlib import Path
import pprint
from typing import Callable, Generator, Iterable, TypeVar, Union, cast, Mapping, Any, Optional, Generic
import urllib.parse
import itertools
import shutil
import xml.etree.ElementTree

import azure.identity.aio
import xxhash
import toolz


_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")


def curried_getattr(ty: type[_V], attr: str) -> Callable[[_T], _V]:
    def inner(obj: _T) -> _V:
        return cast(_V, getattr(obj, attr))
    return inner


@contextlib.contextmanager
def create_temp_file(cleanup: bool = True) -> Generator[Path, None, None]:
    with create_temp_dir(cleanup) as temp_dir:
        yield Path(temp_dir / "file")


@contextlib.contextmanager
def create_temp_dir(cleanup: bool = True) -> Generator[Path, None, None]:
    temp_dir = Path(tempfile.mkdtemp())
    yield Path(temp_dir)
    if cleanup:
        shutil.rmtree(temp_dir)


def random_str(
        length: int,
        alphabet: str = string.ascii_lowercase + string.digits,
) -> str:
    return "".join(random.choice(alphabet) for _ in range(length))


def get_unused_path(prefix: Path, suffixes: Iterable[str]) -> Path:
    for suffix in suffixes:
        candidate = prefix / suffix
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"None of {suffixes} are unused in {prefix}")


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


def non_unique(
    data: Iterable[_T],
    key: Callable[[_T], Any] = toolz.identity,
) -> Iterable[tuple[_T, _T, int, int]]:
    for ix, x in enumerate(data):
        for iy, y in enumerate(data):
            if key(x) == key(y) and ix != iy:
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


def fs_escape(string: str) -> str:
    return urllib.parse.quote(string.replace(" ", "-").replace("_", "-"), safe="")


class ThunkObject:
    def __init__(self, ty: type[_T], thunk: Callable[[], _T]) -> None:
        self._ty = ty
        self._thunk = thunk
        self._value: Optional[_T]
        self._value = None

    def __getstate__(self) -> Any:
        return self._thunk

    def __setstate__(self, thunk: Callable[[], _T]) -> None:
        self._thunk = thunk
        self._value = None

    def _reify(self, ty: type[_T]) -> _T:
        if self._value is None:
            self._value = self._thunk()
            assert self._value is not None
            for attr in dir(self._value):
                if attr not in ["__class__", "__getstate__", "__setstate__"]:
                    setattr(self, attr, getattr(self._value, attr))
        return self._value

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._reify(self._ty), attr)


# azure.identity.aio.DefaultIdentityCredential is not picklable.
# So, instead we create a surrogate object that initializes a new DefaultIdentityCredential when it gets restored from Pickle.
# __init__ implicitly calls azure.identity.aio.ManagedIdentityCredential.__init__
# __setstate__ also calls azure.identity.aio.ManagedIdentityCredential.__init__
# __getstate__ is dummy that returns something Truthy.
class AzureCredential(azure.identity.aio.DefaultAzureCredential):
    def __getstate__(self) -> str:
        return "hi" # must be Truthy
    def __setstate__(self, state: Any) -> None:
        azure.identity.aio.DefaultAzureCredential.__init__(self)


@functools.cache
def get_current_revision() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=Path(__file__).resolve().parent,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def drop_keys(dct: Mapping[_T, _V], drop_keys: set[_T]) -> Mapping[_T, _V]:
    return {
        key: val
        for key, val in dct.items()
        if key not in drop_keys
    }


def map_keys(mapper: Callable[[_T], _U], dct: Mapping[_T, _V]) -> Mapping[_U, _V]:
    return {
        mapper(key): val
        for key, val in dct.items()
    }


def chunk(it: Iterable[_T], chunk_size: int) -> Iterable[list[_T]]:
    ity = iter(it)
    while True:
        ret = []
        for _ in range(chunk_size):
            try:
                ret.append(next(ity))
            except StopIteration:
                yield ret
                break
        yield ret
