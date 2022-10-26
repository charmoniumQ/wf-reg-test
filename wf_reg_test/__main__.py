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

from .engines import engines
from .registries import snakemake_registry, nf_core_registry
from .report import report_html
from .repos import get_repo_accessor
from .workflows import Revision, Workflow
from .util import groupby_dict

logging.basicConfig()
logger = logging.getLogger("wf_reg_test")
logger.setLevel(logging.INFO)
ch_time_block.disable_stderr()
data = Path("data.yaml")


@ch_time_block.decor()
def ensure_revisions(
    wf_apps: list[Workflow], only_empty: bool = True, delete_empty: bool = True
) -> list[Workflow]:
    ret_wf_apps: list[Workflow] = []
    for wf_app in tqdm(wf_apps):
        if (not wf_app.revisions) or (not only_empty):
            repo = get_repo_accessor(wf_app.repo_url)
            db_revisions = list(wf_app.revisions)
            observed_revisions = list(repo.get_revisions(wf_app))
            deleted_revisions = [
                drevision
                for drevision in db_revisions
                if not any(
                    orevision.url == drevision.url for orevision in observed_revisions
                )
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


def report(wf_apps: list[Workflow]) -> None:
    Path("docs/results.html").write_text(report_html(wf_apps))


def ensure_recent_executions(
    wf_apps: list[Workflow],
    period: TimeDelta,
    desired_count: int = 1,
    dry_run: bool = False,
) -> None:
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
            repo = get_repo_accessor(revision.workflow.repo_url)
            with repo.checkout(revision.url) as local_copy:
                raise NotImplementedError
                wf_engine = engines[revision.workflow_app.workflow_engine_name]
                execution = wf_engine.run(local_copy, revision)
                revision.executions.append(execution)
        if not dry_run:
            report(wf_apps)
            data.write_text(yaml.dump(wf_apps))


def check_nodes_are_owned(wf_apps: list[Workflow]) -> None:
    raise NotImplementedError


def merge_duplicates(wf_apps: list[Workflow]) -> list[Workflow]:
    raise NotImplementedError


@ch_time_block.decor()
def main() -> None:
    with ch_time_block.ctx("load", print_start=False):
        wf_apps = cast(
            list[Workflow], yaml.load(data.read_text(), Loader=yaml.Loader)
        )
        assert all(isinstance(wf_app, Workflow) for wf_app in wf_apps)
    with ch_time_block.ctx("process", print_start=False):
        # wf_apps = ensure_revisions(wf_apps, only_empty=True, delete_empty=True)
        # ensure_recent_executions(wf_apps, TimeDelta(days=100), 2, dry_run=False)
        wf_apps = merge_duplicates(wf_apps)
    with ch_time_block.ctx("store", print_start=False):
        data.write_text(yaml.dump(wf_apps))
    with ch_time_block.ctx("report", print_start=False):
        report(wf_apps)


main()


# https://snakemake.github.io/snakemake-workflow-catalog/data.js
# https://github.com/nf-core/nf-co.re/blob/master/update_pipeline_details.php#L85
