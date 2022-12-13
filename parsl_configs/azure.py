import parsl
import os

parallelisum = 1

parsl.load(parsl.config.Config(
    executors=[
        parsl.executors.HighThroughputExecutor(
            provider=parsl.providers.AdHocProvider(
                channels=[
                    parsl.channels.SSHChannel(hostname, script_dir="/home/azureuser")
                    for hostname in os.environ["PARSL_WORKERS"].split(",")
                ],
                worker_init="source $HOME/spack/activate.sh",
                parallelism=1,
            ),
            max_workers=parallelism,
        ),
    ],
))

@parsl.python_app
def f(x):
    return x**2
print(f(3).result())

@parsl.python_app
def g():
    import platform
    return platform.node()
print(g().result())
