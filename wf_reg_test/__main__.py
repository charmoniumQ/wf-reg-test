import json
from pathlib import Path

import sqlalchemy
import sqlalchemy_schemadisplay  # type: ignore

from .workflows import Base, WorkflowApp, Repo


path = Path("test.sqlite")
if path.exists():
    path.unlink()
engine = sqlalchemy.create_engine(f"sqlite:///{path}", future=True)


graph = sqlalchemy_schemadisplay.create_schema_graph(
    metadata=Base.metadata,
    show_datatypes=False,
    show_indexes=False,
    rankdir='LR',
    concentrate=True,
)
graph.write_png('dbschema.png')
Base.metadata.create_all(engine)


default_wf_app = WorkflowApp(
    workflow_engine_name="nextflow",
    url="https://nf-co.re/mag",
    name="nf-core/mag",
    repo=Repo(
        type="github",
        _kwargs=json.dumps({
            "user": "nf-core",
            "repo": "mag",
            "only_tags": True
        }),
    ),
)
with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
    wf_apps = session.execute(
        sqlalchemy.select(WorkflowApp)
        .where(WorkflowApp.name == "nf-core/mag")
    ).scalars().all()
    if wf_apps:
        for wf_app in wf_apps:
            print(wf_app)
    else:
        session.add(default_wf_app)





# Scan registry
# Look for new versions of repo or all repos
# Run tests
