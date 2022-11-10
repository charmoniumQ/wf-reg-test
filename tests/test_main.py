import operator
from pathlib import Path

import yaml
import pytest
import wf_reg_test.util
import wf_reg_test.repos
import wf_reg_test.registries
from wf_reg_test.workflows import RegistryHub
from wf_reg_test.workflows import FileBundle, File
from wf_reg_test.parallel_execute import parallel_map, ResourcePool
from wf_reg_test.executable import Machine, ComputeResources, parse_time_file, time, Executable
from charmonium.freeze import summarize_diff

@pytest.fixture
def hub() -> RegistryHub:
    return RegistryHub([
        wf_reg_test.registries.snakemake_registry(),
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
    with time(Executable(["ls", "-ahlt"])) as (executable, time_file):
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


def test_parallel_map() -> None:
    def worker(resource_pool: ResourcePool[int], arg0: int, arg1: int) -> tuple[int, int]:
        worker_id = resource_pool.get()
        ret = arg0 + arg1
        resource_pool.put(worker_id)
        return (worker_id, ret)
    args_list = [(i, i**2) for i in range(40)]
    max_workers = 4
    results = parallel_map(worker, args_list, max_workers=max_workers)
    for i, (worker_id, ret) in enumerate(results):
        assert ret == i + i**2

def test_file_bundle() -> None:
    with wf_reg_test.util.create_temp_dir() as temp_dir:
        (temp_dir / "foo").write_text("hi")
        (temp_dir / "blah").mkdir()
        (temp_dir / "blah/foo").write_text("hello")
        (temp_dir / "bar").symlink_to("foo")
        (temp_dir / "baz").hardlink_to(temp_dir / "foo")
        common_args = dict(
            hash_algo='xxhash',
            hash_bits=64,
            contents_url=None,
        )
        actual = FileBundle.create(temp_dir)
    expected = FileBundle(contents={
        Path('foo'): File(hash_val=16899831174130972922, size=2, **common_args),
        Path('baz'): File(hash_val=16899831174130972922, size=2, **common_args),
        Path('blah/foo'): File(hash_val=2794345569481354659, size=5, **common_args),
    })
    assert actual == expected, summarize_diff(actual, expected)


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
    assert not wf_reg_test.util.persistent_random_path().exists()
