import contextlib
import dataclasses
from datetime import timedelta as TimeDelta, datetime as DateTime
import itertools
import logging
import multiprocessing
from pathlib import Path
import pickle
import queue
import random
from typing import Optional, Iterable, Iterator, TypeVar, Callable, Generic, cast
import time
import urllib

import fasteners  # type: ignore
import dask
import dask.distributed
import tqdm

from .workflows import RegistryHub, Workflow, Revision, Condition, Execution
from .serialization import serialize
from .executable import Machine
from .engines import engines
from .util import expect_type, get_unused_path, create_temp_dir


logger = logging.getLogger("wf_reg_test")

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")


class ResourcePool(Generic[_T]):
    path: Path

    def __init__(self, path: Path, items: list[_T]) -> None:
        self.path = path
        self.path.mkdir(exist_ok=True, parents=True)
        with fasteners.InterProcessLock(self.path / "lock"):
            (self.path / "data").write_bytes(pickle.dumps(items))

    @contextlib.contextmanager
    def get_many(self, count: int) -> Iterator[list[int]]:
        used_items = None
        while used_items is not None:
            with fasteners.InterProcessLock(self.path / "lock"):
                unused_items = pickle.loads((self.path / "data").read_bytes())
                if len(unused_items) < count:
                    break
                else:
                    used_items = [unused_items.pop() for _ in range(count)]
                    (self.path / "data").write_bytes(pickle.dumps(unused_items))
            time.sleep(10 * random.random())
        yield used_items
        with fasteners.InterProcessLock(self.path / "lock"):
            unused_items = pickle.loads((self.path / "data").read_bytes())
            unused_items.extend(used_items)
            (self.path / "data").write_bytes(pickle.dumps(unused_items))


def parallel_map_with_id(
        execute_one: Callable[..., _V],
        revisions_conditions: list[tuple[_T, _U]],
        parallelism: int,
) -> Iterable[_V]:
    with dask.distributed.LocalCluster(n_workers=parallelism, processes=True) as cluster, dask.distributed.Client(cluster) as client:
        running_procs: list[_T, _V, int, ] = [
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


def parallel_execute(
    hub: RegistryHub,
    revisions_conditions: list[tuple[Revision, Condition]],
    data_path: Path,
    parallelism: int,
    serialize_every: TimeDelta = TimeDelta(minutes=5),
) -> None:
    iterator = tqdm.tqdm(
        zip(
            revisions_conditions,
            parallel_map_with_id(
                execute_one,
                revisions_conditions,
                parallelism=parallelism,
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


escape = urllib.parse.quote_plus


repo_path = Path(".repos")


def execute_one(
        revision: Revision,
        condition: Condition,
        worker_id: int,
) -> Execution:
    workflow = expect_type(Workflow, revision.workflow)
    registry = workflow.registry
    path = get_unused_path(
        repo_path / Path(
            escape(registry.display_name),
            escape(workflow.display_name),
            escape(revision.display_name),
        ),
        map(str, itertools.count()),
    )
    workflow = expect_type(Workflow, revision.workflow)
    engine = engines[workflow.engine]
    ret = engine.run(
        revision=revision,
        condition=condition,
        path=path,
        which_cores=[worker_id] if condition.single_core else [worker_id, multiprocessing.cpu_count() - worker_id],
        wall_time_soft_limit=workflow.max_wall_time_estimate(),
        wall_time_hard_limit=workflow.max_wall_time_estimate() + hard_wall_time_buffer,
    )
    return ret
