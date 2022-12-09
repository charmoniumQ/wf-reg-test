import parsl
import os

parsl.load(parsl.config.Config(
    executors=parsl.executors.HighThroughputExecutor(
        provider=parsl.providers.AdHocProvider(
            channels=[
                parsl.channels.SSHChannel(hostname)
                for hostname in os.environ["PARSL_WORKERS"].split(",")
            ],
            worker_init="source $HOME/spack/activate.sh",
            parallelism=1,
        )
        max_workers=parallelism,
    )
))
