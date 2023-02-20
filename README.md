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

See [`REPRODUCING.md`](REPRODUCING.md) for instructions on reproducing these results.

# TODO

See [`TODO.md`](TODO.md) for instructions on reproducing these results.

# Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for instructions on setting up a development environment.
