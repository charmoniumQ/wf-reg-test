import collections
import itertools
import io
import pathlib
import base64
import urllib
import yaml
from datetime import datetime, timedelta
from typing import Callable, Mapping, cast, Union, Optional

import matplotlib  # type: ignore
import domonic as html  # type: ignore
import upath

from .html_helpers import (
    collapsed,
    css_rule,
    heading,
    html_emoji_bool,
    html_link,
    html_table,
    html_list,
)
from .util import sorted_and_dropped, groupby_dict, upath_to_url
from .workflows import Workflow, RegistryHub, Execution


def is_interesting(workflow: Workflow) -> bool:
    return sum(bool(revision.executions) for revision in workflow.revisions) > 3


def get_stats(hub: RegistryHub) -> html.Element:
    engine2workflows = groupby_dict(hub.workflows, lambda workflow: workflow.engine)
    stats: Mapping[str, Callable[[list[Workflow]], Union[str, int]]] = {
        "N workflows": lambda workflows: len(workflows),
        "revisions / workflows": lambda workflows: "{:.1f}".format(
            sum(len(workflow.revisions) for workflow in workflows)
            / len(workflows)
        ),
        "N revisions": lambda workflows: sum(len(workflow.revisions) for workflow in workflows),
        "executions / revision": lambda workflows: "{:.0f}%".format(
            100*
            sum(
                len(revision.executions)
                for workflow in workflows
                for revision in workflow.revisions
            )
            / sum(len(workflow.revisions) for workflow in workflows)
        ),
        "N executions": lambda workflows: sum(
            len(revision.executions)
            for workflow in workflows
            for revision in workflow.revisions
        ),
        "working executions / executions": lambda workflows: "{:.0f}%".format(
            100
            * sum(
                execution.successful
                for workflow in workflows
                for revision in workflow.revisions
                for execution in revision.executions
            )
            / sum(
                len(revision.executions)
                for workflow in workflows
                for revision in workflow.revisions
            )
        ),
        "N working executions": lambda workflows: sum(
            execution.successful
            for workflow in workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ),
        "error executions / executions": lambda workflows: "{:.0f}%".format(
            100
            * sum(
                not execution.successful
                for workflow in workflows
                for revision in workflow.revisions
                for execution in revision.executions
            )
            / sum(
                len(revision.executions)
                for workflow in workflows
                for revision in workflow.revisions
            )
        ),
        "N error executions": lambda workflows: sum(
            not execution.successful
            for workflow in workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ),
        "classified error executions / error executions": lambda workflows: "{:.0f}%".format(
            100
            * sum(
                (not execution.successful) and execution.workflow_error is not None
                for workflow in workflows
                for revision in workflow.revisions
                for execution in revision.executions
            )
            / sum(
                not execution.successful
                for workflow in workflows
                for revision in workflow.revisions
                for execution in revision.executions
            )
        ),
        "N classified error executions": lambda workflows: sum(
            (not execution.successful) and execution.workflow_error is not None
            for workflow in workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ),
        # "N interesting workflows": lambda workflows: sum(
        #     1 for workflow in workflows if is_interesting(workflow)
        # ),
        # "N revisions of interesting workflows": lambda workflows: sum(
        #     len(workflow.revisions) for workflow in workflows if is_interesting(workflow)
        # ),
        # "N executions of interesting workflows": lambda workflows: sum(
        #     len(revision.executions)
        #     for workflow in workflows
        #     if is_interesting(workflow)
        #     for revision in workflow.revisions
        # ),
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


def html_datetime(dt: datetime) -> html.Element:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


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
                                            "Max RAM": f"{execution.resources.max_rss / 2**30:.3f}GiB",
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
                                            "Machine": execution.machine.short_description if execution.machine else "",
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
                        "Workflow": html.span(html_link(workflow.display_name, workflow.url), id=str(id(execution))),
                        "Revision": html_link(revision.display_name, revision.url),
                        "Engine": workflow.engine,
                        "Staleness": html_timedelta(
                            execution.datetime - revision.datetime,
                            unit="days",
                            digits=0,
                        ),
                        # "Revision date": html_date(revision.datetime),
                        "Execution date": html_datetime(execution.datetime),
                        "Success": (
                            html_emoji_bool(True)
                            if execution.successful else
                            html.div(
                                html.p(html_emoji_bool(False)),
                                html.p(
                                    "unknown error"
                                    if execution.workflow_error is None else
                                    collapsed(
                                        "show error",
                                        html.code(
                                            html.pre(
                                                yaml.dump(
                                                    execution.workflow_error, default_flow_style=False,
                                                )
                                            )
                                        )
                                    )
                                ),
                            )
                        ),
                        "Logs": html_link(
                            "empty" if execution.logs.empty else f"{execution.logs.size / 2**30:.3f}GiB",
                            upath_to_url(execution.logs.url),
                        ),
                        "Outputs": html_link(
                            "empty" if execution.outputs.empty else f"{execution.outputs.size / 2**30:.3f}GiB",
                            upath_to_url(execution.outputs.url),
                        ),
                        "Max RAM": f"{execution.resources.max_rss / 2**30:.3f}GiB",
                        "CPU Time": html_timedelta(
                            execution.resources.user_cpu_time + execution.resources.system_cpu_time,
                            unit="seconds",
                            digits=1,
                        ),
                        "Wall Time": html_timedelta(
                            execution.resources.wall_time, unit="seconds", digits=1
                        ),
                        # "Machine": execution.machine.short_description if execution.machine else "",
                        # "Reproducible": html_emoji_bool(True),
                    },
                )
                for registry in hub.registries
                for workflow in registry.workflows
                for revision in workflow.revisions
                if revision.executions
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
                heading("Stats", level=1, anchor=True),
                get_stats(hub),
                heading("Errors", level=1, anchor=True),
                get_errors(hub),
                html.h1("Workflows"),
                table_by_workflows,
                heading("Executions", level=1, anchor=True),
                table_by_executions,
            ),
        ).__format__("").replace("<!DOCTYPE html>\n", ""),
    )


# TODO: put execution resource statistics


def fig_to_html(figure: matplotlib.figure.Figure) -> html.Element:
    buf = io.BytesIO()
    figure.savefig(buf, format='png')
    return html.img(src="data:image/png;base64," + base64.b64encode(buf.getvalue()).decode('utf-8'))

def get_errors(hub: RegistryHub) -> html.Element:
    failed_executions = hub.failed_executions
    def get_kind(execution: Execution) -> str:
        workflow_error = execution.workflow_error
        return workflow_error.kind if workflow_error is not None else "unknown"
    kind_to_exemplars = groupby_dict(failed_executions, get_kind)
    counter = collections.Counter([get_kind(execution) for execution in failed_executions])
    return html.div(
        html_table(
            [
                {
                    "Error": html.code(kind),
                    "Count": html.span(str(count)),
                    "Fraction of all errors": html.span("{:.0f}%".format((count / len(failed_executions)) * 100)),
                    "Instances": collapsed(
                        "See individual instances",
                        html_list(
                            html_link(str(execution), "#" + str(id(execution)))
                            for execution in kind_to_exemplars[kind]
                        ),
                    ),
                }
                for (kind, count) in counter.most_common()
            ],
        ),
    )
