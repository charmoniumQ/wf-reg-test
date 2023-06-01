import collections
import pickle
import warnings
import textwrap
import shutil
import pathlib
from typing import Iterable, Optional, Mapping, Any

#import charmonium.cache
import charmonium.time_block as ch_time_block
import pandas
import upath
import pandas
import numpy
import seaborn  # type: ignore
import matplotlib  # type: ignore
import matplotlib.pyplot  # type: ignore
import pymc
import tqdm
import arviz

from .util import map_keys, drop_keys, fs_escape, chunk, invert_dict, divide_or
from .data_utils import rand_color, plot_kde
from .serialization import deserialize
from .config import data_path, index_path, cache_path
from .workflows import RegistryHub
from .high_level_errors import classify


# TODO: move this stuff into report.


def to_pandas(hub: RegistryHub) -> pandas.DataFrame:
    df = pandas.DataFrame.from_records(
        [
            {
                # Try to only put attributes you will actually use
                # Otherwise, this df really wide.
                "registry": registry.display_name.replace("snakemake-workflow-catalog", "SWC"),
                "workflow": workflow.display_name,
                "revision": revision.display_name,
                "staleness": revision.datetime - execution.datetime,
                "success": execution.status_code == 0,
                "cpu_time": execution.resources.system_cpu_time + execution.resources.user_cpu_time,
                "wall_time": execution.resources.wall_time,
                "error": classify(execution.workflow_error).class_ if execution.status_code != 0 else None,
            }
            for registry in hub.registries
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ],
    )
    df["registry"] = pandas.Categorical(df["registry"], categories=["SWC", "nf-core"], ordered=True)
    df["workflow"] = pandas.Categorical(df["workflow"])
    df["revision"] = pandas.Categorical(df["revision"])
    df["error"] = pandas.Categorical(df["error"])
    return df


def summary_table(df: pandas.DataFrame) -> str:
    nf_mask = df["registry"] == "nf-core"
    sm_mask = df["registry"] == "SWC"
    def do_three_times(func):
        return  " & ".join(map(str, ["", func(df), func(df[sm_mask]), func(df[nf_mask])]))
    return "\n".join([
        r"\begin{tabular}{p{1.7in}ccc}",
        textwrap.indent(" \\\\\n".join([
            r"Quantity & Total & SWC & nf-core",
            r"\midrule \# workflows" + do_three_times(lambda df: df["workflow"].nunique()),
            fr"\# revisions" + do_three_times(lambda df: len(df)),
            fr"\% of revisions with no crash" + do_three_times(lambda df: "{:.0f}\%".format(df["success"].sum() / len(df) * 100)),
            fr"\% of workflows with at least one non-crashing revision" + do_three_times(lambda df: "{:.0f}\%".format(df[df["success"]]["workflow"].nunique() / df["workflow"].nunique() * 100)),
        ]), prefix="    "),
        r"\end{tabular}",
    ])


def crash_table(df: pandas.DataFrame) -> str:
    nf_mask = df["registry"] == "nf-core"
    sm_mask = df["registry"] == "SWC"
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
    def do_three_times(func):
        return  " & ".join(map(str, ["", func(df), func(df[sm_mask]), func(df[nf_mask])]))
    return "\n".join([
        r"\begin{tabular}{p{1.7in}ccc}",
        textwrap.indent("\n".join([
            r"Kind of crash & all & SWC & nf-core \\",
            r"\midrule",
            *[
                translate_error.get(error, error) + do_three_times(lambda df: "{:.1f}\%".format(sum(df["error"] == error) / len(df) * 100)) + r" \\"
                for error in error_classes
                if sum(df["error"] == error)
            ],
        ]), prefix="    "),
        r"    \midrule No crash" + do_three_times(lambda df: "{:.1f}\%".format(sum(df["error"].isna()) / len(df) * 100)) + r" \\",
        r"    \midrule Total & 100\% & 100\% & 100\% \\"
        r"\end{tabular}",
    ])


def revisions_per_workflow(data_by_workflow: pandas.DataFrame) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    ax = fig.subplots()
    print(data_by_workflow["registry"].cat.categories)
    print(data_by_workflow["registry"].cat.ordered)
    seaborn.histplot(
        data=data_by_workflow.rename(columns={
            "revision": "Revisions per workflow",
            "success": "% Success rate",
            "registry": "Registry"
        }),
        x="Revisions per workflow",
        hue="Registry",
        element="step",
        stat="percent",
        cumulative=True,
        fill=False,
        discrete=True,
        ax=ax,
    )
    fig.set_figheight(fig.get_figheight() * 0.7)
    fig.subplots_adjust(bottom=0.2)
    return fig


def revision_success_rate(data_by_workflow: pandas.DataFrame) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    ax = fig.subplots()
    seaborn.scatterplot(
        data=data_by_workflow.rename(columns={
            "revision": "N Revisions",
            "success": "% Success rate",
            "registry": "Registry"
        }),
        x="% Success rate",
        y="Registry",
        size="N Revisions",
        sizes=(10, 500),
        legend=False,
        ax=ax,
    )
    ax.set_ylim(-0.3, 1.2)
    fig.set_figheight(fig.get_figheight() * 0.4)
    fig.subplots_adjust(left=0.2, bottom=0.35)
    return fig


def cpu_time(df: pandas.DataFrame) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    fig.set_figheight(fig.get_figheight() * 0.7)
    ax = fig.subplots()
    seaborn.histplot(
        data=(
            df
            .assign(**{"cpu_time": df["cpu_time"] / pandas.Timedelta(1, "min")})
            .rename(columns={"cpu_time": "CPU time (minutes)", "registry": "Registry"})
        ),
        x="CPU time (minutes)",
        hue="Registry",
        stat="percent",
        cumulative=True,
        element="step",
        fill=False,
        ax=ax,
    )
    fig.subplots_adjust(bottom=0.2)
    return fig


def staleness(df: pandas.DataFrame) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    ax = fig.subplots()
    seaborn.histplot(
        data=(
            df
            .assign(**{"Staleness in years": df["staleness"] / pandas.Timedelta(365, "days")})
            .rename(columns={
                "registry": "Registry",
                "success": "Success",
            })
        ),
        x="Staleness in years",
        hue="Registry",
        stat="percent",
        cumulative=True,
        element="step",
        fill=False,
        ax=ax,
    )
    fig.set_figheight(fig.get_figheight() * 0.7)
    fig.subplots_adjust(bottom=0.2)
    return fig


def smoothed_success_and_staleness(df: pandas.DataFrame) -> matplotlib.figure.Figure:
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
    fig = matplotlib.figure.Figure()
    ax = fig.add_subplots()
    seaborn.scatterplot(
        data=df.assign(**{
            "Staleness in years": df["staleness"] / pandas.Timedelta(365, "days"),
            "success": "Success",
            "registry": "Registry"
        }),
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
    return fig


def pymc_model(df: pandas.DataFrame) -> pymc.Model:
    model = pymc.Model()
    with model:
        p_0 = pymc.Uniform("p_0", 0, 1)
        r = pymc.Uniform("r", 0, 1)
        t = df["staleness"] / pandas.Timedelta(365, "days")
        p_t = pymc.Bernoulli("p_t", p=p_0 * r**-t, observed=df["success"])
        return model


def pymc_sample(model: pymc.Model, random_seed: int) -> Any:
    with model:
        return pymc.sample(2000, random_seed=random_seed)


def posterior_success_and_staleness(df: pandas.DataFrame, idata: Any) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    ax = fig.subplots()
    df = df.assign(**{
        "Staleness in years": df["staleness"] / pandas.Timedelta(365, "days"),
    }).rename(columns={
        "success": "Success",
        "registry": "Registry"
    })
    times = numpy.linspace(df["Staleness in years"].min(), 0, 100)
    seaborn.scatterplot(
        data=df,
        x="Staleness in years",
        y="Success",
        hue="Registry",
        ax=ax,
    )
    samples = 20
    for p_0_draw, r_draw in zip(idata.posterior["p_0"][-1][-samples:], idata.posterior["r"][-1][-samples:]):
        ax.plot(times, float(p_0_draw) * float(r_draw)**-times, color="blue", alpha=0.3)
    # posterior_p_t = idata.posterior["p_0"] * idata.posterior["r"] ** -t
    # ax.plot(t, posterior_p_t.mean(("chain", "draw")), label="Mean")
    # arviz.plot_hdi(t, idata.posterior_predictive["p_t"], hdi_prob=0.8)
    return fig


def params(idata: Any) -> matplotlib.figure.Figure:
    fig = matplotlib.figure.Figure()
    ax0, ax1 = fig.subplots(1, 2)
    seaborn.kdeplot(
        x=idata.posterior["p_0"][-1],
        ax=ax0,
    )
    seaborn.kdeplot(
        x=idata.posterior["r"][-1],
        ax=ax1,
    )
    return fig


def get_common_file_types(hub: RegistryHub) -> pandas.DataFrame:
    files = [
        file
        for execution in tqdm.tqdm(hub.executions)
        for file_bundle in [execution.outputs]
        for file in file_bundle.files.values()
    ]
    from wf_reg_test.util import sanitize_file_type
    records = []
    for registry in hub.registries:
        for workflow in registry.workflows:
            total_successful = sum(
                execution.successful
                for revision in workflow.revisions
                for execution in revision.executions
            )
            if total_successful > 1:
                common_path_types = collections.Counter([
                    (path, sanitize_file_type(file.file_type))
                    for revision in workflow.revisions
                    for execution in revision.executions
                    if execution.successful
                    for path, file in execution.outputs.files.items()
                ])
                common_types = collections.Counter()
                for (path, type), count in common_path_types.most_common():
                    if count > 2/3:
                        common_types[type] += 1
            records.append({
                "registry": registry.display_name,
                "workflow": workflow.display_name,
                "total_successful": total_successful,
                "common_outputs": bool(common_path_types),
                **{
                    ("count", type): count
                    for (_, type), count in common_path_types.most_common(10)
                },
            })
    df = pandas.DataFrame.from_records(records)
    df["registry"] = df["registry"].replace("snakemake-workflow-catalog", "smk-wf-cat")
    df["registry"] = pandas.Categorical(df["registry"])
    df["workflow"] = pandas.Categorical(df["workflow"])
    return df


def common_file_types_table(df: pandas.DataFrame) -> str:
    types = [type[1] for type in df.columns if type[0] == "count"]
    nf_mask = df["registry"] == "nf-core"
    sm_mask = df["registry"] == "smk-wf-cat"
    def do_three_times(func):
        return  " & ".join(map(str, ["", func(df), func(df[sm_mask]), func(df[nf_mask])]))
    translate_type = {
        "Blocked GNU Zip Format (BGZF; gzip compatible)": "Blocked GNU Zip Format",
        "SVG Scalable Vector Graphics image": "SVG image",
    }
    return "\n".join([
        r"\begin{tabular}{p{1.7in}ccc}",
        textwrap.indent("\n".join([
            r"Type & Total & SWC & nf-core \\",
            r"\midrule",
            *[
                translate_type.get(type, type) + do_three_times(lambda df: r"{:.0f}\%".format(divide_or(
                    sum(df[df["total_successful"] > 1][("count", type)] > 0) * 100,
                    sum(df["total_successful"] > 1)))) + r" \\"
                for type in types
            ],
            r"\midrule",
            "Total" + do_three_times(lambda df: str(sum(df["total_successful"] > 1)))
        ]), prefix="    "),
        r"\end{tabular}",
    ])


@ch_time_block.decor()
def post_process(random_seed: int = 0) -> None:
    # TODO: make this local to this function
    seaborn.set_theme()

    cache_path = pathlib.Path(".cache2/")
    cache_path.mkdir(exist_ok=True)

    generated_path = pathlib.Path("generated")
    if generated_path.exists():
        shutil.rmtree(generated_path)
    generated_path.mkdir(exist_ok=True)

    if (cache_path / "df.pkl").exists():
        # hub = pickle.loads((cache_path / "hub.pkl").read_bytes())
        df = pickle.loads((cache_path / "df.pkl").read_bytes())
        common_file_types = pickle.loads((cache_path / "common_file_types.pkl").read_bytes())
    else:
        hub = deserialize(index_path)
        df = to_pandas(hub)
        common_file_types = get_common_file_types(hub)
        (cache_path / "hub.pkl").write_bytes(pickle.dumps(hub))
        (cache_path / "df.pkl").write_bytes(pickle.dumps(df))
        (cache_path / "common_file_types.pkl").write_bytes(pickle.dumps(common_file_types))

    print(df.dtypes)

    (generated_path / "summary_table.tex").write_text(summary_table(df))

    (generated_path / "crash_table.tex").write_text(crash_table(df))

    (generated_path / "common_file_types.tex").write_text(common_file_types_table(common_file_types))

    data_by_workflow = (
        df.groupby("workflow", as_index=False)
        .agg({
            "revision": lambda df: df.nunique(),
            "registry": lambda df: df.iloc[0],
            "success": lambda df: sum(df) / len(df) * 100,
        })
    )
    data_by_workflow["registry"] = pandas.Categorical(data_by_workflow["registry"], categories=["nf-core", "SWC"], ordered=True)

    # sm_mask = data_by_workflow["registry"] == "smk-wf-cat"
    # nf_mask = data_by_workflow["registry"] == "nf-core"
    # for mask in [sm_mask, nf_mask]:
    #     df2 = data_by_workflow[mask].sort_values("revision")
    #     print(df2.head())
    #     print(df2.tail())
    #     print(df2["revision"].describe())
    #     df2 = data_by_workflow[mask].sort_values("success")
    #     print(df2.head())
    #     print(df2.tail())
    #     print(df2["success"].describe())

    fig = revisions_per_workflow(data_by_workflow)
    fig.savefig(generated_path / "revisions_per_workflow.pdf")
    matplotlib.pyplot.close(fig)

    fig = revision_success_rate(data_by_workflow)
    fig.savefig(generated_path / "revision_success_rate.pdf")
    matplotlib.pyplot.close(fig)

    fig = cpu_time(df)
    fig.savefig(generated_path / "cpu_time.pdf")
    matplotlib.pyplot.close(fig)

    fig = staleness(df)
    fig.savefig(generated_path / "staleness.pdf")
    matplotlib.pyplot.close(fig)

    model = pymc_model(df)

    pymc.model_to_graphviz(model).render(engine="dot", format="pdf", filename=generated_path / "model")

    if (cache_path / "sample.pkl").exists():
        idata = pickle.loads((cache_path / "sample.pkl").read_bytes())
    else:
        idata = pymc_sample(model, random_seed)
        (cache_path / "sample.pkl").write_bytes(pickle.dumps(idata))

    fig = posterior_success_and_staleness(df, idata)
    fig.savefig(generated_path / "posterior_success_and_staleness.pdf")
    matplotlib.pyplot.close(fig)

    fig = params(idata)
    fig.savefig(generated_path / "params.pdf")
    matplotlib.pyplot.close(fig)
