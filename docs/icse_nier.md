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
author:
- Samuel Grayson, Department of Computer Science <grayson5@illinois.edu>
- Daniel S. Katz, NCSA <dskatz@illinois.edu>
- Darko Marniov, Department of Computer Science <marinov@illinois.edu>
- Reed Milewicz, Sandia National Laboratories <rmilewi@sandia.gov>
number-sections: no

indent: no
pagestyle: plain
papersize: letter

colorlinks: yes
linkcolor: blue
---

# Abstract

_I will write this last. TODO_

# Introduction

More than half of scientists surveyed fields develop software for their research [@hettrick_softwaresavedsoftware_in_research_survey_2014_2018].
Unfortunately, the code they develop tends to break over time, even if it is unchanged, due to non-obvious changes in the computational environment.
This phenomenon is called "software collapse" [@hinsen_dealing_2019], because software with an unstable foundation is analogous to a building with unstable foundation.
This breakage could manifest as irreproducible[^1] results.

[^1]: In this article, we use Claerbout's terminology [@claerbout_electronic_1992]. "Reproducibility" means anyone can use the same code to get the same result.

<!-- TODO: define bit-by-bit comparison, exact semantic comparison, approximate semantic comparison, and no-crash comparison. This study primarily deals with no-crash reproducibility and bit-by-bit repeatability, that is whether anyone can run the code without it crashing, and whether they can get identical results. -->

If computational experiments are allowed to collapse, scientists cannot independently verify or build on those results.
Thus, software collapse undermines two fundamental norms of science identified by Merton, organized skepticism and communalism [@merton_sociology_1974].
Software collapse is a technical factor which contributes to the ongoing reproducibility crisis in computational science [@collberg_repeatability_2016], which hinders the credibility of science [@ioannidis_why_2005].

Zhao et al. studied software collapse computational of experiments deposited in the myExperiment registry [@zhao_why_2012].
They find 80% of the experiments in their selection did not work, for a variety of causes: change of third-party resources, unavailable example data, insufficient execution environment, and insufficient metadata.
Of which, change of third-party resources causes the most failures.
This would include a step in the experiment that references data from another server through the internet which is no longer available.

Part of the problem is technical: people who want their software to be reliable do not necessarily know how to achieve that, given their resource constraints.
We suggest a technical solution, which should be a part of a holistic solution.
The technical solution could be proactive or reactive; A proactive solution would change something about the environment or application to provide determinism, whereas a reactive solution would seek to detect non-determinism and alert human developers.
Proactive solutions are preferable, but to date, no proactive solution will eliminate a large case of irreproducibility.
Therefore, we need both proactive and reactive solutions.

## Proactive solutions

- **Docker**: A Dockerfile is a set of UNIX commands and auxiliary commands that specify how to build a Docker image.
  However, these instructions are UNIX commands, which can be non-deterministic themselves[^2], e.g. `pip install ...`.
  Docker cannot mitigate non-determinism due to network resources, pseudorandomness, and parallel program order.
  Zhao et al. showed that first of these, networked resources, is the most common cause of software collapse as well [@zhao_why_2012].
  This is empirically validated, as Henkel et al. find 25% of Dockerfiles in their already limited sample still fail to build [@henkel_shipwright_2021].

[^2]: Docker itself never claims that `Dockerfile`s are reproducible; it only says "reproducible" three times in [their documentation] at the time of writing, and none of them are referring to reproducing the same result from running a `Dockerfile` twice.
  
[their documentation]: https://www.google.com/search?q=reproducible+site%3Adocs.docker.com&client=ms-google-coop&cx=005610573923180467403%3Aiwlnuvjqpv4&ei=iPFEY4eSFY-fptQPopa3aA&ved=0ahUKEwiH9vrzq9f6AhWPj4kEHSLLDQ0Q4dUDCA4&uact=5&oq=reproducible+site%3Adocs.docker.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzoKCAAQRxDWBBCwAzoHCAAQsAMQQzoFCAAQgAQ6CAgAEIAEELEDOgQIABBDOggIABAWEB4QDzoKCAAQFhAeEA8QCjoGCAAQFhAeOgUIIRCgAToFCCEQqwJKBAhBGABKBAhGGABQ5wJYyxpg-xtoBHABeAGAAccCiAGaHJIBCDAuMTcuNS4xmAEAoAEByAEKwAEB&sclient=gws-wiz-serp

- **Filesystem snapshot**: Container images (e.g. Docker, Singularity), functional package managers (e.g. Nix, Guix), CDE [@guo_cde_2011], Sumatra [@davison_automated_2012], and chroot containers spawn a program in a view of the filesystem that they control.
  Then, one can ship the entire filesystem to another user so they can reproduce the execution.
  However, this approach is heavyweight with filesystem snapshots as large as 50Gb.
  Furthermore, this does not control network resources, pseudorandomness, and parallel program order.
  Finally, these are difficult to work with to 

## Reactive solution

Continuous testing is a reactive solution to software collapse that is robust to networked resources, pseudorandomness, and parallel program order.
One could imagine running the computational experiment periodically to assess if the experiment is still not crashing and still reproducible.
The major drawback is increased computational cost.
However, one can always lower the frequency of testing, which trades off computational resources with efficacy of finding bugs.
Additionally, one could test mission-critical experiments more frequently than other experiments.
If one could predict which workflows were more likely to break, one could also prioritize testing on that basis.

![Predicting the rate of software collapse can reduce the resource utilization and increase efficacy of continuous testing.](predictive_maintenance.png){ width=2.5in }

# Methods

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


# Analysis

We will replicate the quantities described by Zhao et al. [@zhao_why_2012] to see if these are changed: proportion of broken experiments, and proportion of breakages due to each reason (volatile third-party resources, missing example data, missing execution environment, insufficient description).
To this, we add "reproducible results" as a new "level" of success, beyond merely not crashing.
We will also extend the failure classification of Zhao et al. by going into deeper subcategories.
We will extend the results of Zhao et al. by asking how the proportion of broken experiments changes with time.

We can improve resource utilization of continuous testing by using our dataset to predict the rate of collapse of various computational experiments.
We will develop predictive models based on the staleness, properties of the code in the revision, and other determinants to predict the probability that a given experiment will fail.
Testing experiments prone to failure more often than reliable ones could save computational resources while maintaining approximately the same degree of reliability in all experiments.
<!--
Note that a failure could indicate collapse, or it could indicate that the experiment never worked in the first place, possibly due to incomplete metadata.
-->

Hinsen suggests that most code should build on reliable, well-tested libraries can provide some degree of resistance to collapse [@hinsen_dealing_2019].
In practice, many experiments fall into collapse despite their best effort to build on reliable foundations.
If that level of reliability is insufficient, one can add continuous testing to help get more reliability.

Once we know what kinds of failure are possible, we can also investigate automatic repair.
Our dataset will contain the output logs for each failure.
Therefore, we can apply similar techniques to Shipwright [@henkel_shipwright_2021], such as using a language model to categorize a large number of failures into a small number of clusters.

We can also use your model to identify best practices, by seeing if they correlate to an empirically lower failure rate.
We will use a "Bayes net" to test for confounding causal variables.
We will operationalize a set of reproducibility metrics based on existing literature and compare them to established software quality measures and their evolution over time for a small set of exemplar software projects; this work will leverage tools our team has developed for repository mining at scale.

<!--
This model will allow us to develop systems that efficiently detect collapse, develop repair techniques, and identify best practices.
One of them might be the choice of workflow engine; perhaps some engines have stronger reproducibility guarantees.

We hypothesize that lower software quality can lead to greater instability in software behavior and this ultimately harms reproducibility (e.g., more intervals of irreproducibility due to broken builds , poorly managed dependencies leading to flaky results , or poor test coverage concealing divergent behaviors).
If successful, our preliminary work will provide us with a tested ensemble of reproducibility metrics and suggest quality measures that may be aligned with those metrics.
-->

## Threats to Validity

The time symmetry assumption may not hold.
With all of the contemporary focus and effort around reproducibility, future rates of change may be markedly less than past rates of change.
While our computed rates of change will be understimates, those underestimates can still be useful as bounds.
Our method will also be useful, unchanged, for future studies.

It is possible that our sample is not representative of the real world of computational experiments.
However, we are casting the widest net we can by systematically pulling a large number experiment from several registries.
Still there is a selection bias in which workflows end up in registries.
The model has some factors based on the population and some based on the actual history of the experiment.
Its initial guess when there is no history would be biased by our selection, but in the long-run it would learn the characteristics of the actual experiment.

_TODO: other threats to validity._

# References

::: {#refs}
:::
