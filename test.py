import os
from pathlib import Path

import parsl

from wf_reg_test.util import expect_type, create_temp_dir

@parsl.python_app
def foo1(x: int) -> int:
    return x**2

def bar1():
    @parsl.python_app
    def foo2(x: int) -> int:
        return x**2

    print(foo2(3).result())

def foo3(x: int) -> int:
    return x**2

def bar2():
    @parsl.python_app
    def foo4(x: int) -> int:
        from test import foo3
        return foo3(x)

    print(foo4(3).result())

from wf_reg_test.workflows import Workflow, Revision, Condition
from wf_reg_test.serialization import deserialize
from wf_reg_test.engines import engines

data_path = Path("data")

def bar3():
    pass

import upath

def foo7(revision: Revision, condition: Condition, storage: upath.UPath) -> str:
    workflow = expect_type(Workflow, revision.workflow)
    registry = workflow.registry
    print(workflow.display_name, registry.display_name, revision.display_name)
    engine = engines[workflow.engine]
    with create_temp_dir() as path:
        return engine.run(
            revision=revision,
            condition=condition,
            path=path,
            which_cores=[0, 1],
            wall_time_limit=workflow.max_wall_time_estimate(),
            storage=storage,
        )

def bar4():
    hub = deserialize(data_path)
    @parsl.python_app
    def foo6(revision: Revision, condition: Condition, storage: upath.UPath) -> str:
        from test import foo7
        return foo7(revision, condition, storage)

    revision = hub.registries[0].workflows[0].revisions[0]
    import azure.identity.aio
    storage = upath.UPath(
        "abfs://data/",
        account_name="wfregtest",
        credential=azure.identity.aio.ManagedIdentityCredential()
    )
    print(foo6(revision, Condition.NO_CONTROLS, storage).result())

if __name__ == "__main__":
    exec(Path(os.environ["PARSL_CONFIG"]).read_text(), {**globals(), "parallelism": 1}, locals())
    print(foo1(3).result())
    bar1()
    bar2()
    bar3()
    bar4()
