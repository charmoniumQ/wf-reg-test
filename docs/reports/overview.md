---
# f=overview.md ; pandoc --standalone --to=revealjs --output=$(basename --suffix .md $f).html $f
title: Testing experiment for software replicability
---

::: incremental

- Volatile third-party resources is the primary cause of non-repeatability (Zhao 2012).
  - Data on the internet
- Don't want to store all of the data with each experiment
- Proactive vs reactive strategy

:::

---

::: incremental

- Use continuous testing!
  - How often to test?
- Use failure rate to tune frequency
  - Need data
  - Could be different per workflow

:::

---

```python
for registry in registries:
    for experiment in registry:
        for version in experiment:
            for i in range(num_repetitions):
                execution = execute(version)
```

---

Registries:

::: incremental

- [nf-core](https://nf-co.re/) [@ewels_nf-core_2020]: community-curated, Nextflow pipelines for bioinformatics
- [Snakemake Catalog](https://snakemake.github.io/snakemake-workflow-catalog/): GitHub-mined, Snakemake pipelines
- SAW SDM (Sandia National Labs): engineering, SAW pipelines
- [Dockstore](https://dockstore.org/) [@oconnor_dockstore_2017]: user-contributed, multi-platform (WDL, CWL, Nextflow) pipelines for genomics
- [WorkflowHub](https://workflowhub.eu/) [@silva_workflowhub_2020]: user-contributed, multi-platform (Galaxy, CWL, Nextflow) pipelines
- [myExperiment](https://www.myexperiment.org/) [@goble_myexperiment_2010]: user-contributed, multi-platform (Taverna, Galaxy) pipelines for bioinformatics
- [WfCommons](https://github.com/wfcommons) [@coleman_wfcommons_2022]: researcher-selected, multi-platform (Makeflow, Nextflow, Pegasus) pipelines

:::

---

::: incremental

- Not trying to get individual workflows to work, but classes of workflows
- 10 workflows break in different ways vs breaking in the same way.
  - E.g. Workflow requires ftputil

:::

---

::: incremental

- Execution targets:
  - Home machine (low cores)
  - Sandia machine (some HTTPS traffic doesn't work; no root)
  - NCSA Delta? (no root)
  - AWS (not free)

:::
