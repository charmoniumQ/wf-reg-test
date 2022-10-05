import json
import logging
import warnings
from datetime import datetime as DateTime, timedelta as TimeDelta
import random
from typing import cast
from pathlib import Path

import charmonium.time_block as ch_time_block
from rich.prompt import Confirm
from tqdm import tqdm
import yaml

from .registries import snakemake_registry
from .engines import engines
from .report import report_html
from .repos import get_repo_accessor
from .workflows2 import WorkflowApp2, Revision2


logging.basicConfig()
logger = logging.getLogger("wf_reg_test")
logger.setLevel(logging.INFO)
ch_time_block.disable_stderr()
data = Path("data.yaml")

@ch_time_block.decor()
def ensure_revisions(wf_apps: list[WorkflowApp2], only_empty: bool = True, delete_empty: bool = True) -> list[WorkflowApp2]:
    ret_wf_apps: list[WorkflowApp2] = []
    for wf_app in tqdm(wf_apps):
        if (not wf_app.revisions) or (not only_empty):
            repo = get_repo_accessor(wf_app.repo_url)
            db_revisions = list(wf_app.revisions)
            observed_revisions = list(repo.get_revisions(wf_app))
            deleted_revisions = [
                drevision
                for drevision in db_revisions
                if not any(orevision.url == drevision.url for orevision in observed_revisions)
            ]
            new_revisions = [
                orevision
                for orevision in observed_revisions
                if not any(orevision.url == drevision.url for drevision in db_revisions)
            ]
            if deleted_revisions:
                warnings.warn(
                    f"{len(deleted_revisions)} deleted revisions on repo {repo}",
                )
            wf_app.revisions.extend(new_revisions)
        if wf_app.revisions or (not delete_empty):
            ret_wf_apps.append(wf_app)
    return ret_wf_apps


def report(wf_apps: list[WorkflowApp2]) -> None:
    Path("docs/results.html").write_text(report_html(wf_apps))

def ensure_recent_executions(
        wf_apps: list[WorkflowApp2],
        period: TimeDelta,
        desired_count: int = 1,
        dry_run: bool = False,
) -> None:
    now = DateTime.now()
    revisions_to_test: list[Revision2] = []
    for wf_app in wf_apps:
        for revision in wf_app.revisions:
            existing_count = sum([
                execution.datetime > now - period
                for execution in revision.executions
            ])
            if existing_count < desired_count:
                revisions_to_test.extend([revision] * (desired_count - existing_count))
    # random.shuffle(revisions_to_test)
    for revision in revisions_to_test:
        logger.info("Running %s", revision)
        if not dry_run:
            repo = get_repo_accessor(revision.workflow_app.repo_url)
            with repo.checkout(revision.url) as local_copy:
                wf_engine = engines[revision.workflow_app.workflow_engine_name]
                execution = wf_engine.run(local_copy, revision)
                revision.executions.append(execution)
        if not dry_run:
            report(wf_apps)
            data.write_text(yaml.dump(wf_apps))


def remove_phantom_executions(wf_apps: list[WorkflowApp2]) -> None:
    for wf_app in wf_apps:
        for revision in wf_app.revisions:
            revision.executions = [
                execution
                for execution in revision.executions
                if execution.user_cpu_time > TimeDelta(seconds=0)
            ]


def check_nodes_are_owned(wf_apps: list[WorkflowApp2]) -> None:
    used_data = {
        revision.tree
        for wf_app in wf_apps
        for revision in wf_app.revisions
    } - {
        execution.output
        for wf_app in wf_apps
        for revision in wf_app.revisions
        for execution in revision.executions
    }
    orphaned_data = set(Path("data").iterdir()) - used_data
    if orphaned_data:
        warnings.warn(f"Orphaned data found: {orphaned_data}")


@ch_time_block.decor()
def main() -> None:
    with ch_time_block.ctx("load", print_start=False):
        wf_apps = cast(list[WorkflowApp2], yaml.load(data.read_text(), Loader=yaml.Loader))
        assert all(isinstance(wf_app, WorkflowApp2) for wf_app in wf_apps)
    # with ch_time_block.ctx("process", print_start=False):
        # wf_apps.extend(snakemake_registry())
        # wf_apps = ensure_revisions(wf_apps, only_empty=True, delete_empty=True)
        # ensure_recent_executions(wf_apps, TimeDelta(days=100), 2, dry_run=False)
        # remove_phantom_executions(wf_apps)
        # check_nodes_are_owned(wf_apps)
    # with ch_time_block.ctx("store", print_start=False):
    #     data.write_text(yaml.dump(wf_apps))
    with ch_time_block.ctx("report", print_start=False):
        report(wf_apps)


main()


# https://snakemake.github.io/snakemake-workflow-catalog/data.js
# https://github.com/nf-core/nf-co.re/blob/master/update_pipeline_details.php#L85
