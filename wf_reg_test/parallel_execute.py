from pathlib import Path
from datetime import timedelta as TimeDelta, datetime as DateTime
from typing import Optional, Iterable, TypeVar, Callable, Generic, cast

import parsl
import parsl.dataflow.futures
import tqdm

from .workflows import RegistryHub, Workflow, Revision, Condition, Execution
from .serialization import serialize
from .executable import Machine
from .engines import engines
from .util import expect_type


_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")


class ResourcePool(Generic[_T]):
    def __init__(self, pool: list[_T]) -> None:
        self.pool = pool

    def get(self) -> _T:
        return self.pool.pop()

    def put(self, elem: _T) -> None:
        self.pool.append(elem)


def parallel_map(
        func: Callable[[ResourcePool[int], _T, _U], _V],
        args: list[tuple[_T, _U]],
        max_workers: int,
) -> Iterable[_V]:
    parsl.load(parsl.config.Config(
        executors=[
            parsl.executors.ThreadPoolExecutor(
                max_threads=max_workers,
            ),
        ],
        app_cache=False,
    ))
    resource_pool = ResourcePool(list(range(max_workers)))
    futures: list[parsl.dataflow.futures.AppFuture] = [
        parsl.python_app(func)(resource_pool, *arg)
        for arg in args
    ]
    for future in futures:
        yield future.result()


def parallel_execute(
    hub: RegistryHub,
    revisions_conditions: list[tuple[Revision, Condition]],
    data_path: Path,
    processes: int,
    serialize_every: TimeDelta = TimeDelta(minutes=5),
) -> None:
    iterator = tqdm.tqdm(
        zip(
            revisions_conditions,
            parallel_map(
                execute_one,
                revisions_conditions,
                max_workers=processes // 2,
            ),
        ),
        total=len(revisions_conditions),
        desc="executing",
    )
    last_serialization = DateTime.now()
    for (revision, _), execution in iterator:
        execution = execution.with_pointers(
            machine=Machine.current_machine(),
            revision=revision,
        )
        for warning in execution.check_invariants():
            # Halt execution quickly if something is wrong.
            raise warning
        # Must be no warnings. yay
        if last_serialization + serialize_every < DateTime.now():
            serialize(hub, data_path)


# time for SIGTERM to propagate before issuing SIGKILL
hard_wall_time_buffer = TimeDelta(minutes=1)


def execute_one(worker_ids: ResourcePool[int], revision: Revision, condition: Condition) -> Execution:
    worker_id = worker_ids.get()
    cache_path = Path(".repos") / str(worker_id)
    cache_path.mkdir(exist_ok=True, parents=True)
    which_cores = [worker_id * 2] if condition.single_core else [worker_id * 2, worker_id * 2 + 1]
    workflow = expect_type(Workflow, revision.workflow)
    engine = engines[workflow.engine]
    ret = engine.run(
        revision=revision,
        condition=condition,
        repo_cache_path=cache_path,
        which_cores=which_cores,
        wall_time_soft_limit=workflow.max_wall_time_estimate(),
        wall_time_hard_limit=workflow.max_wall_time_estimate() + hard_wall_time_buffer,
    )
    worker_ids.put(worker_id)
    return ret
