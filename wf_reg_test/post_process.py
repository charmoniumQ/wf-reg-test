import pickle
import warnings
import textwrap
import shutil
import pathlib
from typing import Iterable, Optional, Mapping

import charmonium.time_block as ch_time_block
import pandas
import upath
import pandas
import numpy
import seaborn  # type: ignore
import matplotlib  # type: ignore
import matplotlib.pyplot  # type: ignore

from .util import map_keys, drop_keys, fs_escape, chunk, invert_dict
from .data_utils import rand_color, plot_kde
from .serialization import deserialize
from .config import data_path, index_path, cache_path
from .workflows import RegistryHub
from .high_level_errors import classify


generated_path = cache_path / "generated"


# TODO: move this stuff into report.
# Also figure out how to generate reports without redoing everything.


@ch_time_block.decor()
def get_hub() -> RegistryHub:
    hub_path = cache_path / "hub.pkl"
    if not hub_path.exists():
        hub_path.write_bytes(pickle.dumps(deserialize(index_path)))
    return pickle.loads(hub_path.read_bytes())


@ch_time_block.decor()
def to_pandas(hub: RegistryHub) -> pandas.DataFrame:
    df = pandas.DataFrame.from_records(
        [
            {
                # Try to only put attributes you will actually use
                # Otherwise, this df really wide.
                "registry": registry.display_name.replace("snakemake-workflow-catalog", "smk-wf-cat"),
                "workflow": workflow.display_name,
                "revision": revision.display_name,
                "date_published": revision.datetime,
                "staleness": revision.datetime - execution.datetime,
                "success": execution.status_code == 0,
                "cpu_time": execution.resources.system_cpu_time + execution.resources.user_cpu_time,
                "wall_time": execution.resources.wall_time,
                "parseable": execution.workflow_error is not None,
                "error": classify(execution.workflow_error).class_ if execution.status_code != 0 else None,
            }
            for registry in hub.registries
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ],
    )
    df["registry"] = pandas.Categorical(df["registry"])
    df["workflow"] = pandas.Categorical(df["workflow"])
    df["revision"] = pandas.Categorical(df["revision"])
    df["error"] = pandas.Categorical(df["error"])
    return df


@ch_time_block.decor()
def successful_table(df: pandas.DataFrame) -> str:
    nf_mask = df["registry"] == "nf-core"
    sm_mask = df["registry"] == "smk-wf-cat"
    def do_three_times(func):
        return  " & ".join(map(str, ["", func(df), func(df[nf_mask]), func(df[sm_mask])]))
    pathlib.Path(generated_path / "summary_table.tex").write_text("\n".join([
        r"\begin{tabular}{p{1.7in}ccc}",
        textwrap.indent(" \\\\\n".join([
            r"Quantity & Total & nf-core & smk-wf-cat",
            r"\midrule \# workflows" + do_three_times(lambda df: df["workflow"].nunique()),
            fr"\# revision" + do_three_times(lambda df: len(df)),
            fr"\% of revisions with no crash" + do_three_times(lambda df: "{:.0f}".format(df["success"].sum() / len(df) * 100)),
            fr"\% of workflows with any non-crashing revision" + do_three_times(lambda df: "{:.0f}".format(df[df["success"]]["workflow"].nunique() / df["workflow"].nunique() * 100)),
        ]), prefix="    "),
        r"\end{tabular}",
    ]))
    error_classes = df["error"].value_counts().index
    translate_error = {
        "missing input": "Missing input",
        "experiment error": "Experiment error",
        "timeout": "Timeout reached",
        "missing dep": "Missing dependency",
        "network resource changed": "Network resource changed",
        "unclassified": "Unclassified reason",
        "workflow script error": "Other (workflow script)",
        "workflow step error": "Other (containerized task)",
    }
    pathlib.Path(generated_path / "crash_table.tex").write_text("\n".join([
        r"\begin{tabular}{p{1.7in}ccc}",
        textwrap.indent("\n".join([
            r"Cause of crash & all crashes & nf crashes & smk crashes \\",
            r"\midrule",
            *[
                translate_error.get(error, error) + do_three_times(lambda df: "{:.0f}\%".format(sum(df["error"] == error) / sum(~df["error"].isna()) * 100)) + r" \\"
                for error in error_classes
            ],
        ]), prefix="    "),
        r"\midrule Total & 100\% & 100\% & 100\% \\",
        r"\end{tabular}",
    ]))


@ch_time_block.decor()
def distribution_figure(df: pandas.DataFrame) -> str:
    data_by_workflow = (
        df.groupby("workflow", as_index=False)
        .agg({"revision": lambda df: df.nunique(), "registry": lambda df: df.iloc[0], "success": lambda df: sum(df) / len(df) * 100})
        .rename(columns={
            "revision": "N Revisions",
            "success": "% Success rate",
            "registry": "Registry"
        }))
    seaborn.histplot(
        data=data_by_workflow.rename(columns={"N Revisions": "Revisions per workflow"}),
        x="Revisions per workflow",
        hue="Registry",
        element="step",
        fill=False,
        binwidth=3,
    )
    fig = matplotlib.pyplot.gcf()
    fig.set_figheight(fig.get_figheight() * 0.7)
    fig.savefig(generated_path / "revisions_per_workflow.pdf")
    matplotlib.pyplot.clf()
    matplotlib.pyplot.figure()

    seaborn.scatterplot(
        data=data_by_workflow,
        x="% Success rate",
        y="Registry",
        size="N Revisions",
        sizes=(10, 500),
        legend=False,
    )
    fig = matplotlib.pyplot.gcf()
    ax = fig.gca()
    ax.set_ylim(-0.3, 1.2)
    ax.legend(["workflow"], loc="center right")
    fig.set_figheight(fig.get_figheight() * 0.4)
    fig.subplots_adjust(left=0.2, bottom=0.35)
    fig.savefig(generated_path / "revision_success_rate.pdf")
    matplotlib.pyplot.clf()
    matplotlib.pyplot.figure()

    seaborn.histplot(
        data=(
            df
            .assign(**{"cpu_time": df["cpu_time"] / pandas.Timedelta(1, "min")})
            .rename(columns={"cpu_time": "CPU time (minutes)", "registry": "Registry"})
        ),
        x="CPU time (minutes)",
        hue="Registry",
        element="step",
        fill=False,
    )
    fig = matplotlib.pyplot.gcf()
    fig.savefig(generated_path / "cpu_time.pdf")
    matplotlib.pyplot.clf()
    matplotlib.pyplot.figure()


def time_analysis(df: pandas.DataFrame, random_seed: int) -> None:
    import pymc
    import arviz

    df = (
        df
        .assign(**{"Staleness in years": df["staleness"] / pandas.Timedelta(365, "days")})
        .rename(columns={
            "registry": "Registry",
            "success": "Success",
        })
    )

    seaborn.histplot(
        data=df,
        x="Staleness in years",
        hue="Registry",
    )
    fig = matplotlib.pyplot.gcf()
    fig.set_figheight(fig.get_figheight() * 0.7)
    ax = fig.gca()
    matplotlib.pyplot.savefig(generated_path / "staleness.pdf")
    matplotlib.pyplot.clf()
    matplotlib.pyplot.figure()

    # seaborn.scatterplot(
    #     data=df,
    #     x="staleness in years",
    #     y="success",
    #     hue="registry",
    # )
    # bin_assignments, bin_locations = pandas.cut(df["staleness in years"], retbins=True, bins=20, labels=False)
    # print(len(bin_locations), min(bin_assignments), max(bin_assignments))
    # df["success"]bin_assignments
    # seaborn.barplot(
    #     x=bins,
    #     y=counts,
    # )
    # matplotlib.pyplot.savefig("test5b.png")
    # matplotlib.pyplot.clf()

    seaborn.scatterplot(
        data=df,
        x="Staleness in years",
        y="Success",
        hue="Registry",
    )
    times = numpy.linspace(df["Staleness in years"].min(), 0, 100)
    smoothness = 1
    for registry in df["Registry"].unique():
        df2 = df[df["Registry"] == registry]
        time_contribution = numpy.exp(-smoothness * (df2["Staleness in years"].to_numpy()[numpy.newaxis, :] - times[:, numpy.newaxis])**2).sum(axis=1)
        smoothed_success = (df2["Success"].to_numpy()[numpy.newaxis, :] * numpy.exp(-smoothness * (df2["Staleness in years"].to_numpy()[numpy.newaxis, :] - times[:, numpy.newaxis])**2)).sum(axis=1) / time_contribution
        seaborn.lineplot(
            x=times,
            y=smoothed_success,
            label=f"Smoothed {registry} success",
        )
    fig = matplotlib.pyplot.gcf()
    fig.savefig(generated_path / "staleness_and_success.pdf")
    matplotlib.pyplot.clf()

    model = pymc.Model()
    with model:
        p_0 = pymc.Uniform("p_0", 0, 1)
        r = pymc.Uniform("r", 0, 1)
        t = df["Staleness in years"]
        p_t = pymc.Bernoulli("p_t", p=p_0 * r**-t, observed=df["Success"])
        pymc.model_to_graphviz(model).render(engine="dot", format="pdf", filename=generated_path / "model")

        idata = pymc.sample(2000, random_seed=random_seed)
        pymc.sample_posterior_predictive(idata, extend_inferencedata=True, random_seed=random_seed)
        seaborn.scatterplot(
            data=df,
            x="Staleness in years",
            y="Success",
        )
        ax = matplotlib.pyplot.gca()
        samples = 20
        for p_0_draw, r_draw in zip(idata.posterior["p_0"][-1][-samples:], idata.posterior["r"][-1][-samples:]):
            ax.plot(times, float(p_0_draw) * float(r_draw)**-times, color="blue", alpha=0.3)
        # posterior_p_t = idata.posterior["p_0"] * idata.posterior["r"] ** -t
        # ax.plot(t, posterior_p_t.mean(("chain", "draw")), label="Mean")
        # arviz.plot_hdi(t, idata.posterior_predictive["p_t"], hdi_prob=0.8)
        fig = matplotlib.pyplot.gcf()
        fig.savefig(generated_path / "posterior_distribution_success_and_staleness.pdf")
        matplotlib.pyplot.clf()

        seaborn.kdeplot(
            x=idata.posterior["p_0"][-1],
        )
        fig = matplotlib.pyplot.gcf()
        fig.savefig(generated_path / "p_0.pdf")
        matplotlib.pyplot.clf()

        seaborn.kdeplot(
            x=idata.posterior["r"][-1],
        )
        fig = matplotlib.pyplot.gcf()
        fig.savefig(generated_path / "r.pdf")
        matplotlib.pyplot.clf()


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


def remove_min_outliers(df: pandas.DataFrame, cutoff: numpy.timedelta64) -> tuple[pandas.DataFrame, Optional[str]]:
    bad_mask = (df["resources", "total_cpu_time"] <= cutoff) | (df["resources", "wall_time"] <= cutoff)
    if bad_mask.any():
        bad_df = df[bad_mask]
        df = df[~bad_mask]
        message = f"{sum(bad_mask)} implausibly fast executions: executions {bad_df['execution', 'id']}, workflows {bad_df['workflow', 'id']}"
    else:
        message = None
    return df, message


@ch_time_block.decor()
def post_process(random_seed: int = 0) -> None:
    # TODO: make this local to this function
    seaborn.set_theme()
    if generated_path.exists():
        shutil.rmtree(generated_path)
    generated_path.mkdir()
    hub = get_hub()
    df = to_pandas(hub)
    print(df.dtypes)
    successful_table(df)
    distribution_figure(df)
    time_analysis(df, random_seed)
    return df
