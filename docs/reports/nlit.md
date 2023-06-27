---
slideNumber: true
link-citations: true
slide-level: 2
header-includes: |
  <style>
    :root {
      --r-heading1-size: 1.6em;
      --r-heading2-size: 1.4em;
      --r-heading3-size: 1.2em;
      --r-heading4-size: 1em;
    }
  </style>
  <script>
    // Set the title without generating a title slide
    window.title = "Automatic reproduction of Workflows in Snakemake Workflow Catalog and Nf-core"
  </script>
---

# Title {style="font-size: 1.2em"}

[Samuel Grayson, Reed Milewicz]{style="font-size: 1.0em"}

## Why automatic reproducibility?

::: incremental
- Test the current state of reproducibility in practice
- Reproducibility := different team/machine + same code -> consistent measurement [@acm_inc_staff_artifact_2020]
- True "research" reproducibility would need knowledge of the specific experiment
- Instead, look at crash-free reproducibility (no domain knowledge)
- Crash-free reproducibility is necessary for resarch reproducibility
:::

## Why workflows?

::: incremental
- Workflow := script that generates directed acyclic graph (DAG) of tasks
  - Usually each node runs in isolation
  - DAG edges specify  I/O to other nodes
- Workflow engine := interpreter that runs the workflow and executes the DAG
- Workflow registry := set of repositories containing workflows (e.g. GitHub)
- Workflows are easier to code than programs
  - Especially parallelism
:::

<!--
## Registry: nf-core [@ewels_nf-core_2020]

::: incremental
- Nextflow engine only
- Community-curated workflows for common tasks
- Nf-core workflows follow certain conventions
  - Always have `./main.nf`
  - Always define profile for Singularity, Docker
- 48 workflows
- All less than 4.5 years
- Hosted in GitHub, can be viewed at <https://nf-co.re>
:::

## Registry: Snakemake Workflow Catalog

::: incremental
- Snakemake engine only
- All GitHub repositories that follow certain standards
  - Have a snakefile in a specific place
- 2,045 workflows but only 53 workflows with GitHub releases
- Almost all less than 2.5 years
- Hosted in GitHub, can be viewed at <https://snakemake.github.io/snakemake-workflow-catalog/>
:::

# % of automatic reproducibility

- The registries advertise a command which runs these repositories.
- We want to know how often this command is sufficient by itself.

## Workflow engines: Nextflow and Snakemake

::: incremental
- Mostly multiomics users (genomics, proteomics, ...)
- Run in cloud, cluster, or local
- Workflows **may** support running each step in Singularity container
- Singularity := container engine (like Docker)
:::

-->


## Results of automatic reproduction

| Quantity                                              | All              | SWC              | nf-core          |
|-------------------------------------------------------|------------------|------------------|------------------|
| \# workflows                                          | 101              | 53               | 48               |
| % of workflows with at least one non-crashing release | [53%]{.fragment} | [23%]{.fragment} | [88%]{.fragment} |
| \# revisions                                          | 584              | 333              | 251              |
| % of revisions with no crash                          | [28%]{.fragment} | [11%]{.fragment} | [51%]{.fragment} |

# What are common error causes

::: incremental
- Workflow task error
  - Timeout
  - Other
  - Network resource changed
  - Missing software dependency
- Workflow script error
  - Missing data/config input
  - Other
- Workflow engine error
  - Singularity error
  - Conda environment unsolvable
- Unclassified
:::

## Results

::: {.table style="font-size: 24px"}

| Kind of crash                | All   | SWC   | nf-core |
|------------------------------|-------|-------|---------|
| Missing data/config input    | 32.2% | 43.8% | 16.7%   |
| Conda environment unsolvable | 10.8% | 18.9% | 0.0%    |
| Unclassified reason          | 7.9%  | 12.0% | 2.4%    |
| Timeout reached              | 7.0%  | 5.7%  | 8.8%    |
| Singularity error            | 6.0%  | 6.6%  | 5.2%    |
| Other (workflow script)      | 5.7%  | 1.5%  | 11.2%   |
| Other (workflow task)        | 1.2%  | 0.0%  | 2.8%    |
| Network resource changed     | 0.7%  | 0.0%  | 1.6%    |
| Missing software dependency  | 0.5%  | 0.9%  | 0.0%    |
|                              |       |       |         |
| No crash                     | 28.1% | 10.5% | 51.4%   |
|                              |       |       |         |
| Total                        | 100%  | 100%  | 100%    |

# Discussion

## Missing example data is prominent

::: incremental
- Workflow authors should include example data, even if it has to be downloaded from the internet or generated
- This would allow these workflows to be tested automatically by someone without knowledge of how the experiment works
:::

## Container infrastructure is difficult

::: incremental
- Distribute container images or distribute container build files?
- Distribute container images:
  - Expensive to store (DockerHub kicks off free projects)
  - Link rot
  - How to update just one dep?
- Distribute container build files:
  - Lose reproducibility benefits if each user has to build
  - Need a reproducible package manager to do the build
    - Workable solution here!
:::

## Conda environment unsolvable

::: incremental
- Prominent error class
- Package managers should include the spec-file and lock-file
- Source-level functional package managers may be more robust
  - Multi-arch
  - Less storage intensive
  - E.g., Nix, Guix, Spack
    - Guix has support for Software Heritage
  - Can build container images reproducibly
:::

## Continuous integration to detect configuration errors

::: incremental
- Scale down fidelity and size
- Rerun periodically, not just when code changes
- Store small artifacts
  - File read/write set and hash (ptrace)
:::

## Continuous integration to detect bugs

::: incremental
- Parameterize test fidelity and size
- Schedule scaled down test frequently, full fidelity test infrequently
- Instead of hash, collect statistical summary
- Write provenance data to link the inputs to intermediates to outputs
  - Interoperable with other tools (W3C PROV)
<!-- Picture -->
:::

<!--
Update title
Better terminology for bugs
Graphs?
-->
