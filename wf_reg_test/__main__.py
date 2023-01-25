import collections
import logging
import warnings
import itertools
import multiprocessing
import random
import re
import shutil
import sys
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from pathlib import Path
from typing import cast, Optional, Callable, Any

import click
import charmonium.time_block as ch_time_block
import yaml
import tqdm
import upath

from .serialization import serialize, deserialize
from .report import report_html
from .repos import get_repo
from .workflows import RegistryHub, Revision, Workflow, Condition, Execution, File
from .util import groupby_dict, functional_shuffle, expect_type, curried_getattr, AzureCredential, http_content_length
from .executable import Machine
from .parallel_execute import parallel_execute

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ch_time_block.disable_stderr()

for name in ["paramiko", "azure"]:
    logging.getLogger(name).setLevel(logging.WARNING)
    logging.getLogger(name).propagate = False


serialize = ch_time_block.decor()(serialize)
deserialize = ch_time_block.decor()(deserialize)


@ch_time_block.decor()
def ensure_revisions(
        hub: RegistryHub, only_empty: bool = True,
) -> None:
    for workflow in tqdm.tqdm(hub.workflows, desc="ensure_revisions"):
        if (not workflow.revisions) or (not only_empty):
            repo = get_repo(workflow.repo_url)
            for revision in repo.get_revisions():
                revision.workflow = workflow
                workflow.revisions.append(revision)


def what_to_execute(
    hub: RegistryHub,
    time_bound: DateTime,
    conditions: list[Condition],
    desired_execution_count: int = 1,
    max_executions: Optional[int] = None,
    seed: int = 0,
) -> list[tuple[Revision, Condition]]:
    revisions_conditions: list[tuple[Revision, Condition]] = []
    for workflow in hub.workflows:
        for revision in workflow.revisions:
            for condition in conditions:
                actual_execution_count = sum(
                    execution.datetime > time_bound
                    for execution in revision.executions
                    if execution.condition == condition
                )
                n_executions = (desired_execution_count - actual_execution_count)
                revisions_conditions.extend(n_executions * [(revision, condition)])
    revisions_conditions = functional_shuffle(revisions_conditions, seed=seed)
    if max_executions:
        revisions_conditions = revisions_conditions[:max_executions]
    return revisions_conditions


def check_nodes_are_owned(hub: RegistryHub) -> None:
    raise NotImplementedError


def review_failures(hub: RegistryHub) -> None:
    revisions = sorted(hub.revisions, key=curried_getattr(DateTime, "datetime"), reverse=True)
    n_total = sum(len(revision.executions) for revision in revisions)
    n_broken = sum(int(execution.status_code != 0) for revision in revisions for execution in revision.executions)
    print(f"{n_total} total, {n_broken} broken executions")
    for revision in revisions:
        for i, execution in enumerate(revision.executions):
            if execution.status_code != 0:
                assert revision.workflow is not None
                assert revision.workflow.registry is not None
                print(revision.workflow.registry.display_name, revision.workflow.display_name, revision.display_name)
                print(execution.logs.url)
                input(":")


storage = upath.UPath(
    "abfs://data/",
    account_name="wfregtest",
    credential=AzureCredential(),
)


index_path = upath.UPath(
    "abfs://index/",
    account_name="wfregtest",
    credential=AzureCredential(),
)

html_path = upath.UPath(
    "abfs://$web/",
    account_name="wfregtest",
    credential=AzureCredential(),
)


# TODO: should code be self-aware that it is in Git?


@click.group()
def main() -> None:
    pass


@main.command()
@ch_time_block.decor()
def regenerate() -> None:
    # This is an archive for my old code.
    # One should also, theoretically, be able to reconstruct hub by rerunning all of the archived code.
    hub = RegistryHub(registries=[])
    from .registries import snakemake_registry, nf_core_registry
    hub.registries.append(nf_core_registry())
    hub.registries.append(snakemake_registry())
    ensure_revisions(hub, only_empty=True)
    serialize(hub, index_path)


@main.command()
@ch_time_block.decor()
def clear() -> None:
    (index_path / "nf-core_executions.yaml").write_text("[]")
    (index_path / "snakemake-workflow-catalog_executions.yaml").write_text("[]")
    for blob in tqdm.tqdm(list(index_path.glob("**.tar.xz"))):
        blob.unlink()
    if Path(".repos").exists():
        shutil.rmtree(".repos")


@main.command()
@click.argument("max_executions", type=int)
@ch_time_block.decor()
def test(max_executions: int) -> None:
    hub = deserialize(index_path)
    revisions_conditions = what_to_execute(
        hub=hub,
        time_bound=DateTime(2022, 8, 1),
        conditions=[Condition.NO_CONTROLS],
        desired_execution_count=1,
        max_executions=max_executions,
    )
    parallel_execute(
        hub,
        revisions_conditions,
        parallelism=10,
        index_path=index_path,
        serialize_every=TimeDelta(seconds=0),
        oversubscribe=False,
        remote=True,
        storage=storage,
    )
    serialize(hub, index_path)


@main.command()
@click.option("--max-executions", type=int, default=-1)
@click.option("--engine", type=str, default="")
@ch_time_block.decor()
def retest(max_executions: int, engine: str) -> None:
    hub = deserialize(index_path)
    revisions_conditions = [
        (expect_type(Revision, execution.revision), execution.condition)
        for execution in hub.failed_executions
        if engine == "" or engine == expect_type(Workflow, expect_type(Revision, execution.revision).workflow).engine
    ]
    if max_executions != -1:
        revisions_conditions = revisions_conditions[:max_executions]
    parallel_execute(
        hub,
        revisions_conditions,
        parallelism=10,
        index_path=index_path,
        serialize_every=TimeDelta(seconds=0),
        oversubscribe=False,
        remote=True,
        storage=storage,
    )
    remove_older_executions(hub)
    serialize(hub, index_path)


@main.command()
@ch_time_block.decor()
def report() -> None:
    hub = deserialize(index_path)
    (html_path / "result.html").write_text(report_html(hub))
    (html_path / "404.html").write_text(Path("docs/404.html").read_text())
    print("    az storage blob update --container-name '$web' --name result.html --account-name wfregtest --content-type text/html")


@main.command()
def delete_old() -> None:
    hub = deserialize(index_path)
    remove_older_executions(hub)
    serialize(hub, index_path)


def remove_older_executions(hub: RegistryHub) -> None:
    for revision in tqdm.tqdm(hub.revisions, desc="revisions"):
        if len(revision.executions) > 2:
            print(f"{revision!s} has multiple")
            newest_execution = revision.executions[0]
            for execution in revision.executions:
                if execution.datetime >= newest_execution.datetime:
                    newest_execution = execution
            print(f"{newest_execution.datetime!s} is the newest")
            old_executions = revision.executions[:]
            old_executions.remove(newest_execution)
            revision.executions = [newest_execution]
            for execution in old_executions:
                for file in [execution.logs, execution.outputs]:
                    url = file.url
                    print(f"Delete {url}")
                    fs_prefix = "file:///"
                    azure_prefix = "https://wfregtest.blob.core.windows.net/"
                    if url is None:
                        pass
                    elif url.startswith(azure_prefix):
                        # TODO: handle this based on generic storage
                        upath.UPath(
                            url[len(azure_prefix):],
                            account_name="wfregtest",
                            credential=AzureCredential(),
                        ).unlink()
                    elif url.startswith(fs_prefix):
                        Path(url[len(fs_prefix):]).unlink()
                    else:
                        raise NotImplementedError(f"Delete routine not implemented for {url}")


@main.command()
def post_process() -> None:
    from .postprocess import get_data
    get_data()


@main.command()
def review() -> None:
    hub = deserialize(index_path)
    review_failures(hub)


@main.command()
def verify() -> None:
    hub = deserialize(index_path)
    serialize(hub, index_path)


@main.command()
def classify_errors() -> None:
    import tarfile
    import urllib
    import shutil

    from .engines import engines
    from .serialization import serialize, deserialize
    from .util import create_temp_dir, http_download_with_cache

    hub = deserialize(index_path)
    failed_executions = [
        execution
        for execution in hub.failed_executions
        if execution.workflow_error is None and execution.logs.url is not None
    ]
    random.seed(1)
    random.shuffle(failed_executions)
    cache_path = Path(".cache")
    cache_path.mkdir(exist_ok=True)
    for execution in tqdm.tqdm(failed_executions, desc="executions"):
        url = execution.logs.url
        assert url
        url = str(url)
        with create_temp_dir() as temp_dir:
            tarball_path = temp_dir / "archive.tar.xz"
            http_download_with_cache(url, tarball_path, cache_path)
            with tarfile.open(str(tarball_path), mode="r:xz") as tarball:
                tarball.extractall(str(temp_dir))
            revision = execution.revision
            assert revision is not None
            workflow = revision.workflow
            assert workflow is not None
            execution.workflow_error = engines[workflow.engine].parse_error(temp_dir)
        if execution.workflow_error is None:
            print("Unparsed error for", execution)
        serialize(hub, index_path)


main()
