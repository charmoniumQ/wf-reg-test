import collections
import logging
import warnings
import itertools
import multiprocessing
import random
import re
import shutil
import sys
import urllib
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
from pathlib import Path
from typing import cast, Optional, Callable, Any

import click
import charmonium.time_block as ch_time_block
import yaml
import tqdm

from .serialization import serialize, deserialize
from .repos import get_repo
from .workflows import RegistryHub, Revision, Workflow, Condition, Execution, File
from .util import groupby_dict, functional_shuffle, expect_type, curried_getattr, http_content_length, upath_to_url
from .executable import Machine
from .parallel_execute import parallel_execute
from .high_level_errors import classify
from .config import data_path, index_path, cache_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ch_time_block.disable_stderr()

for name in ["paramiko", "azure"]:
    logging.getLogger(name).setLevel(logging.WARNING)
    logging.getLogger(name).propagate = False


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


def delete_execution(execution: Execution, confirm: bool = True) -> None:
    if input(f"Remove {execution}? y/n\n") == "y":
        for file_bundle in [execution.logs, execution.outputs]:
            file_bundle_files = (index_path / "files" / f"{file_bundle.archive.hash_val}")
            if file_bundle_files.exists():
                file_bundle_files.unlink()
            url = file_bundle.archive.url
            if url is not None:
                url.unlink()
        revision = execution.revision
        assert revision
        revision.executions.remove(execution)


def delete_orphans_in_storage(hub: RegistryHub) -> None:
    known_files = set(itertools.chain.from_iterable(
        (execution.logs.archive.url, execution.outputs.archive.url)
        for execution in hub.executions
    ))
    with ch_time_block.ctx("globbing_storage"):
        all_files = set(data_path.glob("**"))
    for orphaned_file in tqdm.tqdm(all_files - known_files, desc="file"):
        print(f"Remove {orphaned_file}? Y/n")
        if input().lower()[0] == "y":
            orphaned_file.unlink()


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
    hub = deserialize(index_path)
    for registry in hub.registries:
        path = index_path / f"{registry.display_name}_executions.pkl"
        if path.exists():
            path.unlink()
    for blob in tqdm.tqdm(list(data_path.glob("**.tar.xz")), desc="file archive"):
        blob.unlink()
    for blob in tqdm.tqdm(list(index_path.glob("files/**")), desc="file maps"):
        blob.unlink()
    if Path(".repos").exists():
        shutil.rmtree(".repos")


@main.command()
@click.option("--max-executions", type=int, default=None)
@click.option("--serialize-every", type=int, default=0)
@click.option("--seed", type=int, default=0)
@click.option("--dry-run", type=bool, is_flag=True, default=0)
@ch_time_block.decor()
def test(max_executions: Optional[int], serialize_every: int, seed: int, dry_run: bool) -> None:
    hub = deserialize(index_path)
    revisions_conditions = what_to_execute(
        hub=hub,
        time_bound=DateTime(2022, 8, 1),
        conditions=[Condition.NO_CONTROLS],
        desired_execution_count=1,
        max_executions=max_executions,
    )
    revisions_conditions = functional_shuffle(revisions_conditions, seed=seed)
    if dry_run:
        for revision, condition in revisions_conditions:
            print(revision, condition)
    else:
        parallel_execute(
            hub,
            revisions_conditions,
            index_path=index_path,
            serialize_every=TimeDelta(seconds=serialize_every),
            oversubscribe=False,
            storage=data_path,
        )
        serialize(hub, index_path)


@main.command()
@click.option("--max-executions", type=int, default=-1)
@click.option("--predicate", type=str, default="True")
@click.option("--seed", type=int, default=0)
@click.option("--serialize-every", type=int, default=0)
@ch_time_block.decor()
def retest(max_executions: int, predicate: str, seed: int, serialize_every: int) -> None:
    hub = deserialize(index_path)
    revisions_conditions = [
        (expect_type(Revision, execution.revision), execution.condition)
        for execution in hub.executions
        if eval(predicate, globals(), {**locals(), "error": execution.workflow_error, "revision": execution.revision, "workflow": expect_type(Revision, execution.revision).workflow})
    ]
    revisions_conditions = functional_shuffle(revisions_conditions, seed)
    if max_executions != -1:
        revisions_conditions = revisions_conditions[:max_executions]
    parallel_execute(
        hub,
        revisions_conditions,
        index_path=index_path,
        serialize_every=TimeDelta(seconds=serialize_every),
        oversubscribe=False,
        storage=data_path,
    )
    delete_duplicate_executions(hub)
    serialize(hub, index_path)


@main.command()
@ch_time_block.decor()
def report() -> None:
    from .report import report_html
    import azure.storage.blob
    import azure.identity
    hub = deserialize(index_path)
    report_text = ch_time_block.decor()(report_html)(hub)
    with ch_time_block.ctx("upload_result"):
        if index_path._url.scheme == "abfs":
            account_name: str = index_path._kwargs['account_name']
            azure.storage.blob.BlobClient(
                account_url=f"https://{account_name}.blob.core.windows.net",
                container_name=index_path._url.netloc,
                blob_name="results.html",
                # Note that this should be synchronous not AIO like html_path._kwargs["credential"]
                credential=azure.identity.DefaultAzureCredential(),
            ).upload_blob(
                report_text,
                overwrite=True,
                content_settings=azure.storage.blob.ContentSettings(  # type: ignore
                    content_type="text/html",
                ),
            )
        else:
            (index_path / "results.html").write_text(report_text)


def delete_duplicate_executions(hub: RegistryHub) -> None:
    revisions_with_multiple = [
        revision
        for revision in hub.revisions
        if len(revision.executions) > 1
    ]
    for revision in tqdm.tqdm(revisions_with_multiple, desc="revisions"):
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
                url = file.archive.url
                if url and url.exists():
                    try:
                        url.unlink()
                    except Exception as e:
                        print(type(url), url, type(e), str(e))


@main.command()
def post_process() -> None:
    from .post_process import post_process
    post_process()


@main.command()
@click.option("--delete-duplicates", type=bool, is_flag=True, default=False)
@click.option("--delete-orphans", type=bool, is_flag=True, default=False)
@click.option("--delete-predicate", type=str, default="False")
@click.option("--check-size", type=bool, is_flag=True, default=False)
def verify(delete_duplicates: bool, delete_orphans: bool, delete_predicate: str, check_size: bool) -> None:
    hub = deserialize(index_path)
    if delete_duplicates:
        delete_duplicate_executions(hub)
    if delete_orphans:
        delete_orphans_in_storage(hub)
    to_delete = []
    for execution in hub.executions:
        if eval(delete_predicate, globals(), {**locals(), "error": execution.workflow_error}):
            to_delete.append(execution)
    for execution in tqdm.tqdm(to_delete):
        delete_execution(execution)
    if check_size:
        import dill  # type: ignore
        for executions in hub.executions:
            for file_bundle in [execution.logs, execution.outputs]:
                len(file_bundle.files)
        sizes = sorted([
            (len(dill.dumps(workflow)), random.randint(0, 100000), workflow)
            for workflow in hub.workflows
        ])
        # Note that Parsl has a serialization limit.
        # We need to check that all of our objects are less than the limit.
        limit = 1048576 # found in `cat runinfo/*/parsl.log | grep 'Serialized object exceeds buffer threshold of'`
        for size, _, workflow in sizes[:6]:
            print(f"{size/limit:.2f} * limit = len(dill.dumps({workflow!s}))")
            for revision in workflow.revisions:
                print(f"  {len(dill.dumps(revision))/limit:.2f} * limit ~ len(dill.dumps({revision!s}))")
                for execution in revision.executions:
                    print(f"    {len(dill.dumps(execution))/limit:.2f} * limit ~ len(dill.dumps({execution!s}))")
                    print(f"      {len(dill.dumps(execution.outputs))/limit:.2f} * limit ~ len(dill.dumps(execution.outputs))")
                    print(f"        {len(dill.dumps(execution.outputs))/limit:.2f} * limit ~ len(dill.dumps(execution.outputs.files))")
                    print(f"      {len(dill.dumps(execution.logs))/limit:.2f} * limit ~ len(dill.dumps(execution.logs))")
                    print(f"        {len(dill.dumps(execution.logs))/limit:.2f} * limit ~ len(dill.dumps(execution.logs.files))")
                    print(f"      {len(dill.dumps(execution.workflow_error))/limit:.2f} * limit ~ len(dill.dumps(execution.workflow_error))")
    serialize(hub, index_path)


@main.command()
@click.option("--url-part", type=str, default="")
@click.option("--reclassify", is_flag=True, type=bool, default=False)
def classify_errors(url_part: str, reclassify: bool) -> None:
    import tarfile
    import urllib
    import shutil

    from .engines import engines
    from .serialization import serialize, deserialize
    from .util import create_temp_dir, http_download_with_cache

    hub = deserialize(index_path)
    executions_to_classify = [
        execution
        for execution in hub.failed_executions
        if all([
                (reclassify or execution.workflow_error is None),
                execution.logs.archive.url is not None,
                url_part in str(execution.logs.archive.url),
        ])
    ]
    random.seed(1)
    random.shuffle(executions_to_classify)
    for execution in tqdm.tqdm(executions_to_classify, desc="executions"):
        strurl = upath_to_url(execution.logs.archive.url)
        with create_temp_dir() as temp_dir:
            tarball_path = temp_dir / "archive.tar.xz"
            http_download_with_cache(strurl, tarball_path, cache_path)
            with tarfile.open(str(tarball_path), mode="r:xz") as tarball:
                tarball.extractall(str(temp_dir))
            revision = execution.revision
            assert revision is not None
            workflow = revision.workflow
            assert workflow is not None
            i = revision.executions.index(execution)
            revision.executions[i] = execution.with_attrs(workflow_error=engines[workflow.engine].parse_error(temp_dir, Path("/does-not-exist"), execution.resources, execution.status_code))
        if revision.executions[i] is None:
            print("Unparsed error for", execution)
        else:
            print(type(execution.workflow_error), execution.workflow_error.kind)
            serialize(hub, index_path, warn=False)


main()
