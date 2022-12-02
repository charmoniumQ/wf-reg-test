import collections
import logging
import warnings
import itertools
import multiprocessing
import random
import shutil
import sys
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from pathlib import Path
from typing import cast, Optional

import click
import charmonium.time_block as ch_time_block
import yaml
import tqdm

from .serialization import serialize, deserialize
from .report import report_html
from .repos import get_repo
from .workflows import RegistryHub, Revision, Workflow, Condition, Execution
from .util import groupby_dict, functional_shuffle, expect_type, curried_getattr
from .executable import Machine
from .parallel_execute import parallel_execute

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ch_time_block.disable_stderr()


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


def report(hub: RegistryHub) -> None:
    Path("docs/results.html").write_text(report_html(hub))


def what_to_execute(
    hub: RegistryHub,
    time_bound: DateTime,
    conditions: list[Condition],
    desired_execution_count: int = 1,
    execution_limit: Optional[int] = None,
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
    if execution_limit:
        revisions_conditions = revisions_conditions[:execution_limit]
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
                print(revision.workflow.registry.display_name, revision.workflow.display_name, revision.display_name)
                for path in [Path("stderr.txt"), Path("stdout.txt")]:
                    if path in execution.logs.contents:
                        url = execution.logs.contents[path].contents_url
                        if url.startswith("file:///"):
                            path = Path(url[7:])
                            cwd = Path().resolve()
                            if path.is_relative_to(cwd):
                                print(path.relative_to(cwd))
                            else:
                                print(path)
                        else:
                            print(url)
                input(":")


def regenerate() -> RegistryHub:
    # This is an archive for my old code.
    # One should also, theoretically, be able to reconstruct hub by rerunning all of the archived code.
    hub = RegistryHub(registries=[])
    from .registries import snakemake_registry, nf_core_registry
    hub.registries.append(nf_core_registry())
    hub.registries.append(snakemake_registry())
    ensure_revisions(hub, only_empty=True)
    return hub


data_path = Path("data")


@click.group()
def main() -> None:
    pass


@main.command()
@ch_time_block.decor()
def clear() -> None:
    (data_path / "nf-core_executions.yaml").write_text("[]")
    (data_path / "snakemake-workflow-catalog_executions.yaml").write_text("[]")
    shutil.rmtree(".repos")


@main.command()
@ch_time_block.decor()
def test() -> None:
    with ch_time_block.ctx("load", print_start=False):
        hub = deserialize(data_path)
    with ch_time_block.ctx("process", print_start=False):
        revisions_conditions = what_to_execute(
            hub=hub,
            time_bound=DateTime(2022, 8, 1),
            conditions=[Condition.NO_CONTROLS],
            desired_execution_count=1,
            execution_limit=15,
        )
        parallel_execute(
            hub,
            revisions_conditions,
            parallelism=10,
            data_path=data_path,
            serialize_every=TimeDelta(seconds=0),
            oversubscribe=False,
            remote=True,
            storage="adl://something/something"
        )
    with ch_time_block.ctx("store", print_start=False):
        serialize(hub, data_path)
    with ch_time_block.ctx("report", print_start=False):
        report(hub)

@main.command()
def review() -> None:
    with ch_time_block.ctx("load", print_start=False):
        hub = deserialize(data_path)
    review_failures(hub)


main()
