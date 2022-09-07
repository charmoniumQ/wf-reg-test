import contextlib
import tempfile
from pathlib import Path
from typing import Generator, Union, Iterable
import xxhash

@contextlib.contextmanager
def create_temp_dir() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def hash_path(path: Union[Path, str, bytes]) -> bytes:
    hasher = xxhash.xxh128()
    block_size = 1 << 14
    with open(path, "rb") as file:
        while True:
            buffer = file.read(block_size)
            if not buffer:
                break
            hasher.update(buffer)
    return bytes(hasher.hexdigest(), encoding="ascii")


def walk(path: Path) -> Iterable[Path]:
    yield path
    if path.is_dir():
        for subpath in path.iterdir():
            yield from walk(subpath)
