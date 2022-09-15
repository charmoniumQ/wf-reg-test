from __future__ import annotations

import abc
import logging
import platform
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, ClassVar, ContextManager, Optional, cast

import sqlalchemy
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Interval,
    LargeBinary,
    String,
    Boolean,
)
from sqlalchemy.orm import Mapped, Session, declarative_base, deferred, relationship

from .util import hash_bytes, hash_path, walk

Base = declarative_base()

logger = logging.getLogger()

URL_SIZE = 127
HUMAN_READABLE_NAME_SIZE = 63

# TODO: think long and hard about cascading deletes
# TODO: remove underscore from id


class WorkflowApp(Base):
    __tablename__ = "WorkflowApp"
    _id = Column(Integer, primary_key=True)
    workflow_engine_name: Mapped[str] = Column(
        String(HUMAN_READABLE_NAME_SIZE), nullable=False
    )
    url: Mapped[str] = Column(String(URL_SIZE), nullable=False)
    display_name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    repo_url: Mapped[str] = Column(String(URL_SIZE), nullable=False)
    revisions: Mapped[Revision] = relationship(
        "Revision", order_by="Revision.datetime", back_populates="workflow_app"
    )
    def __str__(self) -> str:
        return f"WorkflowApp {self.display_name}"


class RepoAccessor(abc.ABC):
    @abc.abstractmethod
    def get_revisions(self) -> list[Revision]:
        ...

    @abc.abstractmethod
    def checkout(self, url: str) -> ContextManager[Path]:
        ...


class Revision(Base):
    __tablename__ = "Revision"
    _id = Column(Integer, primary_key=True)
    display_name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    url: Mapped[str] = Column(String(URL_SIZE), nullable=False, unique=True)
    datetime: Mapped[datetime] = Column(DateTime, nullable=False)
    tree: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    _tree_hash = Column(BigInteger, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    executions: Mapped[list[Execution]] = relationship(
        "Execution",
        order_by="Execution.datetime",
        back_populates="revision",
    )
    _workflow_app_id = Column(Integer, ForeignKey("WorkflowApp._id"), nullable=False)
    workflow_app: Mapped[WorkflowApp] = relationship(
        "WorkflowApp", back_populates="revisions"
    )

    def __str__(self) -> str:
        return f"Revision {self.display_name} of {self.workflow_app}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Revision):
            return self.url == other.url
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.url)


class Execution(Base):
    __tablename__ = "Execution"

    _id = Column(Integer, primary_key=True)
    _revision_id = Column(Integer, ForeignKey("Revision._id"), nullable=False)
    revision: Mapped[Revision] = relationship("Revision", back_populates="executions")
    _machine_id = Column(Integer, ForeignKey("Machine._id"), nullable=False)
    machine: Mapped[Machine] = relationship("Machine")
    datetime: Mapped[datetime] = Column(DateTime, nullable=False)
    output: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    _output_hash = Column(BigInteger, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    status_code: Mapped[int] = Column(Integer, nullable=False)
    user_cpu_time: Mapped[timedelta] = Column(Interval, nullable=False)
    system_cpu_time: Mapped[timedelta] = Column(Interval, nullable=False)
    max_rss: Mapped[int] = Column(Integer, nullable=False)
    wall_time: Mapped[timedelta] = Column(Interval, nullable=False)

    def __str__(self) -> str:
        return f"Execution {self._id} of {self.revision}"


class Machine(Base):
    __tablename__ = "Machine"
    _id = Column(Integer, primary_key=True)
    short_description: Mapped[str] = Column(String(128), nullable=False, unique=True)
    long_description: Mapped[str] = deferred(Column(String(102400), nullable=False))

    def __str__(self) -> str:
        return f"Machine {self.short_description}"

    CURRENT_MACHINE: ClassVar[Optional[Machine]] = None

    @staticmethod
    def current_host(
        session: Session,
    ) -> Machine:
        short_description = "-".join(
            [
                platform.node(),
                platform.platform(),
            ]
        )
        if Machine.CURRENT_MACHINE is not None:
            return Machine.CURRENT_MACHINE

        existing_in_db = cast(
            Machine,
            session.execute(
                sqlalchemy.select(Machine).where(
                    Machine.short_description == short_description
                )
            )
            .scalars()
            .one_or_none(),
        )
        if existing_in_db is not None:
            return existing_in_db

        Machine.CURRENT_MACHINE = Machine(
            short_description=short_description,
            long_description=subprocess.run(
                ["lstopo", "--output-format", "xml"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout,
        )
        return Machine.CURRENT_MACHINE


class MerkleTreeNode(Base):
    __tablename__ = "MerkleTreeNode"
    hash: Mapped[int] = Column(BigInteger, primary_key=True, autoincrement=False)
    name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    _parent_hash = Column(BigInteger, ForeignKey("MerkleTreeNode.hash"))
    # parent: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode", back_populates="children", remote_side="hash")
    children: Mapped[list[MerkleTreeNode]] = relationship(
        "MerkleTreeNode",
        # back_populates="parent",
    )  # TODO: make this relationship a dict
    blob: Mapped[Optional[Blob]] = relationship("Blob")
    _blob_hash = Column(BigInteger, ForeignKey("Blob.hash"))
    # size_of_descendents = Column(Integer)
    # updated = Column(Boolean)

    @staticmethod
    def from_path(
        path: Path,
        session: Session,
        nodes_in_transaction: dict[int, MerkleTreeNode],
        blobs_in_transaction: dict[int, Blob],
    ) -> MerkleTreeNode:
        return walk(
            MerkleTreeNode._from_path(
                session=session,
                nodes_in_transaction=nodes_in_transaction,
                blobs_in_transaction=blobs_in_transaction,
            ),
            path,
        )

    @staticmethod
    def _from_path(
        session: Session,
        nodes_in_transaction: dict[int, MerkleTreeNode],
        blobs_in_transaction: dict[int, Blob],
    ) -> Callable[[Path, list[MerkleTreeNode]], MerkleTreeNode]:
        def inner(path: Path, children: list[MerkleTreeNode]) -> MerkleTreeNode:
            # TODO: capture children names in parent rather than child

            if path.is_dir():
                blob = None
                hash_contents = b"".join(
                    f"{path!s}/{child.name}:{child.hash:016x}".encode()
                    for child in sorted(children, key=lambda child: child.hash)
                )
            else:
                blob = Blob.from_path(path, blobs_in_transaction, session)
                hash_contents = f"{path!s}:{blob.hash:08x}".encode()

            hash = hash_bytes(hash_contents, size=64) - (1 << 63)

            existing_in_transaction = nodes_in_transaction.get(hash)
            if existing_in_transaction:
                return existing_in_transaction

            existing_in_db = session.get(MerkleTreeNode, hash)
            if existing_in_db:
                nodes_in_transaction[hash] = existing_in_db
                return existing_in_db

            ret = MerkleTreeNode(
                name=path.name if path.name else ".",
                children=children,
                hash=hash,
                blob=blob,
                # size_of_descendents=blob.size + sum([child.size_of_descendents for child in children]),
            )
            return ret

        return inner

    def list_children(self, prefix: str = "") -> str:
        new_prefix = prefix + "/" + self.name if prefix else self.name
        return (
            new_prefix
            + "\n"
            + "".join([child.list_children(new_prefix) for child in self.children])
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MerkleTreeNode):
            return self.hash == other.hash
        else:
            return False

    def __hash__(self) -> int:
        return self.hash

    def __str__(self) -> str:
        return f"MerkleTreeNode {self.name}"


class Blob(Base):
    __tablename__ = "Blob"
    hash: Mapped[int] = Column(BigInteger, primary_key=True, autoincrement=False)
    data: Mapped[bytes] = deferred(Column(LargeBinary, nullable=False))
    # size: int = Column(Integer)

    def __str__(self) -> str:
        return f"Blob {self.hash}"

    @staticmethod
    def from_path(
        path: Path, blobs_in_transaction: dict[int, Blob], session: Session
    ) -> Blob:
        hash = hash_path(path, size=64) - (1 << 63)

        existing_in_transaction = blobs_in_transaction.get(hash)
        if existing_in_transaction:
            return existing_in_transaction

        existing_in_db = session.get(Blob, hash)
        if existing_in_db:
            blobs_in_transaction[hash] = existing_in_db
            return existing_in_db

        data = path.read_bytes()
        new = Blob(
            hash=hash,
            data=data,
            # size=len(data),
        )
        blobs_in_transaction[hash] = new
        return new

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MerkleTreeNode):
            return self.hash == other.hash
        else:
            return False

    def __hash__(self) -> int:
        return self.hash
