---
# See https://raw.githubusercontent.com/charmoniumQ/nix-documents/main/examples-src/markdown-bells-and-whistles/index.md
fail-if-warnings: yes
standalone: yes
dpi: 300
table-of-contents: no
citeproc: yes
cite-method: citeproc # or natbib or biblatex
bibliography: main.bib
link-citations: yes # in-text citation -> biblio entry
link-bibliography: yes # URLs in biblio
notes-after-punctuation: yes

title: Mitigating failures of software replicability in computational science
number-sections: no

indent: no
pagestyle: plain
papersize: letter

colorlinks: yes
linkcolor: blue
abstract: |
  Irreplicability in computational experiments undermines long-term credibility of science and hinders day-to-day operations of scientists.
  We plan to use Delta to test computational experiments (often workflows) and study the prevalence and mitigiations of software irreplicability in practice.
  We will create and share a public dataset of software irreproducibility in computational experiments.
  This data will be used by us and others to collect data for best practices, make continuous testing feasible, and repair broken programs.
  These techniques increase the replicability of computational experiments.
---

<!--
https://www.ncsa.illinois.edu/expertise/user-services/allocations/delta-proposal-guidelines/

TODO: intervention vs prediction

- Repatability := (same team, same experimental setup) "The measurement can be obtained with stated precision by the same team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same location on multiple trials. For computational experiments, this means that a researcher can reliably repeat her own computation."
- Replicability := (different team, same experimental setup) "The measurement can be obtained with stated precision by a different team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts."
- Reproducibility := (different team, different experimental setup) "The measurement can be obtained with stated precision by a different team, a different measuring system, in a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using artifacts which they develop completely independently."

We define several "measurements" for the above definitions.
- Successful termination := whether the computational experiment runs to completion without error. It may intuitively feel like a "measurement" should be continuous, but it there is no technical reason a measurement can't be a binary for the purposes of the definitions of repeatability, replicability, reproducibility. If the experiment runs in a UNIX environment, this usually means that it returns an exit code of 0.
- Output format := the structure of metadata in an output artifact. For a typical UNIX process, the labels consist of the tree of filenames, CSV column names, HDF5 group-hierarchy, and other structures.
- Output vector := the data values in an output artifact. For example, the CSV contents or HDF5 arrays.
- Output bytes := the bits consisting of the output artifact

We can cautiously assume that experiments in a registry did successfully terminate at the time they were uploaded (although this does become a threat to validity).
When we run the experiment in our system, we determine the replicability of successful termination, since we have a different computational environment.
However, we don't know the original output, so we cannot determine the replicability of the output.
Instead, we will determine the repeatability of the output.
If the output has a repeatable format, then we can find the variance in the output vector across repetitions.
Whether the output vector itself is repeatable depends on the "stated precision."
We can determine the maximal "stated precision" with which the output vector is repeatable.

PRNG state and parallel schedule contribute to non-repeatability of output bytes.
Byte-wise repeatability is desirable because it is easier to debug and it makes memory errors less probable.
{`rr`, /dev/{,u}random, PRNG state, time of day, multiprocessing} affect repeatability.
Non-determinsim affects this.

Network resources and incompletely captured dependencies contribute to irreproducibility of successful termination.
Continuous testing can help irreproducibility even without acceptance tests.

-->

# Participants

| Name | Role | Institution | Email |
|----|----|--------|--------|
| Daniel S. Katz | PI | NCSA | <dskatz@illinois.edu> |
| Darko Marinov | Co-PI | Department of Computer Science, UIUC | <marinov@illinois.edu> |
| Reed Milewicz | Extern Collaborator | Sandia National Laboratories | <rmilewi@sandia.gov> |
| Samuel Grayson | Student | Department of Computer Science, UIUC | <grayson5@illinois.edu> |

# Project Overview

More than 90% of scientists surveyed across all fields use research software and 50% develop software for their research experiments [@hettrick_softwaresavedsoftware_in_research_survey_2014_2018].
However, their research software often fails to be replicable[^repro-terms].
This irreplicability hinders day-to-day operations, because scientists cannot easily build on each others work.
It also undermines trust in science, because sciensts cannot independently scrutinize each others' results.

[^repro-terms]:
In this article, we use ACM's terminology [@plesser_reproducibility_2018]:
**Repeatable:** one can execute the computational experiment again in the same computational environment to get an approximately equivalent result.
**Replicable:** one can execute the computational experiment in a different computational environment to get approximately equivalent results.
**Reproducible:** one can execute a novel computational experiment to come to the same conclusion
Reproducibility is what scientists ultimately want, but repeatability and replicability are necessary stepping stones on the way.

<!-- irreplicable software could always be irreplicable or it could have started out as replicable and collapsed. -->
Software tends to break over time, even if it is unchanged, due to non-obvious changes in the computational environment.
This phenomenon is called "software collapse" [@hinsen_dealing_2019], because software with an unstable foundation is analogous to a building with an unstable foundation.

Unfortunately, irreplicability is widespread in the computational science domain.
Zhao et al. studied software replicability of computational experiments deposited in the myExperiment registry in 2012 [@zhao_why_2012].
They found that 80% of the experiments in their selection were irreplicable, for a variety of causes: change of third-party resources, unavailable example data, insufficient execution environment, and insufficient metadata;
of these, change of third-party resources caused the most failures, such as when a step in an experiment referenced data from another server through the internet which was no longer available.

There are many proposed techniques to ensure replicability, of which most fall into two categories: proactive and reactive.
A _proactive technique_ would control and preserve the environment or application to ensure replicability as software ages, whereas a _reactive technique_ would seek to detect and mitigate non-determinism once it occurs. <!-- Relate "non-determinism" to "collapse"/"replicability" -->
Proactive techniques include using containers (Docker, Singularity, Apptainer, Shifter), virtual machines, system call interposition (Guo's CDE [@guo_cde_2011], Mozilla's [`rr`][1]).
Currently, no mainstream proactive techniques can completely control non-determinism due to network resources, pseudorandomness, and parallel program order without sacrificing a large performance penalty or storage costs.
The user would be getting possibly irreplicable results without even knowing it.

[1]: https://rr-project.org/

On the other hand, _continuous testing_[^CI] seeks to detect rather than eliminate sources of irreplicability.
Continuous testing would run the experiment multiple times to assess if the experiment is still producing the same results (replicability).
Continuous testing handles the "blind-spots" of proactive techniques.
For example, continuous testing might be able to detect when an experiment has non-determinism due to parallel program order.
If the user knows that the experiment is non-deterministic, they could experimentally determine the variance of the result or attempt to fix the non-determinism.
With proactive-only techniques, the user would not even know that their experiment was non-deterministic.

<!--

- For non-deterministic pseudorandomness, replicated executions naturally explore the space of possible seeds.
- For parallel program order, replicated executions on different core-counts or with random scheduling perturbations[^chaos-mode] will explore the space of possible schedules.
- For network resources, replicated executions will identify flaky resources when they become inaccessible. It will not waste the user's time identifying resources that are still accessible, leaving them to focus on only the network resources that are actually flaky.

[^chaos-mode]: The tool `rr` (<https://rr-project.org/>) has a mode that injects random perturbations into the OS scheduler (prioritizing and deprioritizing threads). This approach makes intermittent bugs more likely to occur, so they can be observed and fixed. -->

The major drawback is increased computational cost, since running a computational experiment can be expensive.
However, if one could predict which experiments were more likely to break, one could also prioritize testing on that basis, an optimization we term _predictive continuous testing_.


[^CI]: The continuous testing we are proposing here differs from CI/CD because our proposed continuous testing is triggered periodically, while CI/CD is triggered when the code is changed. CI/CD mitigates software regressions, which are due to _internal changes_, but continuous testing mitigates software collapse, which is due to _external changes_.

<!-- non-determinism -< nonderminism -->

![Predicting the rate of software collapse can reduce resource utilization and increase efficacy of continuous testing.](predictive_maintenance.png){ width=20%, height=25% }

 <!-- Globally: Bug -> Collapse in figure, increase font -->
 
 <!-- Check page limit -->

Once a bug has been identified (perhaps by continuous testing), _automated program repair_ attempts to apply solutions based on comparing the error-message to a database of common errors and solutions.
This technique has been done successfully in other domains [@henkel_shipwright_2021], and it pairs well with continuous testing, since continuous testing identifies the errors, and automated program repair can try to fix it.

# Target Problem

We plan to study the usage and efficacy of these techniques and even improve them.
However, to do so, we need data on the replicability of computational experiments, and such data either has not been collected or made public.
While many experimental registries exist [@ewels_nf-core_2020; @oconner_dockstore_2017; @silva_workflowhub_2020; @goble_myexperiment_2010; @coleman_wfcommons_2022], they do not store prior results, so we cannot tell if the experiment is replicable.
We will collect data on software collapse of computational experiments by automatically running computational experiments from public registries.
Then, we will release a public dataset, so other research can proceed from this experiment.
The resources of Delta are necessary because there are many registries, each experiment can have many versions, and each version may take a while to run.
These registries include:

- [nf-core](https://nf-co.re/) [@ewels_nf-core_2020]: community-curated, Nextflow pipelines for bioinformatics
- [Dockstore](https://dockstore.org/) [@oconnor_dockstore_2017]: user-contributed, multi-platform (WDL, CWL, Nextflow) pipelines for genomics
- [Snakemake Catalog](https://snakemake.github.io/snakemake-workflow-catalog/): GitHub-mined, Snakemake pipelines
- [WorkflowHub](https://workflowhub.eu/) [@silva_workflowhub_2020]: user-contributed, multi-platform (Galaxy, CWL, Nextflow) pipelines
- [myExperiment](https://www.myexperiment.org/) [@goble_myexperiment_2010]: user-contributed, multi-platform (Taverna, Galaxy) pipelines for bioinformatics
- [WfCommons](https://github.com/wfcommons) [@coleman_wfcommons_2022]: researcher-selected, multi-platform (Makeflow, Nextflow, Pegasus) pipelines

Because we cannot take one computational experiment and simulate it one, five, and ten years into the future,
we will instead look for historical versions of an experiment from one, five, or ten years ago and simulate it today.
The registries above store historical versions of the experimental code.
Some will still work, and some will fail, due to software collapse.
In either case, resulting execution will be stored in our database.
The following pseudo-code summarizes this procedure:

\footnotesize
```python
for registry in registries:
    for experiment in registry:
        for version in experiment:
            for i in range(num_repetitions):
                execution = execute(version)
                data.append((
                    execution.date,   execution.output,
                    execution.logs,   execuiton.res_usage,
                    version.date,     version.code,
                    experiment.name,  registry.name,
                ))
```
\normalsize

This dataset will allow us to answer the following research questions (and we will share the dataset so that others can also use it to answer their own research questions in this area of software engineering):

**RQ1:**
What are typical rates of software collapse over time?
We plan to reproduce the experiment described by Zhao et al. [@zhao_why_2012], which assesses if the computational experiments are replicable in our environment.
To the existing categorization, we add "repeatable results" as a new column, which says whether two subsequent executions yield the same result.
We will also study how the proportion of broken experiments changes with time.

**RQ2:**
When software collapses, what is the immediate technical cause?
Zhao et al. studies these at a high-level, and we plan to replicate those categories as well as delve into more subcategories.
For example, when a third-party resource is unavailable, we will assess whether that resource is _data_ or a _software dependency_.

**RQ3**
Can we predict the rate of collapse for a project based on its history, staleness, and properties of the code?
A predictive model is important for the next research question.
The model should operate from a "cold start," where we know nothing about the computational experiment's historical results, but also be able to learn from historical executions if they are present.

**RQ4:**
Can we improve the efficiency of continuous testing by predicting the rate of collapse?
Predicting collapse could be useful for institutions, such as national labs, wanting to ensure their computational experiments remain valid while using resources efficiently.
Since we would have data on the computational cost (runtime and RAM) of each experiment, we can analytically simulate "what if we test X every Y days."
Then we can simulate a system that tests each computational experiment in a frequency based on its failure rate and computational cost, for example processor-time and RAM.

**RQ5:**
What are the best practices that improve replicability?
We plan to examine choice of workflow manager, lines of code, choice of replicability tools (docker, `requirements.txt` with pinned packages, singularity), and other factors.

**RQ6:**
In what fraction of the cases does automatic repair work?
Automatic repair could let one run old experiments off-the-shelf.
We can apply techniques similar to Shipwright [@henkel_shipwright_2021], such as using a language model to categorize many failures into a few clusters.

## Description of codes

<!-- Concise -->
We developed a [Python script](https:/github.com/charmoniumQ/wf-reg-test/) that finds computational experiments from the registries and tests them.
We use [Spack](https://spack.io/) to build our computational environment in `environment.yaml`.
We do not require any runtime libraries to be installed at root-level, since Spack can install these at the user-level.
We plan to^[However, we are open to suggestions.] install the Spack environment to network filesystem that all the worker nodes can read.
Among other things, our Spack environment contains Python, Singularity, OpenJDK, and common UNIX libraries.
The code is not done yet; namely, we need to implement scanning for more registries and execution-handlers for more workflow engines.

We have not explicitly characterized the set of experiments, but we expect they generally consist of a high-level scripting language driving a set of high-performance kernels across a large in-memory dataset.
The tasks are usually CPU, with a some experiments having GPU tasks as well.
CPU tasks are usually memory-bound, while GPU tasks can be either.

We have yet to parallelize the application, but intend to use parallelism to fully utilize Delta's resources and get our results in a practical time.
We can compute multiple experiments simultaneously in a perfectly parallel (also called "embarrassingly parallel") manner.
We expect to compute hundreds of experiments simultaneously, each of which takes tens of minutes to terminate; this implies that a global work-queue will not be a performance bottleneck.
This system can be implemented easily from our existing code using the parallel-map paradigm in [Dask](https://www.dask.org/) or [Parsl](http://parsl-project.org/).

<!--
The output can be divided into two parts: the "small" output containing statistics regarding the execution and a hash of the experiment's output, and the "big" output containing the experiment's output.
Each small-data record of an experiment will fit in hundreds of bytes, so tens of thousands of versions of experiments will yield one megabyte, which will be easily processible on our resources.
Research questions 1, 3, 4, and 5 can be answered by just the "small" output.
Each big-data record could be on the order of gigabytes.
Research questions 2 and 6 require elements from the "big" output of just the collapsed (broken) workflows.
-->

## Experience, readiness, usage plans, and funding sources

We have experience with SLURM batch system, parallel programming, and related HPC technology from using the Campus Cluster.

We do not have estimates on the efficiency of the underlying computational experiments because they are so diverse, and it would take a large HPC resource to gather this efficiency data.

Note that we need to develop more features and robustness in our code before we can run it on an HPC system.
First, we need to parallelize (see prior section), then we need to implement more kinds of runners, so that we can run more experiments, then we need to scrape more registries so we have experiments to run.
This work can be completed within a month.

## Resources required

| Registry | Number of experiments
|------|--|
|nf-core|32|
|Snakemake|42|
|dockstore|~100|
|WorkflowHub|201|
|myExperiment|82|
|WfCommons|7|

We have about 500 experiments, 8 versions per experiment, 5 executions per experiment, 1000 core-seconds per execution, which amounts to 5,000 core-hours or 32 cores working for 7 days.

<!-- 500 * 8 * 5 * 1000 / 60/60/24 -->

Of these, 5% of experiments have GPU tasks. Therefore, we estimate our tasks require 300 GPU-hours or 2 GPUs working continuously for 7 days.

Each experiment emits about 300 Mb of data.
During execution, we need to store the full output so that we can compare their differences.
If we use 32 concurrent workers, this gives 10Gb during execution.
After the execution, we only need to store the "large" results (see Description of Codes) of the failing experiments, so they can be investigated further.
We estimate 25% of the 4,000 executions (i.e., 1,000 executions) will fail, leaving us with 300 Gb.
We will likely be able to complete the analysis within a few months.

|Resource|Request|
|------|---|
|Core-hours|5,000|
|GPU-hours|300|
|Storage|300Gb for three months|

<!--
Start-up awards of up to 1,000 GPU hours and 50,000 CPU core hours may be requested for test runs and to determine full allocation request needs.
ypical allocation awards scale up to 25,000 GPU hours or 690,000 CPU core hours.
More information on Delta Policies & Submissions Guidelines as well as Proposal Submission Instructions can be found on the Delta Illinois Allocation webpage: https://www.ncsa.illinois.edu/expertise/user-services/allocations/
-->

## Requested start date and duration

We request to begin execution on December 1.
While we expect our allocation to be valid for 1 years, we also expect to use the resources in 2022 Q4, and storage resources in 2022 Q4 and 2023 Q1.

# References

::: {#refs}
:::
