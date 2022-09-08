import json
from pathlib import Path

import sqlalchemy
import sqlalchemy_schemadisplay  # type: ignore
import domonic as html

from .html_helpers import html_emoji_bool, html_link, html_table, css_rule
from .workflows import Base, Repo, WorkflowApp

path = Path("test.sqlite")
if path.exists():
    path.unlink()
engine = sqlalchemy.create_engine(f"sqlite:///{path}", future=True)


graph = sqlalchemy_schemadisplay.create_schema_graph(
    metadata=Base.metadata,
    show_datatypes=False,
    show_indexes=False,
    rankdir="LR",
    concentrate=True,
)
graph.write_png("dbschema.png")
Base.metadata.create_all(engine)


default_wf_app = WorkflowApp(
    workflow_engine_name="nextflow",
    url="https://nf-co.re/mag",
    name="nf-core/mag",
    repo=Repo(
        type="GitHubRepo",
        kwargs=json.dumps({"user": "nf-core", "repo": "mag", "only_tags": True}),
    ),
)
with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
    session.add(default_wf_app)


def render(elem: html.Element) -> str:
    return elem.__format__("")


with sqlalchemy.orm.Session(engine, future=True) as session, session.begin():
    Path("build/results.html").write_text(
        render(
            html.html(
                html.style(
                    css_rule(
                        "table, td",
                        {
                            "padding": "10px",
                            "border": "1px solid black",
                            "border-collapse": "collapse",
                        },
                    ),
                    css_rule(
                        "thead",
                        {
                            "font-weight": "bold",
                            "background-color": "lightgray",
                        },
                    ),
                ),
                html.body(
                    html_table(
                        [
                            {
                                "Workflow": html_link(wf_app.name, wf_app.url),
                                "Repo": html_link(
                                    wf_app.repo.parse().name, wf_app.repo.parse().url
                                ),
                                "Revisions": html_table(
                                    [
                                        {
                                            "Revision": html_link(
                                                revision.name, revision.url
                                            ),
                                            "Date/time": revision.datetime.isoformat(),
                                            "Executions": html_table(
                                                [
                                                    {
                                                        "Date/time": execution.datetime.isoformat(),
                                                        "Success": html_emoji_bool(
                                                            execution.success
                                                        ),
                                                        "Output Hash": html.code(
                                                            "{execution.output.hash:016x}"
                                                        ),
                                                    }
                                                    for execution in revision.executions
                                                ]
                                            ),
                                        }
                                        for revision in wf_app.repo.revisions
                                    ]
                                ),
                            }
                            for wf_app in session.execute(
                                sqlalchemy.select(WorkflowApp)
                            )
                            .scalars()
                            .all()
                        ]
                    )
                )
            )
        )
    )


# Scan registry
# Look for new versions of repo or all repos
# Run tests
