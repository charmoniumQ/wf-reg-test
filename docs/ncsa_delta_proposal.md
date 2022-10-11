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

title: A reactive approach to identifying and mitigating software collapse computational science
number-sections: no

indent: no
pagestyle: plain
papersize: letter

colorlinks: yes
linkcolor: blue
---

<!--
https://www.ncsa.illinois.edu/expertise/user-services/allocations/delta-proposal-guidelines/
-->

# Participants

| Name | Role | Institution | Email |
|-----|----|--------|-------|
| Daniel S. Katz | PI | National Center for Supercomputing Applications | <dskatz@illinois.edu> |
| Darko Marinov | Co-PI | Department of Computer Science, UIUC | <marinov@illinois.edu> |
| Reed Milewicz | Extern Collaborator | Sandia National Laboratories | <rmilewi@sandia.gov> |
| Samuel Grayson | Student | Department of Computer Science | <grayson5@illinois.edu> |

# Abstract

_I will write this last. TODO_

# Project Overview

Computational experiments tend to break over time, even if they are unchanged, due to non-obvious changes in the computational environment.
This phenomenon is called "software collapse" [@hinsen_dealing_2019], because software with an unstable foundation is analagous to a building with unstable foundation.
This breakage could manifest as irreproducible[^1] results.
If computational experiments are allowed to collapse, scientists cannot independently verify or build on those results.
Thus, software collapse undermines two fundamental norms of science identified by Merton, organized skepticism and communalism [@merton_sociology_1974].

[^1]: In this article, we use Claerbout's terminology [@claerbout_electronic_1992]. "Reproducibility" means anyone can use the same code to get the same result.

The technical solution could be proactive or reactive; A proactive solution would change something about the environment or application to provide determinism, whereas a reactive solution would seek to detect non-determinism and alert human developers.
Proactive solutions are preferable, but to date, no proactive solution will work in the majority of cases.
Therefore, we need both proactive and reactive solutions.

Continuous testing is a reactive solution to software collapse that is robust to networked resources, pseudorandomness, and parallel program order.
One could imagine running the computational experiment periodically to assess if the experiment is still not crashing and still reproducible.
The major drawback is increased computational cost.
However, one can always lower the frequency of testing, which trades off computational resources with efficacy of finding bugs.
Additionally, one could test mission-critical experiments more frequently than other experiments.
If one could predict which workflows were more likely to break, one could also prioritize testing on that basis.

![Figure: Predicting the rate of software collapse can reduce the resource utilization and increase efficacy of continuous testing.](predictive_maintenance.png){ width=2.5in }

We will replicate the quantities described by Zhao et al. [@zhao_why_2012] to see if these are changed: proportion of broken experiments, and proportion of breakages due to each reason (volatile third-party resources, missing example data, missing execution environment, insufficient description).
To this, we add "reproducible results" as a new "level" of success, beyond merely not crashing.
We will also extend the failure classification of Zhao et al. by going into deeper subcategories.
We will extend the results of Zhao et al. by asking how the proportion of broken experiments changes with time.

We can improve resource utilization of continuous testing by using our dataset to predict the rate of collapse of various computational experiments.
We will develop predictive models based on the staleness, properties of the code in the revision, and other determinants to predict the probability that a given experiment will fail.
Testing experiments prone to failure more often than reliable ones could save computational resources while maintining approximately the same degree of reliability in all experiments.

Hinsen suggests that most code should build on reliable, well-tested libraries can provide some degree of resistance to collapse [@hinsen_dealing_2019].
In practice, many experiments fall into collapse despite their best effort to build on reliable fundations.
If that level of reliability is insufficient, one can add continuous testing to help get more reliability.

Once we know what kinds of failure are possible, we can also investigate automatic repair.
Our dataset will contain the output logs for each failure.
Therefore, we can apply similar techniques to Shipwright [@henkel_shipwright_2021], such as using a language model to categorize a large number of failures into a small number of clusters.

We can also use your model to identify best practices, by seeing if they correlate to an empirically lower failure rate.
We will use a "Bayes net" to test for confounding causal variables.
We will operationalize a set of reproducibility metrics based on existing literature and compare them to established software quality measures and their evolution over time for a small set of exemplar software projects; this work will leverage tools our team has developed for repository mining at scale.

# Target Problem

We want to collect data on software collapse of computational experiments by automatically running computational experiments from public registries.
These registries include:

- [nf-core](https://nf-co.re/): _TODO: describe each of these (one sentence)._
- [Dockstore](https://dockstore.org/)
- [Snakemake Catalog](https://snakemake.github.io/snakemake-workflow-catalog/)
- [WorkflowHub](https://workflowhub.eu/)
- [myExperiment](https://www.myexperiment.org/)
- Sandia's internal repository

We cannot take one computational experiment and simulate it one, five, and ten years into the future.
Instead, we will look for historical revisions of an experiment from one, five, or ten years ago and simulate it today.
All of the registries above store historical revisions of the workflow.
We make a _time symmetry_ assumption: historical rates of change will be similar to the future rate of change.
It is likely that some will still work and some sill fail, due to software collapse.

We will run the following pseudo-code to collect the data.
We will analyze it as described in the next section and publish the raw data for other researchers.

```
for registry in registries:
    for experiment in registry:
        for revision in experiment:
            for i in range(num_repetitions):
                execution = execute(revision)
                data.append((
                    execution.date,
                    execution.output,
                    execution.logs,
                    execuiton.resource_utilization,
                    revision.date,
                    revision.code,
                    experiment.name,
                    experiment.interpreter,
                    registry.name,
                ))
```
## Description of codes

We developed [a Python package](https:/github.com/charmoniumQ/wf-reg-test/) that finds and tests workflows.
This package depends on [Nix](https://nixos.org/) and [Docker](https://www.docker.com/) on the host system.
From Nix and Docker, the package can create software environments for each workflow engine of interest.
We have yet to parallelize the application, but we think this can be done easily using the parallel-map paradigm in [Dask](https://www.dask.org/).
The code is not done yet; namely, we need to implement scanning for more registries and more workflow engines.

## Experience, readiness, usage plans, and funding sources

We have experience with SLURM batch system, Dask programming, and related HPC technology.
Note that we need to develop more features and robustness in our code before we can run it on an HPC system.

## Resources required

5 registries, 100 workflows per registry, 10 revisions per workflow, 300 CPU seconds per workflow is a total of [^TODO: put in latest numbers and recompute.]

## Requested start date and duration

As soon as possible.

# References

::: {#refs}
:::
