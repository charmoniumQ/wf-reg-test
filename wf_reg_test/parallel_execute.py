import contextlib
from pathlib import Path
from datetime import timedelta as TimeDelta, datetime as DateTime
from typing import Optional, Iterable, TypeVar, Callable, Generic, cast
import logging
import time
import queue

import parsl
import parsl.dataflow.futures
import tqdm

from .workflows import RegistryHub, Workflow, Revision, Condition, Execution
from .serialization import serialize
from .executable import Machine
from .engines import engines
from .util import expect_type


parsl_logger = logging.getLogger("parsl")
parsl_logger.setLevel(logging.WARNING)
parsl_logger.propagate = False

logger = logging.getLogger("wf_reg_test")

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")


class ResourcePool(Generic[_T]):
    def __init__(self, pool: list[_T]) -> None:
        self.pool = queue.Queue(len(pool))
        for elem in pool:
            self.pool.put_nowait(elem)

    @contextlib.contextmanager
    def get(self) -> Iterable[_T]:
        while True:
            try:
                elem = self.pool.get_nowait()
                break
            except queue.Empty:
                logger.info(f"Waiting on resource; queue has approx {self.pool.qsize()}")
                time.sleep(1)
        yield elem
        self.pool.put_nowait(elem)


def parsl_parallel_map(
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
    for i, future in enumerate(futures):
        print(i, len(futures))
        yield future.result()


def single_map(
        func: Callable[[ResourcePool[int], _T, _U], _V],
        args: list[tuple[_T, _U]],
        max_workers: int,
) -> Iterable[_V]:
    resource_pool = ResourcePool(list(range(max_workers)))
    return (
        func(resource_pool, arg0, arg1)
        for arg0, arg1 in args
    )


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
            single_map(
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
        revision.executions.append(execution)
        for warning in execution.check_invariants():
            # Halt execution quickly if something is wrong.
            raise warning
        # Must be no warnings. yay
        if last_serialization + serialize_every < DateTime.now():
            serialize(hub, data_path)


# time for SIGTERM to propagate before issuing SIGKILL
hard_wall_time_buffer = TimeDelta(minutes=2)


def execute_one(worker_ids: ResourcePool[int], revision: Revision, condition: Condition) -> Execution:
    with worker_ids.get() as worker_id:
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
        return ret
