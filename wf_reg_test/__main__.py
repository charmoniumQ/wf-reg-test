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
from .workflows import RegistryHub, Revision, Workflow, Condition, Execution
from .util import groupby_dict, functional_shuffle, expect_type, curried_getattr, AzureCredential
from .executable import Machine
from .parallel_execute import parallel_execute

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ch_time_block.disable_stderr()

logging.getLogger("parsl").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("azure").setLevel(logging.WARNING)


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
    revisions = sorted(hub.revisions, key=curried_getattr("datetime"), reverse=True)
    n_total = sum(len(revision.executions) for revision in revisions)
    n_broken = sum(int(execution.status_code != 0) for revision in revisions for execution in revision.executions)
    print(f"{n_total} total, {n_broken} broken executions")
    for revision in revisions:
        for i, execution in enumerate(revision.executions):
            if execution.status_code != 0:
                assert revision.workflow is not None
                assert revision.workflow.registry is not None
                print(revision.workflow.registry.display_name, revision.workflow.display_name, revision.display_name)
                for path in [Path("stderr.txt"), Path("stdout.txt")]:
                    if path in execution.logs.contents:
                        url = execution.logs.contents[path].contents_url
                        if url and url.startswith("file:///"):
                            path = Path(url[7:])
                            cwd = Path().resolve()
                            if path.is_relative_to(cwd):
                                print(path.relative_to(cwd))
                            else:
                                print(path)
                        else:
                            print(url)
                input(":")


storage = upath.UPath(
    "abfs://data/",
    account_name="wfregtest",
    credential=AzureCredential(),
)


data_path = storage / "index"
# TODO: store index in different place
# TODO: store results in different place
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
    serialize(hub, data_path)


@main.command()
@ch_time_block.decor()
def clear() -> None:
    (data_path / "nf-core_executions.yaml").write_text("[]")
    (data_path / "snakemake-workflow-catalog_executions.yaml").write_text("[]")
    for blob in tqdm.tqdm(list(data_path.glob("**.tar.xz"))):
        blob.unlink()
    if Path(".repos").exists():
        shutil.rmtree(".repos")


@main.command()
@click.argument("max_executions", type=int)
@ch_time_block.decor()
def test(max_executions: int) -> None:
    hub = deserialize(data_path)
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
        data_path=data_path,
        serialize_every=TimeDelta(seconds=0),
        oversubscribe=False,
        remote=True,
        storage=storage,
    )
    serialize(hub, data_path)


@main.command()
@ch_time_block.decor()
def report() -> None:
    hub = deserialize(data_path)
    (storage / "results.html").write_text(report_html(hub))


@main.command()
@ch_time_block.decor()
def delete_failures() -> None:
    hub = deserialize(data_path)
    revisions = [
        revision
        for registry in hub.registries
        for workflow in registry.workflows
        for revision in workflow.revisions
    ]
    for revision in tqdm(revisions, desc="revisions"):
        bad_executions      = [execution for execution in revision.executions if not execution.successful]
        revision.executions = [execution for execution in revision.executions if execution.successful]
        for execution in bad_executions:
            for file in [*execution.logs.contents.values(), *execution.outputs.contents.values()]:
                urls_to_delete = []
                url = file.contents_url
                if url is not None:
                    # If is a path within a tarball, this requires special care
                    if m := re.match("tar://.*::(.*)", url):
                        urls_to_delete.append(m.group(1))
                    else:
                        urls_to_delete.append(url)
            for url in set(urls_to_delete):
                if m := re.match("file://(.*)", url):
                    Path(m.group(1)).unlink()
                elif m := re.match("(abfs://.*)", url):
                    # TODO: handle this based on generic storage
                    upath.UPath(
                        m.group(1),
                        account_name="wfregtest",
                        credential=AzureCredential(),
                    ).unlink()
                else:
                    raise NotImplementedError(f"Delete routine not implemented for {url}")
    serialize(hub, data_path)


# @main.command()
# def post_process() -> None:
#     from .postprocess import get_data
#     get_data()


@main.command()
def review() -> None:
    hub = deserialize(data_path)
    review_failures(hub)


main()
