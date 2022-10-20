import itertools
from datetime import datetime, timedelta
from typing import Callable, Mapping, cast

import domonic as html  # type: ignore

from .html_helpers import (
    collapsed,
    css_rule,
    html_emoji_bool,
    html_link,
    html_table,
)
from .util import sorted_and_dropped, groupby_dict
from .workflows2 import WorkflowApp2 as WorkflowApp


def is_interesting(wf_app: WorkflowApp) -> bool:
    return sum(bool(revision.executions) for revision in wf_app.revisions) > 3


def get_stats(all_wf_apps: list[WorkflowApp]) -> html.Element:
    engine2wf_apps = groupby_dict(all_wf_apps, lambda wf_app: wf_app.workflow_engine_name)
    stats: Mapping[str, Callable[[list[WorkflowApp]], int]] = {
        "N workflows": lambda wf_apps: len(wf_apps),
        "N revisions": lambda wf_apps: sum(len(wf_app.revisions) for wf_app in wf_apps),
        "N executions": lambda wf_apps: sum(
            len(revision.executions)
            for wf_app in wf_apps
            for revision in wf_app.revisions
        ),
        "N interesting workflows": lambda wf_apps: sum(
            1 for wf_app in wf_apps if is_interesting(wf_app)
        ),
        "N revisions of interesting workflows": lambda wf_apps: sum(
            len(wf_app.revisions) for wf_app in wf_apps if is_interesting(wf_app)
        ),
        "N executions of interesting workflows": lambda wf_apps: sum(
            len(revision.executions)
            for wf_app in wf_apps
            if is_interesting(wf_app)
            for revision in wf_app.revisions
        ),
    }
    engines = engine2wf_apps.keys()
    return html_table(
        [
            {
                "Stat": stat_name,
                "Total": str(stat_func(all_wf_apps)),
                **{
                    engine: str(stat_func(engine2wf_apps[engine])) for engine in engines
                },
            }
            for stat_name, stat_func in stats.items()
        ]
    )


def html_date(dt: datetime) -> html.Element:
    return dt.strftime("%Y-%m-%d")


def html_timedelta(td: timedelta, unit: str, digits: int) -> html.Element:
    day_diff = td.total_seconds() / timedelta(**{unit: 1}).total_seconds()
    return f"{day_diff:.{digits}f} {unit}"


def report_html(wf_apps: list[WorkflowApp]) -> str:
    table_by_workflows = html_table(
        [
            {
                "Workflow": html_link(wf_app.display_name, wf_app.url),
                "Engine": wf_app.workflow_engine_name,
                "Repo": html_link("repo", wf_app.repo_url),
                "Interesting?": html_emoji_bool(is_interesting(wf_app)),
                "Revisions": collapsed(
                    "Revisions",
                    html_table(
                        [
                            {
                                "Revision": html_link(
                                    revision.display_name, revision.url
                                ),
                                "Date/time": html_date(revision.datetime),
                                "Executions": html_table(
                                    [
                                        {
                                            "Date/time": html_date(execution.datetime),
                                            "Success": html_emoji_bool(
                                                execution.status_code == 0
                                            ),
                                            "Max RAM": f"{execution.max_rss / 2**10:.0f}KiB",
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
    )
    table_by_executions = html_table(
        sorted_and_dropped(
            [
                (
                    execution.datetime - revision.datetime,
                    {
                        "Workflow": html_link(wf_app.display_name, wf_app.url),
                        "Engine": wf_app.workflow_engine_name,
                        "Revision": html_link(revision.display_name, revision.url),
                        "Revision date": html_date(revision.datetime),
                        "Staleness": html_timedelta(
                            execution.datetime - revision.datetime,
                            unit="days",
                            digits=0,
                        ),
                        "Success": html_emoji_bool(execution.status_code == 0),
                        "Max RAM": f"{execution.max_rss / 2**10:.0f}KiB",
                        "CPU Time": html_timedelta(
                            execution.user_cpu_time + execution.system_cpu_time,
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
    )
    return cast(
        str,
        html.html(
            html.head(
                html.meta(_charset="utf-8"),
                html.meta(
                    _http_equiv="Content-Type", _content="text/html; charset=utf-8"
                ),
                html.title("Workflow Registry Test results"),
                html.style(
                    "\n".join(
                        [
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
                        ]
                    )
                ),
            ),
            html.body(
                html.h1("Stats"),
                get_stats(wf_apps),
                html.h1("Workflows"),
                table_by_workflows,
                html.h1("Executions"),
                table_by_executions,
            ),
        ).__format__(""),
    )


# TODO: put execution resource statistics
