import os
from pathlib import Path

import parsl

from wf_reg_test.util import expect_type

exec(Path(os.environ["PARSL_CONFIG"]).read_text(), globals(), locals())

@parsl.python_app
def foo1(x: int) -> int:
    return x**2

print(foo1(3).result())

def bar1():
    @parsl.python_app
    def foo2(x: int) -> int:
        return x**2

    print(foo2(3).result())

bar1()

def foo3(x: int) -> int:
    return x**2

def bar2():
    @parsl.python_app
    def foo4(x: int) -> int:
        return foo3(expect_type(int, x))

    print(foo3(3).result())

bar2()

from wf_reg_test.workflows import Workflow
from wf_reg_test.engines import engines

def bar3():
    hub = deserialize(data_path)
    @parsl.python_app
    def foo5(revision: Revision) -> str:
        workflow = expect_type(Workflow, revision.workflow)
        registry = workflow.registry
        print(workflow.display_name, registry.display_name, revision.display_name)
        return str(engines[workflow.engine])

    revision = hub.registries[0].workflows[0].revisions[0]
    print(foo5(revision).result())

bar3()

from upath import UPath
from wf_reg_test.workflows import Condition

def bar4():
    hub = deserialize(data_path)
    @parsl.python_app
    def foo6(revision: Revision, condition: Condition, storage: UPath) -> str:
        workflow = expect_type(Workflow, revision.workflow)
        registry = workflow.registry
        print(workflow.display_name, registry.display_name, revision.display_name)
        return engine.run(
            revision=revision,
            condition=condition,
            path=path,
            which_cores=[0],
            wall_time_limit=workflow.max_wall_time_estimate(),
            storage=storage,
        )

    revision = hub.registries[0].workflows[0].revisions[0]
    storage = UPath("./tmp")
    print(foo6(revision, Condition.NO_CONTROLS, storage).result())

bar4()
