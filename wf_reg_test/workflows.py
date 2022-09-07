from __future__ import annotations
import abc
import dataclasses
from pathlib import Path
from typing import Mapping, Optional

from sqlalchemy import Column, ForeignKey, Boolean, Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import declarative_base, relationship

from .util import hash_path, walk


Base = declarative_base()


URL_SIZE = 127
ENUM_SIZE = 63
HUMAN_READABLE_NAME_SIZE = 63


# TODO: think long and hard about cascading deletes


class WorkflowApp(Base):
    __tablename__ = "WorkflowApp"
    _id = Column(Integer, primary_key=True)
    repo = relationship("Repo", uselist=False)
    _repo_id = Column(Integer, ForeignKey("Repo._id"), nullable=False)
    workflow_engine_name = Column(String(ENUM_SIZE), nullable=False)
    url = Column(String(URL_SIZE), nullable=False)
    name = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)


class Repo(Base):
    __tablename__ = "Repo"
    _id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String(ENUM_SIZE), nullable=False)
    config = Column(String(1023), nullable=False)
    revisions = relationship("Revision")


class Revision(Base):
    __tablename__ = "Revision"
    _id = Column(Integer, primary_key=True, nullable=False)
    date = Column(DateTime, nullable=False)
    tree = relationship("MerkleTreeNode")
    _tree_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    executions = relationship("Execution", back_populates="revision")
    _repo_id = Column(String(127), ForeignKey("Repo._id"), nullable=False)


class Execution(Base):
    __tablename__ = "Execution"

    _id = Column(Integer, primary_key=True, nullable=False)
    _revision_id = Column(Integer, ForeignKey("Revision._id"), nullable=False)
    revision = relationship("Revision", back_populates="executions")
    output = relationship("MerkleTreeNode")
    _output_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    success = Column(Boolean, nullable=False)


class MerkleTreeNode(Base):
    __tablename__ = "MerkleTreeNode"
    hash = Column(Integer, primary_key=True, nullable=False)
    _parent_hash = Column(Integer, ForeignKey("MerkleTreeNode.hash"), nullable=False)
    children = relationship("MerkleTreeNode")
    name = Column(String(HUMAN_READABLE_NAME_SIZE), nullable=False)
    blob = relationship("Blob")
    _blob_hash = Column(Integer, ForeignKey("Blob.hash"), nullable=False)


class Blob(Base):
    __tablename__ = "Blob"
    hash = Column(Integer, primary_key=True, nullable=False)
    data = Column(LargeBinary, nullable=False)
