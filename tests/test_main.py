import math
import time
from datetime import datetime as DateTime
from pathlib import Path

import yaml
import pytest
import wf_reg_test.util
import wf_reg_test.repos
import wf_reg_test.registries
from wf_reg_test.workflows import RegistryHub
from wf_reg_test.workflows import FileBundle, File
from wf_reg_test.parallel_execute import parallel_map_with_id, ResourcePool
from wf_reg_test.executable import Machine, ComputeResources, parse_time_file, time as time_ex, Executable
from charmonium.freeze import summarize_diff

@pytest.fixture
def hub() -> RegistryHub:
    return RegistryHub([
        wf_reg_test.registries.snakemake_registry(5),
        wf_reg_test.registries.nf_core_registry(5),
    ])


def test_hub(hub: RegistryHub) -> None:
    # test that hub() works.
    pass


@pytest.fixture
def hub_with_repos(hub: RegistryHub) -> RegistryHub:
    count = 0
    for registry in hub.registries:
        for workflow in registry.workflows:
            repo = wf_reg_test.repos.get_repo(workflow.repo_url)
            revisions = list(repo.get_revisions())
            if revisions:
                count += 1
            for revision in revisions:
                revision.workflow = workflow
                workflow.revisions.append(revision)
                count += 1
            if count > 1:
                break
    return hub


def test_hub_with_repos(hub_with_repos: RegistryHub) -> None:
    pass


@pytest.fixture
def machine() -> Machine:
    return Machine.current_machine()


def test_machine(machine: Machine) -> None:
    pass


@pytest.fixture
def compute_resources() -> ComputeResources:
    with time_ex(Executable(["ls", "-ahlt"])) as (executable, time_file):
        executable.local_execute()
        return parse_time_file(time_file)


def test_time(compute_resources: ComputeResources) -> None:
    pass


def test_serialize(compute_resources: ComputeResources, machine: Machine) -> None:
    compute_resources2 = yaml.load(yaml.dump(compute_resources), Loader=yaml.Loader)
    assert compute_resources == compute_resources2
    machine2 = yaml.load(yaml.dump(machine), Loader=yaml.Loader)
    assert machine2 == machine
    assert type(machine2) is type(machine)

wait = 0.2
def worker(arg0: int, arg1: int, core_pool: ResourcePool[int], wait: float = wait) -> tuple[int, int]:
    ret = arg0 + arg1
    time.sleep(wait)
    return ret

def test_parallel_map() -> None:
    total_items = 20
    args_list = [(i, i**2) for i in range(total_items)]
    start = DateTime.now()
    results = list(parallel_map_with_id(worker, args_list, oversubscribe=False, ))
    elapsed = (DateTime.now() - start).total_seconds()
    assert len(results) == total_items
    for (arg0, arg1, ret) in results:
        assert ret == arg0 + arg1

def test_file_bundle() -> None:
    with wf_reg_test.util.create_temp_dir() as temp_dir:
        (temp_dir / "foo").write_text("hi")
        (temp_dir / "blah").mkdir()
        (temp_dir / "blah/foo").write_text("hello")
        (temp_dir / "bar").symlink_to("foo")
        (temp_dir / "baz").hardlink_to(temp_dir / "foo")
        file_bundle_loc = temp_dir / "test.tar.xz"
        actual = FileBundle.from_path(temp_dir, file_bundle_loc)
        kwargs = dict(hash_algo='xxhash', hash_bits=64, file_type="ASCII text", mime_type="text/plain")
        expected = {
            Path('foo'): File(hash_val=16899831174130972922, size=2, url=None, **kwargs),
            Path('baz'): File(hash_val=16899831174130972922, size=2, url=None, **kwargs),
            Path('blah/foo'): File(hash_val=2794345569481354659, size=5, url=None, **kwargs),
        }
        assert actual.files == expected


def test_walk_files() -> None:
    with wf_reg_test.util.create_temp_dir() as temp_dir:
        (temp_dir / "foo").write_text("hi")
        (temp_dir / "blah").mkdir()
        (temp_dir / "blah/foo").write_text("hello")
        (temp_dir / "bar").symlink_to("foo")
        (temp_dir / "baz").hardlink_to(temp_dir / "foo")
        assert set(wf_reg_test.util.walk_files(temp_dir)) == {
            Path("foo"),
            Path("blah/foo"),
            Path("bar"),
            Path("baz"),
        }


def test_random_path() -> None:
    with wf_reg_test.util.create_temp_dir() as tmp_dir:
        assert tmp_dir.exists()
    assert not tmp_dir.exists()
    assert wf_reg_test.util.random_str(15) != wf_reg_test.util.random_str(15)
    assert not wf_reg_test.util.get_unused_path(Path(), suffixes=map(str, range(10))).exists()


if __name__ == "__main__":
    test_parallel_map()
