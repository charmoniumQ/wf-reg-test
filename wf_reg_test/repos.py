from __future__ import annotations

import dataclasses
import json
import os
import types
import urllib.parse
from pathlib import Path
import subprocess
from typing import ContextManager, Optional, Any, Iterable, Mapping
from typing_extensions import Protocol
import warnings

import git
import github
import xxhash

from .workflows import Revision, Workflow


github_client = github.Github(os.environ.get("GITHUB_ACCESS_TOKEN", None))


def get_repo(url: str) -> Repo:
    parsed_url = urllib.parse.urlparse(url)
    path = Path(parsed_url.path)
    if parsed_url.netloc == "github.com" in parsed_url.netloc:
        if len(path.parts) == 3:
            url_options = urllib.parse.parse_qs(parsed_url.query)
            revisions = url_options.get("revisions", ["tags"])[-1]
            skip_drafts = bool(int(url_options.get("skip-revisions", ["1"])[-1]))
            skip_prereleases = bool(int(url_options.get("skip-prereleases", ["1"])[-1]))
            return GitHubRepo(
                user=path.parts[1],
                repo=path.parts[2].replace(".git", ""),
                revisions=revisions,
                skip_drafts=skip_drafts,
                skip_prereleases=skip_prereleases,
            )
        else:
            raise NotImplementedError(
                "Only know how to access whole git repositories, not subdirs"
            )
    raise NotImplementedError(f"No known RepoAccessor for {parsed_url!s}")


class Repo(Protocol):
    def get_revisions(self) -> Iterable[Revision]: ...
    def checkout(self, revision: Revision, dest_path: Path) -> None: ...
    def get_checkout_cmd(self, revision: Revision, dest_path: Path) -> list[list[str]]: ...


@dataclasses.dataclass
class GitHubRepo(Repo):
    user: str
    repo: str
    revisions: str = "tags"
    skip_drafts: bool = True
    skip_prereleases: bool = True

    @property
    def url(self) -> str:
        return f"https://github.com/{self.user}/{self.repo}"

    def get_revisions(self) -> Iterable[Revision]:
        repo = github_client.get_user(self.user).get_repo(self.repo)
        if False:
            pass
        elif self.revisions == "tags":
            for tag in repo.get_tags():
                yield Revision(
                    rev=tag.commit.sha,
                    display_name=tag.name,
                    url=f"{self.url}/tree/{tag.name}",
                    datetime=tag.commit.commit.committer.date,
                    executions=[],
                    workflow=None,
                )
        elif self.revisions == "releases":
            tags = {tag.name: tag for tag in repo.get_tags()}
            for release in repo.get_releases():
                if (not self.skip_drafts or not release.draft) and (not self.skip_prereleases or not release.prerelease):
                    tag = tags[release.tag_name]
                    try:
                        commit = tag.commit.commit
                    except github.GithubException:
                        warnings.warn(f"Problem fetching commit for {self.url} {release.tag_name}")
                        continue
                    yield Revision(
                        rev=tag.commit.sha,
                        display_name=tag.name,
                        url=f"{self.url}/tree/{tag.name}",
                        datetime=tag.commit.commit.committer.date,
                        executions=[],
                        workflow=None,
                    )
        elif self.revisions == "commits":
            for commit2 in repo.get_commits():
                yield Revision(
                    rev=commit2.sha,
                    display_name=commit2.sha[:6],
                    url=f"{self.url}/tree/{commit2.sha}",
                    datetime=commit2.commit.committer.date,
                    executions=[],
                    workflow=None,
                )
        else:
            raise ValueError(f"Don't know how to list {self.revisions}")

    def checkout(
            self,
            revision: Revision,
            dest_path: Path,
    ) -> None:
        subprocess.run(["git", "clone", "--recursive", self.url, str(dest_path)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(dest_path), "checkout", revision.rev], check=True, capture_output=True)
        proc = subprocess.run(["git", "-C", str(dest_path), "submodule", "update", "--init", "--recursive"], check=False, capture_output=True)
        if proc.returncode != 0:
            warnings.warn(f"Could not update submodules for {self.url} in {dest_path}")

    def get_checkout_cmd(self, revision: Revision, dest_path: Path) -> list[list[str]]:
        return [
            ["git", "clone", "--recursive", self.url, str(dest_path)],
            ["git", "-C", str(dest_path), "checkout", revision.rev],
            ["git", "submodule", "update", "--recursive"],
        ]
