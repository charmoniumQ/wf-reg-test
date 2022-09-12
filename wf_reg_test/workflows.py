from __future__ import annotations

import abc
from datetime import datetime
import logging
import functools
import json
import operator
from pathlib import Path
from typing import ContextManager, cast, Optional, Callable

import sqlalchemy
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
    BigInteger
)
from sqlalchemy.orm import Mapped, Session, declarative_base, relationship, deferred

from .util import hash_path, hash_bytes, walk

Base = declarative_base()

logger = logging.getLogger()

URL_SIZE = 127
HUMAN_READABLE_NAME_SIZE = 63

# TODO: think long and hard about cascading deletes


class WorkflowApp(Base):
    __tablename__ = "WorkflowApp"
    _id = Column(Integer, primary_key=True)
    workflow_engine_name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    url: Mapped[str] = Column(String(URL_SIZE), nullable=False)
    display_name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    repo_url: Mapped[str] = Column(String(URL_SIZE), nullable=False)
    revisions: Mapped[Revision] = relationship("Revision", order_by="Revision.datetime")


class RepoAccessor(abc.ABC):
    @abc.abstractmethod
    def get_revisions(self) -> list[Revision]:
        ...

    @abc.abstractmethod
    def checkout(self, revision: Revision) -> ContextManager[Path]:
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
        "Execution", order_by="Execution.datetime"
    )
    _workflow_app_id = Column(Integer, ForeignKey("WorkflowApp._id"), nullable=False)

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
    datetime: Mapped[datetime] = Column(DateTime, nullable=False)
    output: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    _output_hash = Column(BigInteger, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    success: Mapped[bool] = Column(Boolean, nullable=False)


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

    def ref_count(self, session: Session) -> int:
        # TODO: remove this cast
        return sqlalchemy.select(WorkflowApp).filter_by(_parent_hash=self.hash).count() # type: ignore

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
                hash_contents = f"{path!s}:{blob.hash:08x}"

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
            )
            return ret

        return inner

    def list_children(self, prefix: str = "") -> str:
        new_prefix = prefix + "/" + self.name if prefix else self.name
        return  new_prefix + "\n" + "".join([
            child.list_children(new_prefix)
            for child in self.children
        ])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MerkleTreeNode):
            return self.hash == other.hash
        else:
            return False

    def __hash__(self) -> int:
        return self.hash


class Blob(Base):
    __tablename__ = "Blob"
    hash: Mapped[int] = Column(BigInteger, primary_key=True, autoincrement=False)
    data: Mapped[bytes] = deferred(Column(LargeBinary, nullable=False))

    @staticmethod
    def from_path(path: Path, blobs_in_transaction: dict[int, Blob], session: Session) -> Blob:
        hash = hash_path(path, size=64) - (1 << 63)

        existing_in_transaction = blobs_in_transaction.get(hash)
        if existing_in_transaction:
            return existing_in_transaction

        existing_in_db = session.get(Blob, hash)
        if existing_in_db:
            blobs_in_transaction[hash] = existing_in_db
            return existing_in_db

        new = Blob(
            hash=hash,
            data=path.read_bytes(),
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
