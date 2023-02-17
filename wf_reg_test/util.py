from __future__ import annotations
import random
import string
import random
import datetime
import dataclasses
import contextlib
import os
import random
import functools
import subprocess
import tempfile
import pprint
from pathlib import Path
import re
from typing import Callable, Generator, Iterable, TypeVar, Union, cast, Mapping, Any, Optional, Generic, NoReturn
import urllib.parse
import itertools
import shutil
import xml.etree.ElementTree

import azure.identity.aio
import xxhash
import toolz
import tqdm
import upath


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


tmp_root = Path.home() / "tmp"


@contextlib.contextmanager
def create_temp_dir(cleanup: bool = True) -> Generator[Path, None, None]:
    temp_dir = get_unused_path(tmp_root, (random_str(10) for _ in itertools.count()))
    temp_dir.mkdir(parents=True)
    try:
        yield Path(temp_dir)
    finally:
        if cleanup:
            shutil.rmtree(temp_dir)
            os.sync()


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


def groupby_dict(data: Iterable[_T], key_func: Callable[[_T], _V]) -> Mapping[_V, list[_T]]:
    ret: dict[_V, list[_T]] = {}
    for key, group in itertools.groupby(data, key_func):
        ret.setdefault(key, []).extend(group)
    return ret


def merge_dicts(dicts: Iterable[Mapping[_T, _V]]) -> dict[_T, _V]:
    ret: dict[_T, _V] = {}
    for dict in dicts:
        ret.update(dict)
    return ret


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


def raise_(exception: Exception) -> NoReturn:
    raise exception


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


def http_content_length(url: str) -> int:
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req) as response:
        return int(response.getheader("Content-Length"))
        

chunk_size = 1024 * 16


def http_get_with_progress(url: str, path: Path) -> None:
    response = urllib.request.urlopen(url)
    total = http_content_length(url)
    with (
            urllib.request.urlopen(url) as src_fobj,
            path.open("wb") as dst_fobj,
            tqdm.tqdm(total=total, unit="b", unit_scale=True) as bar
    ):
        for i in range(total // chunk_size + 1):
            dst_fobj.write(src_fobj.read(chunk_size))
            bar.update(chunk_size)


def http_download_with_cache(url: str, dest_path: Path, cache_path: Path) -> None:
    cache_dest_path = cache_path / urllib.parse.quote(url, safe="")
    if not cache_dest_path.exists():
        http_get_with_progress(url, cache_dest_path)
    shutil.copy(cache_dest_path, dest_path)


def upath_to_url(url: Optional[Path]) -> str:
    if url is None:
        return "http://github.com/404"
    elif isinstance(url, upath.implementations.cloud.AzurePath):
        return f"https://{url._kwargs['account_name']}.blob.core.windows.net/{url._url.netloc}/{urllib.parse.quote(url.path[1:], safe='')}"
    elif isinstance(url, Path):
        if url.is_absolute():
            return f"file:///{url!s}"
        else:
            return f"file://{url!s}"
    else:
        return str(url)


def file_type(path: Path) -> str:
    return subprocess.run(["file", "--brief", str(path)], capture_output=True, text=True, check=True).stdout.strip()


def mime_type(path: Path) -> str:
    return subprocess.run(["file", "--brief", "--mime-type", str(path)], capture_output=True, text=True, check=True).stdout.strip()


def sanitize_file_type(file_str: str) -> str:
    file_str = re.sub(r"\d\d:\d\d:\d\d:", "time", file_str)
    file_str = re.sub(r"\d{2,}", "##", file_str)
    file_str = re.sub('".*"', '"string"', file_str)
    return file_str
