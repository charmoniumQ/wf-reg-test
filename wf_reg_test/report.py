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
from .workflows import Workflow, RegistryHub


def is_interesting(workflow: Workflow) -> bool:
    return sum(bool(revision.executions) for revision in workflow.revisions) > 3


def get_stats(hub: RegistryHub) -> html.Element:
    engine2workflows = groupby_dict(hub.workflows, lambda workflow: workflow.engine)
    stats: Mapping[str, Callable[[list[Workflow]], int]] = {
        "N workflows": lambda workflows: len(workflows),
        "N revisions": lambda workflows: sum(len(workflow.revisions) for workflow in workflows),
        "N executions": lambda workflows: sum(
            len(revision.executions)
            for workflow in workflows
            for revision in workflow.revisions
        ),
        "N interesting workflows": lambda workflows: sum(
            1 for workflow in workflows if is_interesting(workflow)
        ),
        "N revisions of interesting workflows": lambda workflows: sum(
            len(workflow.revisions) for workflow in workflows if is_interesting(workflow)
        ),
        "N executions of interesting workflows": lambda workflows: sum(
            len(revision.executions)
            for workflow in workflows
            if is_interesting(workflow)
            for revision in workflow.revisions
        ),
    }
    engines = engine2workflows.keys()
    return html_table(
        [
            {
                "Stat": stat_name,
                "Total": str(stat_func(hub.workflows)),
                **{
                    engine: str(stat_func(engine2workflows[engine])) for engine in engines
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


def report_html(hub: RegistryHub) -> str:
    table_by_workflows = html_table(
        [
            {
                "Workflow": html_link(workflow.display_name, workflow.url),
                "Engine": workflow.engine,
                "Repo": html_link("repo", workflow.repo_url),
                "Interesting?": html_emoji_bool(is_interesting(workflow)),
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
                                            "Max RAM": f"{execution.resources.max_rss / 2**10:.0f}KiB",
                                            "CPU Time": html_timedelta(
                                                execution.resources.user_cpu_time
                                                + execution.resources.system_cpu_time,
                                                unit="seconds",
                                                digits=1,
                                            ),
                                            "Wall Time": html_timedelta(
                                                execution.resources.wall_time,
                                                unit="seconds",
                                                digits=1,
                                            ),
                                            "Machine": execution.machine.short_description,
                                        }
                                        for execution in revision.executions
                                    ]
                                ),
                            }
                            for revision in workflow.revisions
                        ]
                    ),
                ),
            }
            for workflow in hub.workflows
        ]
    )
    table_by_executions = html_table(
        sorted_and_dropped(
            [
                (
                    execution.datetime - revision.datetime,
                    {
                        "Workflow": html_link(workflow.display_name, workflow.url),
                        "Engine": workflow.engine,
                        "Revision": html_link(revision.display_name, revision.url),
                        "Revision date": html_date(revision.datetime),
                        "Staleness": html_timedelta(
                            execution.datetime - revision.datetime,
                            unit="days",
                            digits=0,
                        ),
                        "Success": html_emoji_bool(execution.status_code == 0),
                        "Max RAM": f"{execution.resources.max_rss / 2**10:.0f}KiB",
                        "CPU Time": html_timedelta(
                            execution.resources.user_cpu_time + execution.resources.system_cpu_time,
                            unit="seconds",
                            digits=1,
                        ),
                        "Wall Time": html_timedelta(
                            execution.resources.wall_time, unit="seconds", digits=1
                        ),
                        "Machine": execution.machine.short_description,
                        # "Reproducible": html_emoji_bool(True),
                    },
                )
                for registry in hub.registries
                for workflow in registry.workflows
                for revision in workflow.revisions
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
                get_stats(hub),
                html.h1("Workflows"),
                table_by_workflows,
                html.h1("Executions"),
                table_by_executions,
            ),
        ).__format__(""),
    )


# TODO: put execution resource statistics
