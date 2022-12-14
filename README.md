# wf-reg-test

Software tends to break or "collapse" over time, even if it is unchanged, due to non-obvious changes in the computational environment.
Collapse in computational experiments undermines long-term credibility and hinders day-to-day operations.
We propose to create the first public dataset of automatically executable scientific experiments.
This data could be used to identify best practices, make continuous testing feasible, and repair broken programs.
These techniques increase the replicability of computational experiments.

Conceptually, we intend to collect the following:

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
  - [ ] SLoC by type
  - [ ] Code-to-comment by type
  - [ ] Cyclomatic
  - [ ] Function length distribution
  - [ ] Dependency graph?
      - Imports per file
      - Total transitive dependencies
  - [ ] Component graph?
  - [ ] Similarity of experiments?
  - [ ] Detect presence of best practices?
    - Tools for reproducibility
    - Dependency count, transitive dependency count
	- SLoC count by language, transitive SLoC count by language
    - Documentation to code ratio

- Data analysis assumptions:
  - Assumption: Time symmetry
  - Assumption: Group and problem identity is constant and one-dimensional
  - Assumption: Versions are indistinguishable
    - Except possibly last version?
  - Caveat: predictor != intervention
  - Caveat: predictor only works with unawareness of its use as a predictor
    - https://en.wikipedia.org/wiki/Goodhart%27s_law
    - https://en.wikipedia.org/wiki/Lucas_critique
  - Analysis question: Do input variables predict rate of decay or do input variables + staleness predict failure?
  - Analysis question: between levels of reproducibility
    - Set of factors are necessary and sufficient for reproducibility
    - Successful termination
    - {Faketime, fake random, ASLR}
    - Multi-threaded
  - Analysis question: Model infant mortality or constant rate of failure?

- Data analysis:
  - [ ] Measure rate of collapse over time?
      - Coefficient of staleness on successful termination
  - [ ] Predictive accuracy of collapse over time based on staleness, code anaylsis, and optionally history?
      - How to use information from other simultaneously failing workflows?
  - [ ] How effective is each non-determinism mitigation?
    - `R` / `total`
    - `R_easy` / `total`
	- `R_multi` / `total`
    - `R_all` / `total`
  - [ ] Improve efficiency of continuous testing in simulation?
      - Generate time-to-collapse
      - How to use information from other simultaneously failing workflows?
  - [ ] Code best practices
    - Influence of code metrics on decay rate, `R_easy`, (`R_all` given not `R_easy`)
    - Interaction between code metrics on rate of decay?

- Other questions:
  - [ ] Cluster error messages?
  - [ ] Replicate Zhao's categories?
  - [ ] Design automatic fixes?
  - [ ] Outcome preserving input minimization?
    - https://seg.inf.unibe.ch/papers/ase22.pdf
  - [ ] How many failures occur in a unit-testable component?
  - [ ] Compositional testing?

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for instructions on setting up a development environment.
