# Reproducing

Note that this software invokes software which creates containers, so it might or might not work inside a container. We avoid the problem of nested containers by running this software on bare-metal.

1. Install the Spack package manager. See [here][spack] for more details. Note that I am using 0.20.0.dev0 (68b711c1ad7157930154fc37f4a912aaf325fbfb) of Spack. Spack itself has some [prerequisites][spack-prereqs], although they should be present in the default repository of Ubuntu or any other Linux distribution. Spack will bootstrap as much of its own tools as possible, so system-level dependencies do not leak into the environment.

[spack]: https://spack.readthedocs.io/en/latest/getting_started.html#installation
[spack-prereqs]: https://spack.readthedocs.io/en/latest/getting_started.html#system-prerequisites

```bash
$ # If this is a Debian-based system,
$ sudo apt-get update && sudo apt-get install -y build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv unzip zip
$ # Otherwise, find those dependencies some other way.

$ git clone -c feature.manyFiles=true https://github.com/spack/spack.git
$ source spack/share/spack/setup-env.sh
```

2. Install this environment with Spack.

[spack-external-find]: https://spack.readthedocs.io/en/latest/build_settings.html#cmd-spack-external-find

```bash
$ git clone https://github.com/charmoniumQ/wf-reg-test
$ spack repo add wf-reg-test/spack/spack_repo
$ spack env create wf-reg-test wf-reg-test/spack/spack.yaml
$ spack env activate wf-reg-test
$ spack install
$ sudo $(which spack_perms_fix.sh)
```

Note that this may take up to an hour, as it builds all dependencies from source. You can skip building an item from source using the [spack extrnal][spack-external-find]. For example,

```bash
$ sudo apt-get install -y golang-go
$ spack external find go

$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
$ spack external find rust
```

The `spack_perms_fix.sh` command requires super-user priveleges because, Singularity with setuid, requires its configuration to be owned by root. If you do not have super-user priveleges, ask your system administrator to run this command or to provide Singularity with setuid, which you can use `spack external find singularity` to pick up.

3. Configure the paths in `wf_reg_test/config.py` to point to the desired destination for results. These can be any `pathlib.Path` or `upath.UPath` objects. In my configuration, I am using Azure Blob Storage as a file system. If you want to use local files, write `pathlib.Path("/path/to/directory")`, where the directory should already exist. If you want to deploy to Azure, consider using the terraform scripts in `./terraform`.

4. Generate the list of workflows and revisiosn. This should only a few seconds. At this point the `index_path` will be populated with YAML files describing the registries, workflows, and revisions of those workflows. You can skip this step by extracting the `index.zip` into `index_path`.

You will need a GitHub Personal Access Token, and allow it read-only access to public reposiotries. Export the token as an environment variable. This is quite easy if you have a normal GitHub account at this [link](https://github.com/settings/tokens?type=beta).

```bash
$ cd wf-reg-test/
$ GITHUB_ACCESS_TOKEN=github_pat_XXXX python -m wf_reg_test regenerate
```

5. Run each version of each workflow. This will take days on a single core. If this script terminates for any reason, you can restart it to pick up where it left off. You can skip this step by extracting the `index.zip` into `index_path`.

```bash
$ cd wf-reg-test/
$ python -m wf_reg_test test
```

To just run a few workflows as a test, pass `python -m wf_reg_test test --max-executions 10`, which just runs 10. The next time you execute this command, it will run the _next_ 10 that have not already been run.

If you want to run in parallel using Parsl, set `PARSL_CONFIG` to a file that executes `parsl.load(parsl.config.Config(...))`. See the examples in `./parsl_configs/`. Of course, the parallel workers will need access to the same Spack environment and same code as this node. See `./spack/*.sh` for how I do that. If you want to run on Azure, see the scripts in `./terraform`.

6. At any time after step 4 (even during step 5), run `python -m wf_reg_test report` to get a report on the results in `$index_path/results.html`.

Be sure to check that the workers are not running out of disk space periodically. If they are, you can use `python -m wf_reg_test retest --predicate 'HERE'` to rerun just those failing workflows, replacing `HERE` with a Python expression which selects the revisions you wish to re-execute. For example, if you want to rerun the timed out executions with a larger limit, change the limit and run `python -m wf_reg_test retest --predicate 'execution.resources.wall_time > TimeDelta(seconds=old_limit) and not execution.successful'`
