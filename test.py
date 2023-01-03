import os
from pathlib import Path

import parsl
import upath

from wf_reg_test.util import expect_type, create_temp_dir

from wf_reg_test.workflows import Workflow, Revision, Condition
from wf_reg_test.serialization import deserialize
from wf_reg_test.engines import engines

def foo7(revision: Revision, condition: Condition, storage: upath.UPath) -> str:
    workflow = expect_type(Workflow, revision.workflow)
    registry = workflow.registry
    engine = engines[workflow.engine]
    return engine.run(
        revision=revision,
        condition=condition,
        which_cores=[0, 1],
        wall_time_limit=workflow.max_wall_time_estimate(),
        storage=storage,
    )

from typing import Generic, TypeVar, Callable, Any

def wrap(outer: Any, inner: T) -> T:
    def proxy_wrap(attr):
        "This method creates a proxy method that calls the wrappee's method."
        def f(self, *args):
            return getattr(self.wrappee, attr)(*args)
        return f
    # Don't overwrite any attributes already present
    exclude = set(dir(outer))
    # Watch out for this one...
    exclude.add('__class__')
    for (attr, value) in inspect.getmembers(inner, callable):
        if attr not in EXCLUDE:
            setattr(Wrapper, attr, proxy_wrap(attr))

_T = TypeVar("_T")

class ThunkObject(wrapt.ObjectProxy):
    def __init__(self, thunk: Callable[[], _T]) -> None:
        self._thunk = thunk
        self._value = None

    def __getattr__(self, attr: str) -> Any:
        if self._value is None:
            self._value = self._thunk()
            
            assert self._value is not None
        return getattr(self._value, attr)

    def __getstate__(self) -> None:
        return self._thunk

    def __setstate__(self, thunk: Callable[[], _T]) -> None:
        self._thunk = thunk


if __name__ == "__main__":
    exec(Path(os.environ["PARSL_CONFIG"]).read_text(), {**globals(), "parallelism": 1}, locals())
    data_path = Path("data")
    hub = deserialize(data_path)
    revision = hub.registries[0].workflows[0].revisions[0]
    storage = lambda: __import__("upath").UPath(
        "abfs://data/",
        account_name="wfregtest",
        credential=__import__("azure.identity.aio").identity.aio.ManagedIdentityCredential(),
    )

    @parsl.python_app
    def foo6(revision: Revision, condition: Condition, storage: Callable[upath.UPath]) -> str:
        from test import foo7
        return foo7(revision, condition, storage())
    print(foo6(revision, Condition.NO_CONTROLS, storage).result())
