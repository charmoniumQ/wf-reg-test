from __future__ import annotations

import shutil
from datetime import datetime as DateTime, timedelta as TimeDelta
import dataclasses
import pathlib
import shlex
import subprocess
from typing import ClassVar, ContextManager, Optional, Iterable, Mapping
import urllib.parse

import upath

from .util import non_unique, concat_lists, hash_path, walk_files, curried_getattr, create_temp_dir, get_current_revision, file_type, mime_type, http_download_with_cache, upath_to_url
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
    def executions(self) -> list[Execution]:
        return concat_lists([
            revision.executions
            for registry in self.registries
            for workflow in registry.workflows
            for revision in workflow.revisions
        ])

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
            # if wf.registry != self:
            #     yield UserWarning("Workflow does not point back to self", wf, self)
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
    # I changed this because the serialization of the workflow was too large when it included an up-pointer to the registry and the entire hub.
    #registry: Registry = dataclasses.field(compare=False)

    def max_wall_time_estimate(self) -> TimeDelta:
        # wall_times_of_successes = [
        #     execution.resources.wall_time
        #     for revision in self.revisions
        #     for execution in revision.executions
        #     if execution.successful
        # ]
        # if wall_times_of_successes:
        #     return max(wall_times_of_successes) * 3 + TimeDelta(minutes=30)
        # else:
        return TimeDelta(minutes=180)

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
        # if self not in self.registry.workflows:
        #     yield UserWarning("Not in own registry")
        # rev can be the same if nothing changes between revisions
        # E.g., https://github.com/franciscozorrilla/metaGEM v1.0.1 and v1.0.0 are both cc3d75a9
        for attr in ["url", "display_name"]:
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
class WorkflowError:
    kind: str


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
    workflow_error: Optional[WorkflowError] = None

    def with_attrs(
            self,
            machine: Optional[Machine] = None,
            revision: Optional[Revision] = None,
            workflow_error: Optional[WorkflowError] = None
    ) -> Execution:
        return Execution(
            machine=machine if machine is not None else self.machine,
            revision=revision if revision is not None else self.revision,
            datetime=self.datetime,
            outputs=self.outputs,
            logs=self.logs,
            condition=self.condition,
            resources=self.resources,
            status_code=self.status_code,
            workflow_error=workflow_error if workflow_error is not None else self.workflow_error,
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


@dataclasses.dataclass#(frozen=True)
class FileBundle:
    archive: File
    files: Mapping[pathlib.Path, File]

    @staticmethod
    def from_path(data_path: pathlib.Path, remote_archive: upath.UPath) -> FileBundle:
        contents: dict[pathlib.Path, File] = {}
        for path in walk_files(data_path):
            if (data_path / path).is_file() and not (data_path / path).is_symlink():
                contents[path] = File.from_path(data_path / path)
        with create_temp_dir() as temp_dir:
            local_archive = temp_dir / remote_archive.name
            (temp_dir / "files").write_text(
                "\n".join(
                    str(member.relative_to(data_path))
                    for member in data_path.iterdir()
                ) + "\n"
            )
            cmd = ["tar", "--create", "--xz", f"--file={local_archive}", f"--files-from={temp_dir / 'files'}"]
            proc = subprocess.run(
                cmd,
                cwd=data_path,
                check=True,
                capture_output=True,
                text=True,
            )
            with local_archive.open("rb") as src_fileobj, remote_archive.open("wb") as dst_fileobj:
                shutil.copyfileobj(src_fileobj, dst_fileobj)
            return FileBundle(File.from_path(local_archive, remote_archive), contents)

    @staticmethod
    def blank() -> FileBundle:
        return FileBundle(File.blank(), {})

    @staticmethod
    def from_file_archive(remote_archive: File, cache_path: pathlib.Path) -> FileBundle:
        with create_temp_dir() as temp_dir:
            local_archive = temp_dir / "test.tar.xz"
            http_download_with_cache(upath_to_url(remote_archive.url), local_archive, cache_path)
            data_path = temp_dir / "data"
            if data_path.exists():
                shutil.rmtree(data_path)
            data_path.mkdir()
            subprocess.run(
                ["tar", "--extract", f"--file={local_archive}", f"--directory={data_path}"],
                check=True,
                capture_output=True,
            )
            contents: dict[pathlib.Path, File] = {}
            for path in walk_files(data_path):
                if (data_path / path).is_file() and not (data_path / path).is_symlink():
                    contents[path] = File.from_path(data_path / path)
        return FileBundle(remote_archive, contents)

    def check_invariants(self) -> Iterable[UserWarning]:
        ## This might involve fetching a lazy_object_proxy.
        ## Not worth it!
        # for file in self.files.values():
        #     yield from file.check_invariants()
        yield from []

    @property
    def empty(self) -> bool:
        return False
        # return not bool(self.files)

    @property
    def size(self) -> int:
        return self.archive.size
        # return sum(file.size for file in self.files.values())


@dataclasses.dataclass(frozen=True)
class File:
    hash_algo: str
    hash_bits: int
    hash_val: int
    size: int
    file_type: str
    mime_type: str
    url: Optional[pathlib.Path]

    @staticmethod
    def from_path(path: pathlib.Path, url: Optional[upath.UPath] = None) -> File:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"{path} is not a regular file")
        return File(
            hash_algo="xxhash",
            hash_bits=64,
            hash_val=hash_path(path, size=64),
            size=path.stat().st_size,
            file_type=file_type(path),
            mime_type=mime_type(path),
            url=path if url is None else url,
        )

    @staticmethod
    def blank() -> File:
        return File(
            hash_algo="xxhash",
            hash_bits=64,
            hash_val=hash_path(pathlib.Path("/dev/null", size=64)),
            size=0,
            file_type="empty",
            mime_type="empty",
            url=None,
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, File):
            if self.hash_algo == other.hash_algo and self.hash_bits == other.hash_bits:
                return self.hash_val == other.hash_val
            else:
                raise ValueError("Files have different hash algorithms. No determination could be made.")
        else:
            return False

    def check_invariants(self) -> Iterable[UserWarning]:
        if not (0 <= self.hash_val < (1 << self.hash_bits)):
            yield UserWarning("hash is bigger than hash_bits", self, self.hash_val, self.hash_bits)
        if self.size < 0:
            yield UserWarning("File cannot have negative size")

    @property
    def empty(self) -> bool:
        return self.size == 0

    def read_bytes(self) -> Optional[bytes]:
        """Return the bytes of this file, if we have them, else None."""
        # I guess we never have them :/
        return None
