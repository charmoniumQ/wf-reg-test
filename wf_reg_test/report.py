from typing import Mapping, Any, Sequence, cast
import domonic as html  # type: ignore
import functools
from .html_helpers import TagLike, html_table, html_emoji_bool, html_link, css_rule
from .workflows import Execution, Revision, WorkflowApp

def wf_app_table(workflow_apps: Sequence[WorkflowApp]) -> html.Element:
    raise NotImplementedError()

def report_table(list_: list[Any]) -> html.Element:
    return html_table([
        report_table_row(item)
        for item in list_
    ])


@functools.singledispatch
def report_table_row(arg: Any) -> Mapping[str, TagLike]:
    raise TypeError("report_item(...) is not implemented for {type(arg)!s}")


@report_table_row.register
def _(execution: Execution) -> html.Element:
    return {
        "Date/time": execution.datetime.isoformat(),
        "Success": html_emoji_bool(
            execution.success
        ),
        "Output Hash": html.code(
            "{execution.output.hash:016x}"
        ),
    }


@report_table_row.register
def _(revision: Revision) -> Mapping[str, TagLike]:
    return {
        "Revision": html_link(revision.display_name, revision.url),
        "Date/time": revision.datetime.isoformat(),
        "Executions": report_table(revision.executions),
    }


@report_table_row.register
def _(wf_app: WorkflowApp) -> Mapping[str, TagLike]:
    return {
        "Workflow": html_link(wf_app.display_name, wf_app.url),
        "Repo": html_link("repo", wf_app.repo_url),
        "Revisions": report_table(wf_app.revisions),
    }


def report_html(workflow_apps: list[WorkflowApp]) -> str:
    return cast(str, html.html(
        html.head(
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
        ),
        html.body(
            report_table(workflow_apps),
        ),
    ).__format__(""))
