import random
import contextlib
import tempfile
from pathlib import Path
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


def walk(
    mapper: Callable[[Path, list[_T]], _T],
    path: Path,
    ignore_preds: tuple[Callable[[str], bool], ...] = (_ignore_vcs,),
) -> _T:
    from gitignore_parser import parse_gitignore  # type: ignore
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
    children = [xml_to_dict(child) for child in elem]
    return (
        elem.tag,
        {
            **({"text": text} if text else {}),
            **({"tail": tail} if tail else {}),
            **elem.attrib,
        },
        *((children,) if children else ()),
    )
