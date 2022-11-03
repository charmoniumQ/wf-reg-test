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
import charmonium.freeze


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
    children = tuple(xml_to_dict(child) for child in elem)
    return (
        elem.tag,
        frozenset(elem.attrib.items()),
        *((text,) if text else ()),
        *((children,) if children else ()),
        *((tail,) if tail else ()),
    )


def common_prefix(it0: Iterable[_T], it1: Iterable[_T]) -> list[_T]:
    ret = []
    for elem0, elem1 in zip(it0, it1):
        if elem0 == elem1:
            ret.append(elem0)
        else:
            break
    return ret


@dataclasses.dataclass
class ObjectLocation:
    labels: tuple[str, ...]
    objects: tuple[object, ...]

    def append(self, label: str, obj: object) -> ObjectLocation:
        return self.__class__((*self.labels, label), (*self.objects, obj))

    @property
    def tail(self):
        return self.objects[-1]

    @tail.setter
    def set_tail(self, obj: object) -> ObjectLocation:
        self.objects = (*self.objects[:-1], obj)


def summarize_diff(obj0: Any, obj1: Any) -> str:
    differences = list(iterate_diffs(
        ObjectLocation(
            labels=("obj0",),
            objects=(charmonium.freeze.freeze(obj0),),
        ),
        ObjectLocation(
            labels=("obj1",),
            objects=(charmonium.freeze.freeze(obj1),),
        ),
    ))
    if differences:
        longest_common = differences[0][0].labels[1:]
        for difference in differences:
            longest_common = common_prefix(longest_common, difference[0].labels[1:])
            longest_common = common_prefix(longest_common, difference[1].labels[1:])
        ret = []
        ret.append("obj0_sub = obj0{}".format("".join(longest_common)))
        ret.append(pprint.pformat(differences[0][0].objects[len(longest_common) + 1], width=300))
        ret.append("obj1_sub = obj1{}".format("".join(longest_common)))
        ret.append(pprint.pformat(differences[0][1].objects[len(longest_common) + 1], width=300))
        for difference in differences:
            path_from_sub = "".join(difference[0].labels[len(longest_common) + 1:])
            ret.append("obj0_sub{} == {}".format(path_from_sub, difference[0].objects[-1]))
            ret.append(pprint.pformat(difference[0].objects[len(longest_common) + 3]))
            ret.append("obj1_sub{} == {}".format(path_from_sub, difference[1].objects[-1]))
            ret.append(pprint.pformat(difference[1].objects[len(longest_common) + 3]))
        return "\n".join(ret)
    else:
        return "no differences"


def iterate_diffs(
        obj0: ObjectLocation,
        obj1: ObjectLocation,
) -> Iterable[tuple[ObjectLocation, ObjectLocation]]:
    if obj0.tail.__class__ != obj1.tail.__class__:
        yield (
            obj0.append(".__class__", obj0.tail.__class__.__name__),
            obj1.append(".__class__", obj1.tail.__class__.__name__),
        )
    elif isinstance(obj0.tail, tuple) and isinstance(obj1.tail, tuple):
        if len(obj0.tail) != len(obj1.tail):
            yield (
                obj0.append(".__len__()", len(obj0.tail)),
                obj1.append(".__len__()", len(obj1.tail)),
            )
        for idx in range(min(len(obj0.tail), len(obj1.tail))):
            yield from iterate_diffs(
                obj0.append(f"[{idx}]", obj0.tail[idx]),
                obj1.append(f"[{idx}]", obj1.tail[idx]),
            )
    elif isinstance(obj0, frozenset) and isinstance(obj1, frozenset):
        if all(isinstance(elem, tuple) and len(elem) == 2 for elem in obj0) and all(isinstance(elem, tuple) and len(elem) == 2 for elem in obj1):
            # treat frozenset as a dict:
            obj0.tail = dict(obj0.tail)
            obj1.tail = dict(obj1.tail)
            for elem in obj0.tail.keys() - obj1.tail.keys():
                yield (
                    obj0.append(".keys().has()", elem),
                    obj1.append(".keys().has()", "no such elem"),
                )
            for elem in obj1.tail.keys() - obj0.tail.keys():
                yield (
                    obj0.append(".keys().has()", "no such elem"),
                    obj1.append(".keys().has()", elem),
                )
            for key in obj0.keys() & obj1.keys():
                yield from iterate_diffs(
                    obj0.append(f"[{key}]", obj0.tail[key]),
                    obj1.append(f"[{key}]", obj1.tail[key]),
                )
        else:
            # treat frozenset as a pure frozenset:
            for elem in obj0 - obj1:
                yield (
                    obj0.append(".has()", elem),
                    obj1.append(".has()", "no such elem"),
                )
            for elem in obj1 - obj0:
                yield (
                    obj0.append(".has()", "no such elem"),
                    obj1.append(".has()", elem),
                )
    else:
        if obj0.tail != obj1.tail:
            yield (obj0, obj1)
