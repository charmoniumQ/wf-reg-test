import abc
from typing import ContextManager
import github
import json
import dataclasses
import xxhash
import git
from typing import Optional
import types
from pathlib import Path
import xxhash
from datetime import datetime


class Repo(abc.ABC):
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
    only_use_tagged_commits: bool

    def get_revisions(self) -> list[tuple[datetime, LazyPath]]:
        repo = github_client.get_user(self.user).get_repo(self.repo)
        if self.only_use_tagged_commits:
             revs = (
                 (tag.commit, tag.name)
                 for tag in repo.get_tags()
             )
        else:
            revs = (
                (commit, commit.sha)
                for commit in repo.get_commits()
            )
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
