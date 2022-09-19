import json
import logging
import warnings
from datetime import datetime, timedelta
from pathlib import Path

import charmonium.time_block as ch_time_block
from rich.prompt import Confirm
import sqlalchemy
from sqlalchemy import func
import sqlalchemy_schemadisplay  # type: ignore

from .engines import engines
from .report import report_html
from .repos import get_repo_accessor
from .workflows import Base, Blob, Execution, MerkleTreeNode, Revision, WorkflowApp, Machine


logging.basicConfig()
logger = logging.getLogger("wf_reg_test")
logger.setLevel(logging.INFO)
ch_time_block.disable_stderr()


def ensure_tables(engine: sqlalchemy.engine.Engine) -> None:
    Base.metadata.create_all(engine)


def clear_tables(engine: sqlalchemy.engine.Engine) -> None:
    input("Dropping tables\nEnter to continue, Ctrl+C to abort")
    Base.metadata.drop_all(engine)


def diagram_object_model(path: Path) -> None:
    graph = sqlalchemy_schemadisplay.create_schema_graph(
        metadata=Base.metadata,
        show_datatypes=False,
        show_indexes=False,
        rankdir="LR",
        concentrate=True,
    )
    graph.write_png(path)


def ensure_default_wfs(session: sqlalchemy.orm.Session) -> None:
    wf_apps = [
        WorkflowApp(
            workflow_engine_name="nextflow",
            url="https://nf-co.re/mag",
            display_name="nf-core/mag",
            repo_url="https://github.com/nf-core/mag?only_tags",
        ),
        WorkflowApp(
            workflow_engine_name="nextflow",
            url="https://nf-co.re/rnaseq",
            display_name="nf-core/rnaseq",
            repo_url="https://github.com/nf-core/rnaseq?only_tags"
        ),
        WorkflowApp(
            workflow_engine_name="nextflow",
            url="https://nf-co.re/chipseq",
            display_name="nf-core/chipseq",
            repo_url="https://github.com/nf-core/chipseq?only_tags"
        ),
    ]
    with session.begin():
        for wf_app in wf_apps:
            existing_in_db = (
                session.execute(
                    sqlalchemy.select(WorkflowApp).where(
                        WorkflowApp.url == wf_app.url
                    )
                )
                .scalars()
                .one_or_none()
            )
            if existing_in_db is None:
                logger.info("Adding %s", wf_app)
                session.add(wf_app)


def report(path: Path, session: sqlalchemy.orm.Session) -> None:
    path.parent.mkdir(exist_ok=True, parents=True)
    with session.begin():
        workflow_apps = session.execute(sqlalchemy.select(WorkflowApp)).scalars().all()
        path.write_text(report_html(workflow_apps))


@ch_time_block.decor()
def ensure_revisions(session: sqlalchemy.orm.Session) -> None:
    blobs_in_transaction: dict[int, Blob] = {}
    nodes_in_transaction: dict[int, MerkleTreeNode] = {}
    with session.begin():
        wf_apps = session.execute(sqlalchemy.select(WorkflowApp)).scalars()
        for wf_app in wf_apps:
            repo = get_repo_accessor(wf_app.repo_url)
            db_revisions = set(wf_app.revisions)
            observed_revisions = set(repo.get_revisions())
            deleted_revisions = db_revisions - observed_revisions
            new_revisions = observed_revisions - db_revisions
            if deleted_revisions:
                warnings.warn(
                    f"{len(deleted_revisions)} deleted revisions on repo {repo}",
                )
            for revision in new_revisions:
                logger.info("Adding %s", revision)
                with repo.checkout(revision.url) as local_copy:
                    revision.tree = MerkleTreeNode.from_path(  # type: ignore
                        local_copy,
                        session,
                        nodes_in_transaction,
                        blobs_in_transaction,
                    )
                wf_app.revisions.append(revision)


def ensure_recent_executions(period: timedelta, session: sqlalchemy.orm.Session) -> None:
    now = datetime.now()
    with session.begin():
        recent_executions = (
            sqlalchemy.select(Execution._revision_id).where(
                Execution.datetime > now - period
            )
        ).subquery()
        revisions_to_test = (
            session.execute(
                sqlalchemy.select(Revision)
                .join(
                    recent_executions,
                    recent_executions.c._revision_id == Revision._id,
                    isouter=True,
                )
                .where(recent_executions.c._revision_id == None)
            )
            .scalars()
            .all()
        )
    with session.begin():
        for revision in revisions_to_test:
            logger.info("Running %s", revision)
            repo = get_repo_accessor(revision.workflow_app.repo_url)
            with repo.checkout(revision.url) as local_copy:
                wf_engine = engines[revision.workflow_app.workflow_engine_name]
                execution = wf_engine.run(local_copy, session)
                revision.executions.append(execution)


def fix_failed_revisions(session: sqlalchemy.orm.Session) -> None:
    with session.begin():
        executions = session.execute(
            sqlalchemy.select(Execution)
            .where(Execution.user_cpu_time == timedelta(seconds=0.0))
        ).scalars().all()
        for execution in executions:
            logger.info(f"Fixing {execution!s}")
            for child in execution.output.children:
                if child.name == "time":
                    time_output = child.blob.data.decode().strip().split("\n")[-1].split(" ")
                    try:
                        mem_kb, system_sec, user_sec, wall_time = time_output
                    except ValueError:
                        warnings.warn("Unable to fix")
                        mem_kb, system_sec, user_sec, wall_time = "0", "0.0", "0.0", "0.0"
                    execution.wall_time = timedelta(seconds=float(wall_time))
                    execution.user_cpu_time = timedelta(seconds=float(user_sec))
                    execution.system_cpu_time = timedelta(seconds=float(system_sec))
                    execution.max_rss = int(mem_kb) * 1024


def enable_sql_echo() -> None:
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def get_db_info(session: sqlalchemy.orm.Session) -> str:
    with session.begin():
        wf_apps = session.query(func.count(WorkflowApp._id)).scalar()
        revisions = session.query(func.count(Revision._id)).scalar()
        executions = session.query(func.count(Execution._id)).scalar()
        machines = session.query(func.count(Machine._id)).scalar()
        blobs = session.query(func.count(Blob.hash)).scalar()
        return f"{blobs} blobs from {executions} executions of {revisions} revisions of {wf_apps} workflows on {machines} machines"


# def fix_size(session: sqlalchemy.orm.Session) -> None:
#     with session.begin():
#         blobs = set(session.execute(
#             sqlalchemy.select(Blob)
#         ).scalars().all())
#         for blob in blobs:
#             blob.size = len(blob.data)

#         nodes = set(session.execute(
#             sqlalchemy.select(MerkleTreeNode)
#         ).scalars().all())
#         while nodes:
#             logger.info(len(nodes), "nodes remaining")
#             for node in list(nodes):
#                 if all([child.is_updated for child in node.children]):
#                     node.size_of_descendents = node.blob.size + sum([child.size_of_descendents for child in node.children])
#                     nodes.remove(node)


def check_blobs_are_owned(session: sqlalchemy.orm.Session) -> None:
    with session.begin():
        blobs = session.execute(
            sqlalchemy.select(Blob)
            .join(MerkleTreeNode, isouter=True)
            .where(MerkleTreeNode.hash == None)
        ).scalars().all()
        for blob in blobs:
            if Confirm(f"Delete {blob!s}"):
                blob.delete()
            else:
                logger.info("Not deleting")


def check_nodes_are_owned(session: sqlalchemy.orm.Session) -> None:
    pass


@ch_time_block.decor()
def main() -> None:
    engine = sqlalchemy.create_engine("data.sqlite", future=True)
    with sqlalchemy.orm.Session(engine, future=True) as session:
        # clear_tables(engine)
        # diagram_object_model(Path("dbschema.png"))
        ensure_tables(engine)
        logger.info("Before: " + get_db_info(session))

        # ensure_default_wfs(session)
        # ensure_revisions(session)
        # ensure_recent_executions(timedelta(days=100), session)
        # fix_failed_revisions(session)
        # delete_zero_time_executions(session)

        check_blobs_are_owned(session)
        check_nodes_are_owned(session)

        logger.info("After: " + get_db_info(session))
        report(Path("docs/results.html"), session)


main()


# https://snakemake.github.io/snakemake-workflow-catalog/data.js
# https://github.com/nf-core/nf-co.re/blob/master/update_pipeline_details.php#L85
