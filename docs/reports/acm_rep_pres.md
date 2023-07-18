---
# title: Automatic reproduction of Workflows in Snakemake Workflow Catalog and Nf-core
# author:
#   - Samuel Grayson
#   - Darko Marinov
#   - Daniel S. Katz
#   - Reed Milewicz
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
    .reveal table {
      border: separate;
    }
    .reveal .slide-number {
      right: 40px;
      bottom: 120px;
      font-size: 16px;
    }
  </style>
  <script>
    // The default Pandoc-generated citation links don't work because they link to a different slide.
    document.querySelectorAll(".citation a").forEach(a => {a.href = "#/references";});

    // Set the title without generating a title slide
    window.title = "Automatic reproduction of Workflows in Snakemake Workflow Catalog and Nf-core"
  </script>
---

# Automatic reproduction of Workflows in Snakemake Workflow Catalog and Nf-core {style="font-size: 1.2em"}

[Samuel Grayson, Darko Marinov, Daniel S. Katz, Reed Milewicz]{style="font-size: 1.0em"}

---

[Automatic Reproduction]{.fragment} [of Workflows]{.fragment} [in Registries]{.fragment} [(Snakemake Workflow Catalog and Nf-core)]{.fragment}

## Why automatic reproducibility?

::: incremental
- Test the current state of reproducibility in practice
- Reproducible &colone; different team/machine + same code &rArr; consistent measurement [@acm_inc_staff_artifact_2020]
- True "research" reproducibility would need knowledge of the specific experiment
- Instead, look at crash-free reproducibility
- Crash-free reproducibility is necessary for resarch reproducibility
:::

## Why workflows?

::: incremental
- Workflow &colone; script that generates directed acyclic graph (DAG) of tasks
  - DAG edges specify data dependencies to other nodes
  - Usually each node runs in a container
- Workflow engine &colone; interpreter that runs the workflow and executes the DAG
- Workflow registry &colone; archive of workflows (e.g. GitHub)
- Workflows are easier to code than programs
  - Especially parallelism
:::

## Prior work

::: incremental
- "Why workflows break — understanding and combating decay in Taverna workflows" Zhao et al. 2012 [@zhao_why_2012]
- "Repeatability in Computer Systems Research" Collberg and Proebsting 2016 [@collberg_repeatability_2016]
- "A large-scale study on research code quality and execution" Trisovic et al. 2022 [@trisovic_large-scale_2022]
:::

# Research questions

::: incremental
0. Characterize the registries
1. How many workflows were crash-free reproducible?
2. Causes of crashes?
:::

# RQ0: Workflow registries

::: incremental
- Drawn from <https://workflows.community/>
:::

## Registry: nf-core [@ewels_nf-core_2020]

::: incremental
- Nextflow engine only
- Mostly multiomics users (genomics, proteomics, ...)
- Community-curated workflows for common tasks
- Nf-core workflows follow certain conventions
  - Have `./main.nf`
  - Define profile for Singularity, Docker
- 48 workflows
- All less than 4.5 years
- Hosted in GitHub, can be viewed at <https://nf-co.re>
:::

## Registry: Snakemake Workflow Catalog

::: {.incremental style="font-size: 36px;"}
- Snakemake engine only
- Mostly multiomics users (genomics, proteomics, ...)
- All GitHub repositories that follow certain standards
  - Have a snakefile in a specific place
- 2,045 workflows but only 53 workflows with GitHub releases
- Developers can customize the usage command with their run file `.snakemake-workflow-catalog.yml`
- Almost all less than 2.5 years
- Hosted in GitHub, can be viewed at <https://snakemake.github.io/snakemake-workflow-catalog/>
:::

## Registry: WorkflowHub and Dockstore

::: incremental
- WorkflowHub.eu [@ferreira_da_silva_workflowhub_2020] and Dockstore
  - Multiple workflow engines &rArr; no automatic run commands
  - Future work
:::

## Results

| Quantity    | All | SWC | nf-core |
|-------------|-----|-----|---------|
| # workflows | 101 | 53  | 48      |
| # releases  | 584 | 333 | 251     |

# RQ1: % of automatic reproducibility

- The registries advertise a command which runs these repositories.
- We want to know how often this command works without manual input.

## Results

| Quantity                                        | All              | SWC              | nf-core          |
|-------------------------------------------------|------------------|------------------|------------------|
| \# workflows                                    | 101              | 53               | 48               |
| % of workflows with &ge; 1 non-crashing release | [53%]{.fragment} | [23%]{.fragment} | [88%]{.fragment} |
|                                                 |                  |                  |                  |
| \# releases                                     | 584              | 333              | 251              |
| % of releases with no crash                     | [28%]{.fragment} | [11%]{.fragment} | [51%]{.fragment} |

# RQ2: What are common error causes

---

::: incremental
1. Look at one unclassified crashing execution by hand.
   * Describe the high-level reason.
2. Write a regular expression to catch this kind of error.
   * Make sure it is exclusive with the other regular expressions.
3. Mark these as classified.
4. Repeat to 1
5. Spotcheck the results
:::

---

::: incremental
- Workflow task error
  - Timeout
  - Network resource changed
  - Missing software dependency
  - Other
- Workflow script error
  - Missing data/config input
  - Other
- Workflow engine error
  - Singularity error
  - Conda environment unsolvable
- Unclassified
:::

## Results

<div style="font-size: 24px">

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

</div>

## Observations

::: {.incremental style="font-size: 32px"}
- Misisng example data/config is prominent
  - SWC YAML run file does not have a place for example data
  - Sometimes the nf-core `test` profile is insufficient!
  - Workflows should default to example data (downloaded or generated)
- Conda environment solve is also a common factor
  - Conda, by default, does not generate lockfiles
  - Difficult to debug
  - Packages can get yoinked
  - Source-level package managers could be more robust (Spack, Nix, Guix)
    - But Conda is specially supported by Snakemake
:::

<!-- 
# RQ4: What were the outputs?

---

::: {style="font-size: 20px"}
| Type                       | All | SWC | nf-core |
|----------------------------|-----|-----|---------|
| ASCII text                 | 85% | 33% | 100%    |
| HTML document              | 59% | 0%  | 76%     |
| SVG image                  | 26% | 0%  | 33%     |
| Zip archive data           | 7%  | 0%  | 10%     |
| XML 1.0 document           | 4%  | 0%  | 5%      |
| CSV text                   | 19% | 0%  | 24%     |
| JSON text data             | 15% | 0%  | 19%     |
| very short file (no magic) | 4%  | 0%  | 5%      |
| gzip compressed data       | 11% | 0%  | 14%     |
| PDF document               | 7%  | 0%  | 10%     |
| Blocked GNU Zip Format     | 7%  | 17% | 5%      |
| PNG image data             | 4%  | 0%  | 5%      |
| LaTeX 2e document          | 4%  | 0%  | 5%      |
|                            |     |     |         |
| Total                      | 27  | 6   | 21      |
:::

---

- Many plaintext!
- Could be more easily stored and analyzed by registries

-->

# Discussion

## Containers require superuser to install

::: incremental
- Users won't necessarily have root on shared systems
- Rootless user-namespaces exist, but may be too new or not enabled
- Why do we need root to reproduce someone else's code?
  - Linux filesystems are kernel modules, requires root to modify
- Future work could look at CharlieCloud
:::

## Towards an execution description language

::: {.incremental}
- SWC supports a YAML file which says how to run the workflow
- Develop workflow-agnostic way of saying how to run a workflow
  - Stored with the workflow code
  - Could be done by workflow authors or by reproducers
  - Simplify artifact evaluation, CI, reusability, reproducibility
:::

# References {style="font-size: 1.3em"}

::: {#refs style="font-size: 18px"}
:::


# Backup slides

## Links

- [This presentation](https://htmlpreview.github.io/?https://github.com/charmoniumQ/wf-reg-test/blob/main/docs/reports/acm_rep_pres.html)
- [Paper preprint](https://raw.githubusercontent.com/charmoniumQ/wf-reg-test/main/docs/reports/Understanding-the-results-of-automatic-reproduction-of-workflows-in-nf-core-and-Snakemake-Workflow-Catalog.pdf)
- Code [(GitHub)](https://github.com/charmoniumQ/wf-reg-test/) [(archived)](https://zenodo.org/record/7996835)
- Raw data [(rendered)](https://htmlpreview.github.io/?https://github.com/charmoniumQ/wf-reg-test/blob/main/data/results.html) [(archived)](https://zenodo.org/record/7996835) `./data/results.html`

## Continuous integration

::: incremental
- Use current CI scripts
  - If the script multiple targets, which one to use?
  - None of them may actually run the experiment, if it is too expensive to run in CI.
- Use CI script format but write new scripts
  - No way to say **what** the command does
  - Need linked data for that
:::

<!--
python -m http.server
docker run -v $PWD:$PWD astefanutti/decktape reveal file://$PWD/acm_rep_pres.html $PWD/acm_rep_pres.pdf
docker run --net=host -v ${PWD}:/slides astefanutti/decktape reveal http://localhost:8000/acm_rep_pres.html acm_rep_pres.pdf 
-->
