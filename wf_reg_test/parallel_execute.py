import contextlib
import dataclasses
from datetime import timedelta as TimeDelta, datetime as DateTime
import itertools
import logging
import multiprocessing
import os
from pathlib import Path
import pickle
import queue
import random
from typing import Any, Optional, Iterable, Iterator, TypeVar, Callable, Generic, cast
import time
import urllib

import fasteners  # type: ignore
import tqdm
from upath import UPath

from .workflows import RegistryHub, Workflow, Revision, Condition, Execution
from .serialization import serialize
from .executable import Machine
from .engines import engines
from .util import expect_type, get_unused_path, create_temp_dir, create_temp_file


logger = logging.getLogger("wf_reg_test")

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")


class ResourcePool(Generic[_T]):
    path: Path

    def __init__(self, path: Path, items: list[_T]) -> None:
        self.path = path
        self.path.mkdir(exist_ok=True, parents=True)
        self.thread_lock = fasteners.ReaderWriterLock()
        self.process_lock = fasteners.InterProcessLock(self.path / "lock")
        with self.thread_lock.write_lock(), self.process_lock:
            (self.path / "data").write_bytes(pickle.dumps(items))

    @contextlib.contextmanager
    def get_many(self, count: int, delay: float) -> Iterator[list[int]]:
        used_items: Optional[list[int]] = None
        while True:
            with self.thread_lock.write_lock(), self.process_lock:
                unused_items = cast(list[int], pickle.loads((self.path / "data").read_bytes()))
                if len(unused_items) >= count:
                    used_items = unused_items[:count]
                    unused_items = unused_items[count:]
                    (self.path / "data").write_bytes(pickle.dumps(unused_items))
                    break
            logger.info(f"Spinning, while waiting for {count} resources")
            os.sync()
            time.sleep(delay * random.random())
        assert used_items is not None
        yield used_items
        with self.thread_lock.write_lock(), self.process_lock:
            unused_items = pickle.loads((self.path / "data").read_bytes())
            unused_items.extend(used_items)
            (self.path / "data").write_bytes(pickle.dumps(unused_items))


def dask_parallel_map_with_id(
        execute_one: Callable[..., _V],
        revisions_conditions: list[tuple[_T, _U]],
        parallelism: int,
) -> Iterable[tuple[_T, _U, _V]]:
    with dask.distributed.LocalCluster(n_workers=parallelism, processes=True) as cluster, dask.distributed.Client(cluster) as client:  # type: ignore
        running_procs: list[tuple[_T, _U, int, Any]] = [
            (
                revision,
                condition,
                c,
                client.submit(execute_one, revision, condition, c),
            )
            for c, (revision, condition) in enumerate(revisions_conditions[:parallelism])
        ]
        waiting = revisions_conditions[parallelism:]
        all_done = False
        while not all_done:
            all_done = True
            for i, (revision, condition, c, future) in enumerate(running_procs):
                if future is not None:
                    all_done = False
                    if future.status == "finished":
                        yield (revision, condition, future.result())
                        if waiting:
                            revision, condition = waiting.pop()
                            running_procs[i] = (
                                revision,
                                condition,
                                c,
                                client.submit(execute_one, revision, condition, c)
                            )
                        else:
                            running_procs[i] = (revision, condition, c, None)
            time.sleep(0.5)


import concurrent
import parsl
def parsl_parallel_map_with_id(
        execute_one: Callable[[_T, _U, Optional[ResourcePool[int]]], _V],
        ts_vs: list[tuple[_T, _U]],
        parallelism: int,
        oversubscribe: bool,
        remote: bool,
        **kwargs: Any,
) -> Iterable[tuple[_T, _U, _V]]:
    with create_temp_dir() as temp_dir:
        # Note, I am using a tuple instead of a list because tuples are covariant.
        exec(Path(os.environ["PARSL_CONFIG"]).read_text(), globals(), locals())
        if oversubscribe:
            raise NotImplementedError("Oversubscribe is not implemented for multi-node deployments yet.")
            @parsl.python_app
            def _execute_one(idx: int, pool: ResourcePool[int]) -> tuple[int, _V]:
                t, v = ts_vs[idx]
                return idx, execute_one(t, v, pool, **kwargs)
            core_pool = ResourcePool(temp_dir, list(range(multiprocessing.cpu_count())))
            futures = [_execute_one(idx, core_pool) for idx in range(len(ts_vs))]
        else:
            @parsl.python_app
            def _execute_one(idx: int) -> tuple[int, _V]:
                return None
                t, v = ts_vs[idx]
                return idx, execute_one(t, v, None, **kwargs)
            futures = [_execute_one(idx) for idx in range(len(ts_vs))]
        for future in concurrent.futures.as_completed(futures):
            idx, u = future.result()
            t, v = ts_vs[idx]
            yield t, v, u


parallel_map_with_id = parsl_parallel_map_with_id


def parallel_execute(
    hub: RegistryHub,
    revisions_conditions: list[tuple[Revision, Condition]],
    data_path: Path,
    parallelism: int,
    oversubscribe: bool,
    remote: bool,
    storage: UPath,
    serialize_every: TimeDelta = TimeDelta(minutes=5),
) -> None:
    iterator = tqdm.tqdm(
        parallel_map_with_id(
            execute_one,
            revisions_conditions,
            parallelism=parallelism,
            oversubscribe=oversubscribe,
            remote=remote,
            storage=storage,
        ),
        total=len(revisions_conditions),
        desc="executing",
    )
    last_serialization = DateTime.now()
    for (revision, _condition, execution) in iterator:
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


escape = urllib.parse.quote_plus


repo_path = Path(".repos")


def execute_one(
        revision: Revision,
        condition: Condition,
        core_pool: Optional[ResourcePool[int]],
        storage: Optional[UPath] = None,
) -> Execution:
    if storage is None:
        raise RuntimeError()
    workflow = expect_type(Workflow, revision.workflow)
    registry = workflow.registry
    print(workflow.display_name, registry.display_name, revision.display_name)
    engine = engines[workflow.engine]
    if core_pool is not None:
        with core_pool.get_many(1 if condition.single_core else 2, delay=10) as cores:
            return engine.run(
                revision=revision,
                condition=condition,
                which_cores=cores,
                wall_time_limit=workflow.max_wall_time_estimate(),
                storage=storage,
            )
    else:
        return engine.run(
            revision=revision,
            condition=condition,
            which_cores=[0] if condition.single_core else [0, 1],
            wall_time_limit=workflow.max_wall_time_estimate(),
            storage=storage,
        )
