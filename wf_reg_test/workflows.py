from __future__ import annotations

import shutil
from datetime import datetime as DateTime, timedelta as TimeDelta
import dataclasses
from pathlib import Path
import tarfile
from typing import ClassVar, ContextManager, Optional, Iterable, Mapping
import urllib.parse

from upath import UPath

from .util import non_unique, concat_lists, hash_path, walk_files, curried_getattr, create_temp_dir, get_current_revision
from .executable import Executable, ComputeResources, Machine


# TODO: do this more like three separate tables with joins maybe?
# THat would help immutability


@dataclasses.dataclass
class RegistryHub:
    registries: list[Registry]

    def __str__(self) -> str:
        return f"{self.__class__.__name__} [{', '.join(str(registry) for registry in self.registries)}]"

    @property
    def workflows(self) -> list[Workflow]:
        return concat_lists(registry.workflows for registry in self.registries)

    @property
    def revisions(self) -> list[Revision]:
        return concat_lists(
            workflow.revisions
            for registry in self.registries
            for workflow in registry.workflows
        )

    @property
    def failed_executions(self) -> list[Execution]:
        return [
            execution
            for registry in self.registries
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
            if not execution.successful
        ]

    def check_invariants(self) -> Iterable[UserWarning]:
        for attr in ["url", "display_name"]:
            for reg_i, reg_j, i, j in non_unique(self.registries, curried_getattr(str, attr)):
                yield UserWarning(f"Two registries have the same {attr}: {i} \"{reg_i!s}\", {j} \"{reg_j!s}\"")
        for registry in self.registries:
            yield from registry.check_invariants()


@dataclasses.dataclass
class Registry:
    display_name: str
    url: str
    workflows: list[Workflow]

    def __add__(self, other: Registry) -> Registry:
        if (other.display_name, other.url) != (self.display_name, self.url):
            raise RuntimeError(f"Cannot add different registries: {self} + {other}")
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name}"

    def check_invariants(self) -> Iterable[UserWarning]:
        for attr in ["url", "display_name"]:
            for wf_i, wf_j, i, j in non_unique(self.workflows, curried_getattr(str, attr)):
                yield UserWarning(f"Two workflows have the same {attr}: {i} \"{wf_i!s}\", {j} \"{wf_j!s}\"")
        for wf in self.workflows:
            if wf.registry != self:
                yield UserWarning("Workflow does not point back to self", wf, self)
            yield from wf.check_invariants()


@dataclasses.dataclass
class Workflow:
    """Note that this is termed "computational experiment" when
    writing about this research (see docs/).

    """
    engine: str
    url: str
    display_name: str
    repo_url: str
    revisions: list[Revision]
    registry: Registry = dataclasses.field(compare=False)

    def max_wall_time_estimate(self) -> TimeDelta:
        wall_times_of_successes = [
            execution.resources.wall_time
            for revision in self.revisions
            for execution in revision.executions
            if execution.successful
        ]
        if wall_times_of_successes:
            return max(wall_times_of_successes) * 3 // 2 + TimeDelta(minutes=10)
        else:
            return TimeDelta(minutes=90)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name}"

    def __add__(self, other: Workflow) -> Workflow:
        raise NotImplementedError()
        url_to_revisions = {
            revision.url: revision
            for revision in self.revisions
        }
        for revision in other.revisions:
            if revision.url in url_to_revisions:
                url_to_revisions[revision.url].merge(revision)
            else:
                self.revisions.append(revision)

    def check_invariants(self) -> Iterable[UserWarning]:
        if self not in self.registry.workflows:
            yield UserWarning("Not in own registry")
        for attr in ["url", "display_name", "rev"]:
            for rev_i, rev_j, i, j in non_unique(self.revisions, curried_getattr(str, attr)):
                yield UserWarning(f"Two revisions have the same {attr}: {i} \"{rev_i!s}\", {j} \"{rev_j!s}\"")
        for revision in self.revisions:
            if revision.workflow != self:
                yield UserWarning("Revision does not point back to self", revision, self)
            yield from revision.check_invariants()


@dataclasses.dataclass
class Revision:
    display_name: str
    url: str
    rev: str
    datetime: DateTime
    executions: list[Execution]
    workflow: Optional[Workflow] = dataclasses.field(compare=False)

    def check_invariants(self) -> Iterable[UserWarning]:
        if not self.workflow:
            yield UserWarning("workflow not set")
        elif self not in self.workflow.revisions:
            yield UserWarning("Not in own workflow")
        for execution in self.executions:
            if execution.revision != self:
                yield UserWarning("Execution does not point back to self", execution, self)
            yield from execution.check_invariants()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.display_name} of {self.workflow}"

    def __add__(self, other: Revision) -> Revision:
        raise NotImplementedError
        machine_time_to_executions = {
            (execution.machine, execution.datetime): execution
            for execution in self.executions
        }
        for execution in other.executions:
            if (execution.machine, execution.datetime) in machine_time_to_executions:
                pass
            else:
                self.executions.append(execution)


@dataclasses.dataclass(frozen=True)
class Execution:
    machine: Optional[Machine]
    datetime: DateTime
    outputs: FileBundle
    logs: FileBundle
    condition: Condition
    resources: ComputeResources
    status_code: int
    revision: Optional[Revision] = dataclasses.field(compare=False)
    wf_reg_test_revision: str = dataclasses.field(default_factory=get_current_revision)

    def with_pointers(self, machine: Machine, revision: Revision) -> Execution:
        return Execution(
            machine=machine,
            revision=revision,
            datetime=self.datetime,
            outputs=self.outputs,
            logs=self.logs,
            condition=self.condition,
            resources=self.resources,
            status_code=self.status_code,
        )

    @property
    def successful(self) -> bool:
        return self.status_code == 0

    def check_invariants(self) -> Iterable[UserWarning]:
        if self.machine is None:
            yield UserWarning("machine not set")
        if self.revision is None:
            yield UserWarning("revision not set")
        elif self not in self.revision.executions:
            yield UserWarning("Not in own revision")
        yield from self.outputs.check_invariants()
        yield from self.logs.check_invariants()
        yield from self.resources.check_invariants()
        yield from self.condition.check_invariants()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} of {self.revision}"


@dataclasses.dataclass(frozen=True)
class RandomStream:
    seed: int
    method: str = "stdlib"


@dataclasses.dataclass(frozen=True)
class Condition:
    single_core: bool
    aslr: bool
    faketime: Optional[DateTime]
    dev_random: Optional[RandomStream]
    rr_record: bool
    rr_replay: Optional[object]

    def __str__(self) -> str:
        return f"single_core={self.single_core},aslr={self.aslr},faketime_set={bool(self.faketime)},dev_random_set={bool(self.dev_random)},rr_record={self.rr_record},rr_replay_set={bool(self.rr_replay)}"

    def check_invariants(self) -> Iterable[UserWarning]:
        yield from []

    NO_CONTROLS: ClassVar[Condition]
    EASY_CONTROLS: ClassVar[Condition]
    HARD_CONTROLS: ClassVar[Condition]

Condition.NO_CONTROLS = Condition(
        single_core=False,
        aslr=False,
        faketime=None,
        dev_random=None,
        rr_record=False,
        rr_replay=None,
    )

Condition.EASY_CONTROLS = Condition(
        single_core=False,
        aslr=True,
        faketime=DateTime(2020, 1, 1),
        dev_random=RandomStream(seed=0, method="stdlib"),
        rr_record=False,
        rr_replay=None,
    )

Condition.HARD_CONTROLS = Condition(
        single_core=True,
        aslr=True,
        faketime=DateTime(2022, 1, 1),
        dev_random=RandomStream(seed=0, method="stdlib"),
        rr_record=False,
        rr_replay=None,
    )


@dataclasses.dataclass(frozen=True)
class FileBundle:
    contents: Mapping[Path, File]
    # archive: upath.UPath

    @staticmethod
    def create_on_disk(root: Path) -> FileBundle:
        contents: dict[Path, File] = {}
        for path in walk_files(root):
            if (root / path).is_file() and not (root / path).is_symlink():
                contents[path] = File.create(root / path, url=f"file://{path.resolve()!s}")
        return FileBundle(contents)

    @staticmethod
    def create_in_storage(root: Path, remote_archive: UPath) -> FileBundle:
        if not remote_archive.name.endswith(".tar.xz"):
            raise ValueError("Must pass a .tar.xz")
        with create_temp_dir(cleanup=False) as temp_dir:
            tarball = tarfile.open(temp_dir / remote_archive.name, "w:xz")
            contents: dict[Path, File] = {}
            for path in walk_files(root):
                if (root / path).is_file() and not (root / path).is_symlink():
                    contents[path] = File.create(root / path, url=f"tar://{path!s}::{remote_archive!s}")
                    tarball.add(root / path, path)
            tarball.close()
            if isinstance(remote_archive, UPath):
                remote_archive_path = remote_archive.path
                # Note that Azure blob storage Python SDK already calls urlquote, so by default, these things get quoted twice!
                # So we should unquote them here.
                if remote_archive.fs.__class__.__name__ == "AzureBlobFileSystem":
                    remote_archive_path = urllib.parse.unquote(remote_archive_path)
                remote_archive.fs.put_file(tarball.name, remote_archive._url.netloc + remote_archive_path)
            else:
                remote_archive.parent.mkdir(exist_ok=True, parents=True)
                shutil.move(tarball.name, remote_archive)
        return FileBundle(
            contents,
            # remote_archive,
        )

    @property
    def archive(self) -> str:
        try:
            path, file = next(iter(self.contents.items()))
        except StopIteration:
            return ""
        url = file.contents_url
        if url is None:
            return ""
        else:
            return (
                url
                # Looking for path to whole archive, not just this file
                .replace(str(path), "")
                # If this path was a path within a tar://, this gets us the URL of the tar.
                .replace("tar://::", "")
                # If this was an Azure, this gives us an HTTP url.
                .replace("abfs://", "https://wfregtest.blob.core.windows.net/")
            )

    @property
    def empty(self) -> bool:
        return not bool(self.contents)

    def total_size(self) -> int:
        return sum(file.size for file in self.contents.values())

    def check_invariants(self) -> Iterable[UserWarning]:
        for file in self.contents.values():
            yield from file.check_invariants()


@dataclasses.dataclass(frozen=True)
class File:
    hash_algo: str
    hash_bits: int
    hash_val: int
    size: int
    contents_url: Optional[str] = dataclasses.field(compare=False, hash=False)

    @staticmethod
    def create(path: Path, url: Optional[str] = None) -> File:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"{path} is not a regular file")
        return File(
            hash_algo="xxhash",
            hash_bits=64,
            hash_val=hash_path(path, size=64),
            size=path.stat().st_size,
            contents_url=f"file://{path.resolve()!s}" if url is None else url,
        )

    def check_invariants(self) -> Iterable[UserWarning]:
        if not (0 <= self.hash_val < (1 << self.hash_bits)):
            yield UserWarning("hash is bigger than hash_bits", self, self.hash_val, self.hash_bits)
        if self.size < 0:
            yield UserWarning("File cannot have negative size")

    def read_bytes(self) -> Optional[bytes]:
        """Return the bytes of this file, if we have them, else None."""
        # I guess we never have them :/
        return None
