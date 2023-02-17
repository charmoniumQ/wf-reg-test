import parsl

parsl.load(parsl.config.Config(
    executors=[
        parsl.executors.ThreadPoolExecutor(),
    ],
))
