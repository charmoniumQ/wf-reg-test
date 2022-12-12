import parsl
import os

parsl.load(parsl.config.Config(
    executors=parsl.executors.HighThroughputExecutor(
        provider=parsl.providers.AdHocProvider(
            channels=[
                parsl.channels.SSHChannel(hostname)
                for hostname in os.environ["PARSL_WORKERS"].split(",")
            ],
            # worker_init="source $HOME/spack/activate.sh",
            worker_init="source $HOME/spack/share/spack/setup-env.sh\nspack env activate wf-reg-test\n",
            parallelism=1,
        ),
        max_workers=parallelism,
    ),
))
