from datetime import datetime, timedelta
from typing import Optional, cast

import domonic as html  # type: ignore

from .html_helpers import (
    collapsed,
    css_attribute,
    css_rule,
    html_emoji_bool,
    html_link,
    html_table,
)
from .util import sorted_and_dropped
from .workflows import MerkleTreeNode, WorkflowApp


def html_mtn(node: Optional[MerkleTreeNode]) -> html.Element:
    if node is None:
        return html.span("Missing", style=css_attribute(background="red"))
    else:
        return collapsed(
            html.code(f"{node.hash + 2**63:016x}"),
            html.code(html.pre(node.list_children())),
        )


def html_date(dt: datetime) -> html.Element:
    return dt.strftime("%Y-%m-%d")


def html_timedelta(td: timedelta, unit: str, digits: int) -> html.Element:
    day_diff = td.total_seconds() / timedelta(**{unit: 1}).total_seconds()
    return f"{day_diff:.{digits}f} {unit}"


def report_html(wf_apps: list[WorkflowApp]) -> str:
    return cast(
        str,
        html.html(
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
                html.h1("Workflows"),
                html_table(
                    [
                        {
                            "Workflow": html_link(wf_app.display_name, wf_app.url),
                            "Repo": html_link("repo", wf_app.repo_url),
                            "Revisions": collapsed(
                                "Revisions",
                                html_table(
                                    [
                                        {
                                            "Revision": html_link(
                                                revision.display_name, revision.url
                                            ),
                                            "Date/time": html_date(revision.datetime),
                                            "Input Hash": html_mtn(revision.tree),
                                            "Executions": html_table(
                                                [
                                                    {
                                                        "Date/time": html_date(
                                                            execution.datetime
                                                        ),
                                                        "Output Hash": html_mtn(
                                                            execution.output
                                                        ),
                                                        "Success": html_emoji_bool(
                                                            execution.status_code == 0
                                                        ),
                                                        "Max RAM": f"{execution.max_rss / 2**30:.1f}GiB",
                                                        "CPU Time": html_timedelta(
                                                            execution.user_cpu_time
                                                            + execution.system_cpu_time,
                                                            unit="seconds",
                                                            digits=1,
                                                        ),
                                                        "Wall Time": html_timedelta(
                                                            execution.wall_time,
                                                            unit="seconds",
                                                            digits=1,
                                                        ),
                                                        "Machine": execution.machine.short_description,
                                                    }
                                                    for execution in revision.executions
                                                ]
                                            ),
                                        }
                                        for revision in wf_app.revisions
                                    ]
                                ),
                            ),
                        }
                        for wf_app in wf_apps
                    ]
                ),
                html.h1("Executions"),
                html_table(
                    sorted_and_dropped(
                        [
                            (
                                execution.datetime - revision.datetime,
                                {
                                    "Workflow": html_link(
                                        wf_app.display_name, wf_app.url
                                    ),
                                    "Revision": html_link(
                                        revision.display_name, revision.url
                                    ),
                                    "Revision date": html_date(revision.datetime),
                                    "Staleness": html_timedelta(
                                        execution.datetime - revision.datetime,
                                        unit="days",
                                        digits=0,
                                    ),
                                    "Success": html_emoji_bool(
                                        execution.status_code == 0
                                    ),
                                    "Max RAM": f"{execution.max_rss / 2**30:.1f}GiB",
                                    "CPU Time": html_timedelta(
                                        execution.user_cpu_time
                                        + execution.system_cpu_time,
                                        unit="seconds",
                                        digits=1,
                                    ),
                                    "Wall Time": html_timedelta(
                                        execution.wall_time, unit="seconds", digits=1
                                    ),
                                    "Machine": execution.machine.short_description,
                                    # "Reproducible": html_emoji_bool(True),
                                },
                            )
                            for wf_app in wf_apps
                            for revision in wf_app.revisions
                            for execution in revision.executions
                        ],
                        reverse=True,
                    )
                ),
            ),
        ).__format__(""),
    )


# TODO: put execution resource statistics
