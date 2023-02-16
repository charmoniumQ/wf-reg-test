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

# Reproducing

1. Install the Spack package manager. See [here][spack] for more details. Note that I am using 0.20.0.dev0 (68b711c1ad7157930154fc37f4a912aaf325fbfb) of Spack. Spack itself has some [prerequisites][spack-prereqs], although they should be present on stock Ubuntu or any other Linux distribution. Spack will bootstrap as much of its own tools as possible, so these system-level dependencies do not leak into the environment.

[spack]: https://spack.readthedocs.io/en/latest/getting_started.html#installation
[spack-prereqs]: https://spack.readthedocs.io/en/latest/getting_started.html#system-prerequisites

```bash
$ git clone -c feature.manyFiles=true https://github.com/spack/spack.git
$ source spack/share/spack/setup-env.sh
```

2. Install this environment with Spack.

[spack-external-find]: https://spack.readthedocs.io/en/latest/build_settings.html#cmd-spack-external-find

```bash
$ git clone https://github.com/charmoniumQ/wf-reg-test
$ spack repo add wf-reg-test/spack/spack_repo
$ spack env create wf-reg-test wf-reg-test/spack/spack.yaml
$ spack concretize
$ spack install
$ spack env activate wf-reg-test
$ sudo $(which spack_perms_fix.sh)
```

Note that this may take up to an hour to build everything from source. You can skip building an item from source using the [spack extrnal][spack-external-find].

The last command requires super-user priveleges because, Singularity, requires its configuration to be owned by root. If you do not have super-user priveleges, ask your system administrator to run this command or to provide Singularity with setuid, which you can use `spack external find` to pick up.

3. Configure the paths in `wf_reg_test/__main__.py` to point to the desired destination for results. These can be any `pathlib.Path` or `upath.UPath` objects. In my configuration, I am using Azure Blob Storage as a file system. If you want to use local files, write `pathlib.Path("/path/to/directory")`, where the directory should already exist. If you want to deploy to Azure, consider using the terraform scripts in `./terraform`. You will also need to get a GitHub Personal Access Token, and allow it read-only access to public reposiotries. Export the token as an environment variable.

4. Generate the list of workflows and revisiosn. This should only a few seconds. At this point the `index_path` will be populated with YAML files describing the registries, workflows, and revisions of those workflows.

```bash
$ cd wf-reg-test/
$ GITHUB_ACCESS_TOKEN=github_pat_XXXX python -m wf_reg_test regenerate
```

5. Run each version of each workflow. This will take days. If this script terminates for any reason, you can restart it to pick up where it left off.

```bash
$ cd wf-reg-test/
$ python -m wf_reg_test test
```

If you want to run in parallel using Parsl, set `PARSL_CONFIG` to a file that executes `parsl.load(parsl.config.Config(...))`. See the examples in `./parsl_configs/`. Of course, the parallel workers will need access to the same Spack environment and same code as this node. See `./spack/*.sh` for how I do that. If you want to run on Azure, see the scripts in `./terraform`.

6. At any time after step 4 (even during step 5), run `python -m wf_reg_test report` to get a report on the results in `$index_path/results.html`.

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
