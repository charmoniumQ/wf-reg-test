import parsl
import os

parsl.load(parsl.config.Config(
    executors=[
        parsl.executors.HighThroughputExecutor(
            provider=parsl.providers.AdHocProvider(
                channels=[
                    parsl.channels.SSHChannel(hostname, script_dir="/home/azureuser/parsl")
                    for hostname in os.environ["PARSL_WORKERS"].split(",")
                ],
                worker_init="source $HOME/spack/activate.sh\nexport PYTHONPATH=$HOME/wf-reg-test:$PYTHONPATH\n",
                parallelism=1,
            ),
        ),
    ],
   # monitoring=parsl.monitoring.MonitoringHub(
   #     hub_address=parsl.addresses.address_by_hostname(),
   #     hub_port=55055,
   #     monitoring_debug=False,
   #     resource_monitoring_interval=10,
   # ),
))
