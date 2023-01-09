# import upath
# import pandas
# import numpy
# import warnings
# from typing import Iterable, Optional

# from .util import map_keys, drop_keys, fs_escape
# from .serialization import deserialize


# def get_data() -> pandas.DataFrame:
#     hub = deserialize(upath.UPath("data"))
#     df = pandas.DataFrame.from_records(
#         [
#             {
#                 ("registry", "id"): registry_id,
#                 **map_keys(lambda key: (key, "registry"), drop_keys(registry.__dict__, {"workflows"})),
#                 ("revision", "id"): revision_id,
#                 **map_keys(lambda key: (key, "wf_app"), drop_keys(wf_app.__dict__, {"revisions", "registry"})),
#                 **map_keys(lambda key: (key, "revision"), drop_keys(revision.__dict__, {"executions", "workflow_app"})),
#                 **map_keys(lambda key: (key, "execution"), drop_keys(execution.__dict__, {"revision", "condition", "resources"})),
#                 **map_keys(lambda key: (key, "condition"), drop_keys(execution.condition.__dict__, {"revision"})),
#                 **map_keys(lambda key: (key, "resources"), drop_keys(execution.resources.__dict__, {"revision"})),
#             }
#             for registry_id, registry in enumerate(hub.registries)
#             for wf_app_id, wf_app in enumerate(registry.wf_apps)
#             for revision_id, revision in enumerate(wf_app.revisions)
#             for execution in revision.executions
#         ],
#     )
#     df.columns = pandas.MultiIndex.from_tuples(df.columns)
#     df["execution", "success"] = df["execution", "status_code"] == 0
#     df["execution", "system_cpu_time"] = df["execution", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
#     df["execution", "user_cpu_time"] = df["execution", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
#     df["execution", "wall_time"] = df["execution", "system_cpu_time"] * numpy.timedelta64(1, 'ns')
#     df["execution", "total_cpu_time"] = df["execution", "system_cpu_time"] + df["execution", "user_cpu_time"]
#     df["execution", "staleness"] = (df["revision", "datetime"] - df["execution", "datetime"])
#     return df


# def filter_plentiful_data(df: pandas.DataFrame, min_n_revisions: int) -> pandas.DataFrame:
#     return df[
#         df[[("wf_app", "id"), ("revision", "id")]]
#         .drop_duplicates()
#         .groupby(("wf_app", "id"))
#         .aggregate(len)
#         [("revision", "id")]
#         > min_number_of_revisions
#     ]


# def plot_time(df: pandas.DataFrame, chunk_size: int) -> Iterable[matplotlib.figure.Figure]:
#     for time in ["total_cpu_time", "wall_time"]:
#         for wf_app_ids in chunk(sorted(df["wf_app", "id"].unique()), chunk_size):
#             fig = plt.figure()
#             ax = fig.gca()
#             max_time = max(
#                 numpy.percentile(80, df[df["wf_app", "id"] == wf_app_id])
#                 for wf_app_id in wf_app_idsx
#             )
#             times = numpy.linspace(0, max_time, 50)
#             for i, wf_app_id in enumerate(wf_app_ids):
#                 dist = df[df["wf_app", "id"] == wf_app_id]["resources", time]
#                 plot_kde(
#                     ax,
#                     times / numpy.timedelta(1, "s"),
#                     dist,
#                     rug=True,
#                     label=str(wf_app_id),
#                     color=rand_color(i, chunk_size),
#                 )
#             ax.legend()
#             ax.set_xlabel(f"{time.capitalize().replace('_', ' ')} in sec")
#             ax.set_ylabel("Probability density")
#             ax.set_title(f"{time} of {', '.join(map(str, wf_app_ids))}")
#         yield fig


# def get_counts(df: pandas.DataFrame) -> Mapping[str, int]:
#     return {
#         "n_workflows": df["wf_app", "id"].nunique(),
#         "n_revisions": df["execution", "id"].nunique(),
#         "n_executions": len(df),
#         "n_successful_executions": df[df["execution", "id"]]["success"].sum(),
#     }


# def remove_min_outliers(df: pandas.DataFrame, cutoff: numpy.Timedelta) -> tuple[pandas.DataFrame, Optional[str]]:
#     bad_mask = (df[("execution", "total_cpu_time")] <= cutoff) | (df[("execution", "wall_time")] <= cutoff)
#     if bad_mask.any():
#         bad_df = df[bad_mask]
#         df = df[~bad_mask]
#         message = f"{sum(bad_mask)} implausibly fast executions: executions {bad_df['execution', 'id']}, workflows {bad_df['workflow', 'id']}"
#     else:
#         message = None
#     return df, message


# def post_process() -> None:
#     df = get_data()
#     print(get_counts(df))
#     print(df.dtypes)
#     df, message = get_min_outliers(df, numpy.timedelta(0.5, "s"))
#     if message:
#         warnings.warn(message)
#     for fig in plot_time(df):
#         fig.savefig(Path("output") / (fs_escape(fig.get_title()) + ".png"))
#     df = filter_data_plentiful(df)
#     print(get_counts(df))
#     for fig in plot_time(df):
#         fig.savefig(Path("output") / ("filtered_" + fs_escape(fig.get_title()) + ".png"))
