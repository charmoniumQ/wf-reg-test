from datetime import datetime, timedelta
import json
import logging
from pathlib import Path
import warnings

import sqlalchemy
import sqlalchemy_schemadisplay  # type: ignore

from .report import report_html
from .workflows import Base, Execution, WorkflowApp, Revision, MerkleTreeNode, Blob
from .repos import get_repo_accessor
from .engines import engines


def create_tables() -> None:
    print("Creating tables if it doesn't already exist")
    Base.metadata.create_all(engine)


def clear_tables() -> None:
    print("Clearing tables")
    Base.metadata.drop_all(engine)


def diagram_object_model(path: Path) -> None:
    print(f"Generating diagram {path!s}")
    graph = sqlalchemy_schemadisplay.create_schema_graph(
        metadata=Base.metadata,
        show_datatypes=False,
        show_indexes=False,
        rankdir="LR",
        concentrate=True,
    )
    graph.write_png(path)


def add_default_wf() -> None:
    default_wf_app = WorkflowApp(
        workflow_engine_name="nextflow",
        url="https://nf-co.re/mag",
        display_name="nf-core/mag",
        repo_url="https://github.com/nf-core/mag?only_tags"
    )
    print(f"Adding {default_wf_app.display_name}")
    with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
        session.add(default_wf_app)


def report(path: Path) -> None:
    print(f"Generating report {path!s}")
    with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
        workflow_apps = session.execute(sqlalchemy.select(WorkflowApp)).scalars().all()
        path.write_text(report_html(workflow_apps))


def refresh_revisions() -> None:
    now = datetime.now()
    blobs_in_transaction: dict[int, Blob] = {}
    nodes_in_transaction: dict[int, MerkleTreeNode] = {}
    with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
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
                print(f"Adding {wf_app.display_name} {revision.display_name}")
                with repo.checkout(revision.url) as local_copy:
                    revision.tree = MerkleTreeNode.from_path(  # type: ignore
                        local_copy,
                        session,
                        nodes_in_transaction,
                        blobs_in_transaction,
                    )
                wf_app.revisions.append(revision)


def run_out_of_date(period: timedelta) -> None:
    now = datetime.now()
    with sqlalchemy.orm.Session(engine, future=True) as session:
        with session.begin():
            revisions_to_test = (
                session.execute(
                    sqlalchemy.select(Revision)
                    .join(WorkflowApp)
                    .join(Execution, isouter=True)
                    # .where((Execution.datetime < now - period) | (Execution == None))
                )
                .scalars()
                .all()
            )
        for revision in revisions_to_test:
            print(f"Running {revision.workflow_app.display_name} {revision.display_name}")
            # with session.begin():
            if True:
                repo = get_repo_accessor(revision.workflow_app.repo_url)
                with repo.checkout(revision.url) as local_copy:
                    wf_engine = engines[revision.workflow_app.workflow_engine_name]
                    execution = wf_engine.run(local_copy, session)
                    revision.executions.append(execution)


secrets = json.loads(Path("secrets.json").read_text())
engine = sqlalchemy.create_engine(secrets["db_url"], future=True)
# restart_db = True
# if restart_db:
#     clear_tables()
#     create_tables()
#     add_default_wf()
#     refresh_revisions()

## diagram_object_model(Path("dbschema.png"))

run_out_of_date(timedelta(days=100))
# report(Path("build/results.html"))

# Scan registry
# Look for new versions of repo or all repos
# Run tests
