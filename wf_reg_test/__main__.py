import collections
import logging
import warnings
import itertools
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from pathlib import Path
from typing import cast

import charmonium.time_block as ch_time_block
import yaml
from tqdm import tqdm

from .serialization import serialize, deserialize
from .registries import snakemake_registry, nf_core_registry
from .report import report_html
from .repos import get_repo
from .workflows import RegistryHub, Revision, Workflow
from .util import groupby_dict

logging.basicConfig()
logger = logging.getLogger("wf_reg_test")
logger.setLevel(logging.INFO)
ch_time_block.disable_stderr()
data = Path("data.yaml")


@ch_time_block.decor()
def ensure_revisions(
        hub: RegistryHub, only_empty: bool = True,
) -> None:
    for workflow in tqdm(hub.workflows, desc="ensure_revisions"):
        if (not workflow.revisions) or (not only_empty):
            repo = get_repo(workflow.repo_url)
            for revision in repo.get_revisions():
                revision.workflow = workflow
                workflow.revisions.append(revision)


def report(hub: RegistryHub) -> None:
    Path("docs/results.html").write_text(report_html(hub))


def ensure_recent_executions(
    wf_apps: list[Workflow],
    period: TimeDelta,
    desired_count: int = 1,
    dry_run: bool = False,
) -> None:
    from .engines import engines
    now = DateTime.now()
    revisions_to_test: list[Revision] = []
    for wf_app in wf_apps:
        for revision in wf_app.revisions:
            existing_count = sum(
                execution.datetime > now - period
                for execution in revision.executions
            )
            if existing_count < desired_count:
                revisions_to_test.extend([revision] * (desired_count - existing_count))
    # random.shuffle(revisions_to_test)
    for revision in revisions_to_test:
        logger.info("Running %s", revision)
        if not dry_run:
            execution = None
            raise NotImplementedError
            revision.executions.append(execution)


def check_nodes_are_owned(hub: RegistryHub) -> None:
    raise NotImplementedError


def regenerate() -> RegistryHub:
    # This is an archive for my old code.
    # One should also, theoretically, be able to reconstruct hub by rerunning all of the archived code.
    hub = RegistryHub(registries=[])
    hub.registries.append(nf_core_registry())
    hub.registries.append(snakemake_registry())
    return hub


@ch_time_block.decor()
def main() -> None:
    data_path = Path("data")
    with ch_time_block.ctx("load", print_start=False):
        hub = deserialize(data_path)
    with ch_time_block.ctx("process", print_start=False):
        ensure_revisions(hub, only_empty=True)
    with ch_time_block.ctx("store", print_start=False):
        serialize(hub, data_path)
    with ch_time_block.ctx("report", print_start=False):
        report(hub)


main()
