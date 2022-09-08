from __future__ import annotations
import abc
import dataclasses
from datetime import datetime
import functools
import json
import operator
from pathlib import Path
from typing import Mapping, Optional, Any

from sqlalchemy import Column, ForeignKey, Boolean, Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import declarative_base, relationship, Mapped

from .util import hash_path, walk


Base = declarative_base()


URL_SIZE = 127
ENUM_SIZE = 63
HUMAN_READABLE_NAME_SIZE = 63


# TODO: think long and hard about cascading deletes


class WorkflowApp(Base):
    __tablename__ = "WorkflowApp"
    _id = Column(Integer, primary_key=True)
    repo: Mapped[Repo] = relationship("Repo", uselist=False)
    _repo_id = Column(Integer, ForeignKey("Repo._id"), nullable=False)
    workflow_engine_name: Mapped[str] = Column(String(ENUM_SIZE), nullable=False)
    url: Mapped[str] = Column(String(URL_SIZE), nullable=False)
    name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)


class Repo(Base):
    __tablename__ = "Repo"
    _id = Column(Integer, primary_key=True, nullable=False)
    type: Mapped[str] = Column(String(ENUM_SIZE), nullable=False)
    _kwargs: Mapped[str] = Column(String(1023), nullable=False)
    revisions: Mapped[Revision] = relationship("Revision", order_by="Revision.datetime")

    @property
    def kwargs(self) -> Any:
        return json.loads(self._kwargs)


class Revision(Base):
    __tablename__ = "Revision"
    _id = Column(Integer, primary_key=True, nullable=False)
    datetime: Mapped[datetime] = Column(DateTime, nullable=False)
    tree: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    _tree_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    executions: Mapped[list[Execution]] = relationship("Execution", order_by="Execution.datetime")
    _repo_id = Column(String(127), ForeignKey("Repo._id"), nullable=False)


class Execution(Base):
    __tablename__ = "Execution"

    _id = Column(Integer, primary_key=True, nullable=False)
    _revision_id = Column(Integer, ForeignKey("Revision._id"), nullable=False)
    datetime: Mapped[datetime] = Column(DateTime, nullable=False)
    output: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    _output_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    success: Mapped[bool] = Column(Boolean, nullable=False)


class MerkleTreeNode(Base):
    __tablename__ = "MerkleTreeNode"
    hash: Mapped[int] = Column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    _parent_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"))
    children: Mapped[MerkleTreeNode] = relationship("MerkleTreeNode")
    blob: Mapped[Blob] = relationship("Blob")
    _blob_hash = Column(Integer, ForeignKey("Blob.hash"))

    @staticmethod
    def from_path(
            path: Path,
            root: bool = True,
    ) -> MerkleTreeNode:
        ret = MerkleTreeNode(
            name="." if root else path.name,
        )
        if path.is_dir():
            ret.children = [
                MerkleTreeNode.from_path(path, root=False)
            ]
            ret.blob = None
            ret.hash = functools.reduce(
                operator.xor,
                (child.hash for child in ret.children),
                0,
            )
        else:
            ret.children = []
            ret.blob = Blob.from_path(path)
            ret.hash = ret.blob.hash
        return ret


class Blob(Base):
    __tablename__ = "Blob"
    hash: Mapped[int] = Column(Integer, primary_key=True, nullable=False)
    data: Mapped[bytes] = Column(LargeBinary, nullable=False)

    @staticmethod
    def from_path(path: Path) -> Blob:
        return Blob(
            hash=hash_path(path, size=64),
            data=path.read_bytes(),
        )
