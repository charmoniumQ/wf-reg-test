import upath
import pandas
import numpy
import warnings
from typing import Iterable, Optional, Mapping

import pandas
import numpy
import matplotlib  # type: ignore
import matplotlib.pyplot  # type: ignore

from .util import map_keys, drop_keys, fs_escape, chunk
from .data_utils import rand_color, plot_kde
from .serialization import deserialize


def get_data() -> pandas.DataFrame:
    hub = deserialize(upath.UPath("data"))
    df = pandas.DataFrame.from_records(
        [
            {
                ("registry", "id"): registry_id,
                **map_keys(lambda key: ("registry", key), drop_keys(registry.__dict__, {"workflows"})),
                ("revision", "id"): revision_id,
                **map_keys(lambda key: ("wf_app", key), drop_keys(wf_app.__dict__, {"revisions", "registry"})),
                **map_keys(lambda key: ("revision", key), drop_keys(revision.__dict__, {"executions", "workflow_app"})),
                **map_keys(lambda key: ("execution", key), drop_keys(execution.__dict__, {"revision", "condition", "resources"})),
                **map_keys(lambda key: ("condition", key), drop_keys(execution.condition.__dict__, {"revision"})),
                **map_keys(lambda key: ("resources", key), drop_keys(execution.resources.__dict__, {"revision"})),
            }
            for registry_id, registry in enumerate(hub.registries)
            for wf_app_id, wf_app in enumerate(registry.workflows)
            for revision_id, revision in enumerate(wf_app.revisions)
            for execution in revision.executions
        ],
    )
    print(df.columns)
    print(df.dtypes)
    df.columns = pandas.MultiIndex.from_tuples(df.columns)
    df["execution", "success"] = df["execution", "status_code"] == 0
    df["resources", "system_cpu_time"] = df["resources", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
    df["resources", "user_cpu_time"] = df["resources", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
    df["resources", "wall_time"] = df["resources", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
    df["execution", "total_cpu_time"] = df["execution", "system_cpu_time"] + df["execution", "user_cpu_time"]
    df["execution", "staleness"] = (df["revision", "datetime"] - df["execution", "datetime"])
    return df


def filter_plentiful_data(df: pandas.DataFrame, min_n_revisions: int) -> pandas.DataFrame:
    return df[
        df[[("wf_app", "id"), ("revision", "id")]]
        .drop_duplicates()
        .groupby(("wf_app", "id"))
        .aggregate(len)
        [("revision", "id")]
        > min_n_revisions
    ]


def plot_time(df: pandas.DataFrame, chunk_size: int) -> Iterable[matplotlib.figure.Figure]:
    for time in ["total_cpu_time", "wall_time"]:
        for wf_app_ids in chunk(sorted(df["wf_app", "id"].unique()), chunk_size):
            fig = matplotlib.pyplot.figure()
            ax = fig.add_subplot(1, 1, 1)
            max_time = max(
                numpy.percentile(df[df["wf_app", "id"] == wf_app_id], 90)
                for wf_app_id in wf_app_ids
            )
            times = numpy.linspace(0, max_time, 50)
            for i, wf_app_id in enumerate(wf_app_ids):
                dist = df[df["wf_app", "id"] == wf_app_id]["resources", time]
                plot_kde(
                    ax,
                    times / numpy.timedelta64(1, "s"),
                    dist,
                    rug=True,
                    label=str(wf_app_id),
                    color=rand_color(i, chunk_size),
                )
            ax.legend()
            ax.set_xlabel(f"{time.capitalize().replace('_', ' ')} in sec")
            ax.set_ylabel("Probability density")
            ax.set_title(f"{time} of {', '.join(map(str, wf_app_ids))}")
        yield fig


def get_counts(df: pandas.DataFrame) -> Mapping[str, int]:
    return {
        "n_workflows": df["wf_app", "id"].nunique(),
        "n_revisions": df["execution", "id"].nunique(),
        "n_executions": len(df),
        "n_successful_executions": df[df["execution", "id"]]["success"].sum(),
    }


def remove_min_outliers(df: pandas.DataFrame, cutoff: numpy.timedelta64) -> tuple[pandas.DataFrame, Optional[str]]:
    bad_mask = (df["resources", "total_cpu_time"] <= cutoff) | (df["resources", "wall_time"] <= cutoff)
    if bad_mask.any():
        bad_df = df[bad_mask]
        df = df[~bad_mask]
        message = f"{sum(bad_mask)} implausibly fast executions: executions {bad_df['execution', 'id']}, workflows {bad_df['workflow', 'id']}"
    else:
        message = None
    return df, message


def post_process() -> None:
    df = get_data()
    print(get_counts(df))
    print(df.dtypes)
    df, message = remove_min_outliers(df, numpy.timedelta64(200, "ms"))
    if message:
        warnings.warn(message)
    # for fig in plot_time(df):
    #     fig.savefig(Path("output") / (fs_escape(fig.get_title()) + ".png"))
    df = filter_plentiful_data(df, 2)
    print(get_counts(df))
    # for fig in plot_time(df):
    #     fig.savefig(Path("output") / ("filtered_" + fs_escape(fig.get_title()) + ".png"))
