# wf-reg-test

Software tends to break or "collapse" over time, even if it is unchanged, due to non-obvious changes in the computational environment.
Collapse in computational experiments undermines long-term credibility and hinders day-to-day operations.
We propose to create the first public dataset of automatically executable scientific experiments.
This data could be used to identify best practices, make continuous testing feasible, and repair broken programs.
These techniques increase the replicability of computational experiments.

# TODO list

- Registries of computational experiments
  - [x] [nf-core](https://nf-co.re/): Nextflow
  - [x] [Snakemake Catalog](https://snakemake.github.io/snakemake-workflow-catalog/): Snakemake
  - [ ] SAW ECMF: SAW NGW
  - [ ] [WorkflowHub](https://workflowhub.eu/): Galaxy, CWL, Nextflow, Snakemake, KNIME
  - [ ] [Dockstore](https://dockstore.org/): WDL, CWL, Nextflow, Galaxy
  - [ ] [PegasusHub](https://pegasushub.io): Pegasus
  - [ ] [WfCommons](https://github.com/wfcommons): Pegasus, Makeflow, Nextlfow
  - [ ] [myExperiment](https://www.myexperiment.org/): Taverna, RapidMiner, Kepler, Bioclipse, LONI, GWorkflowDL, BioExtract
  - [ ] GitHub?
	
- Computational experiment runtimes
  - [x] [Nextflow](https://nextflow.io)
  - [x] [Snakemake](https://snakemake.github.io/)
  - [ ] SAW NGW (proprietary)
  - [ ] Galaxy
  - [ ] WDL
  - [ ] Common Workflow Language (CWL)
  - [ ] Pegasus
  - [ ] Makefile

- Tests
  - [x] Repeatable crash-freedom?
  - [ ] If crashes, repeatable error-message?
  - [ ] If not crashes, repeatable bitwise-equivalent with holding zero, one, two, three, or four of {/dev/{,u}random, datetime, ASL, single-core}?
  - [ ] Repeatable 5--95%-ile interval?

- Code analysis
  - [ ] SLoC by type?
  - [ ] Dependency graph?
  - [ ] Component graph?
  - [ ] Similarity of experiments?
  - [ ] Detect presence of best practices?
    - Tools for reproducibility
    - Dependency count, transitive count, SLoC transitive count
    - Documentation to code ratio

- Data analysis:
  - [ ] Measure rate of collapse over time?
  - [ ] Similarity implies collapse co-occurrence?
  - [ ] Predict rate of collapse over time based on staleness, code anaylsis, history, and history of similar experiments?
  - [ ] Improve efficiency of continuous testing?
  - [ ] Cateogrize error messages?
  - [ ] Causes of collapse?
  - [ ] Design automatic fixes?
  - [ ] How many failures occur in a unit-testable component?
  - [ ] How effective is each non-determinism mitigation?

- Other questions:
  - [ ] Input minimization?
  - [ ] Compositional testing?

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for instructions on setting up a development environment.
