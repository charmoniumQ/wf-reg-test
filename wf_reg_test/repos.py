from __future__ import annotations

import abc
import dataclasses
import json
import types
from datetime import datetime
from pathlib import Path
from typing import ContextManager, Optional

import git
import github
import xxhash


class Repo(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def url(self) -> str:
        ...

    @abc.abstractmethod
    def get_revisions(self) -> list[tuple[datetime, LazyPath]]:
        ...


class LazyPath(abc.ABC):
    @abc.abstractmethod
    def materialize(self) -> ContextManager[Path]:
        ...


github_client = github.Github(json.loads(Path("secrets.json").read_text())["github"])


@dataclasses.dataclass
class GitHubRepo(Repo):
    user: str
    repo: str
    only_tags: bool

    @property
    def name(self) -> str:
        return self.repo

    @property
    def url(self) -> str:
        return f"https://github.com/{self.user}/{self.repo}"

    def get_revisions(self) -> list[tuple[datetime, LazyPath]]:
        repo = github_client.get_user(self.user).get_repo(self.repo)
        if self.only_tags:
            revs = ((tag.commit, tag.name) for tag in repo.get_tags())
        else:
            revs = ((commit, commit.sha) for commit in repo.get_commits())
        return [
            (commit.commit.committer.date, LazyGitCheckout(repo.svn_url, rev))
            for commit, rev in revs
        ]


cache_path = Path(".cache2")


@dataclasses.dataclass
class LazyGitCheckout(LazyPath):
    url: str
    rev: str

    def materialize(self) -> ContextManager[Path]:
        return self

    def __enter__(self) -> Path:
        url_hash = xxhash.xxh32(self.url.encode("utf-8")).hexdigest()
        repo_path = cache_path / url_hash
        if not repo_path.exists():
            repo = git.repo.Repo.clone_from(self.url, repo_path)
        else:
            repo = git.repo.Repo(repo_path)
        with repo:
            repo.head.reset(self.rev, index=True, working_tree=True)
            return repo_path

    def __exit__(
        self,
        _exc_type: Optional[type[BaseException]],
        _exc_value: Optional[BaseException],
        _traceback: Optional[types.TracebackType],
    ) -> None:
        pass


repos = {
    "GitHubRepo": GitHubRepo,
}
