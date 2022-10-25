import re
import json
from pathlib import Path
from typing import Iterable

import github
import requests

from .workflows import WorkflowApp


github_client = github.Github(json.loads(Path("secrets.json").read_text())["github"])


def nf_core_registry() -> Iterable[WorkflowApp]:
    # https://github.com/nf-core/nf-co.re/blob/master/update_pipeline_details.php#L90
    ignored_repos_ini = requests.get("https://raw.githubusercontent.com/nf-core/nf-co.re/master/ignored_repos.ini").text
    ignored_repos_ini = ignored_repos_ini[:ignored_repos_ini.find("[ignore_topics]")]
    ignored_repos = {
        match.group(1)
        for match in re.finditer(r"repos\[\] = \"(.*)\"", ignored_repos_ini)
    }
    for repo in github_client.get_user("nf-core").get_repos():
        if repo.name not in ignored_repos:
            raise NotImplementedError
            yield WorkflowApp(
                workflow_engine_name="nextflow",
                url="https://nf-co.re/" + repo.name,
                display_name=repo.name,
                repo_url="https://github.com/" + repo.full_name,
                revisions=[],
            )

def snakemake_registry() -> Iterable[WorkflowApp]:
    # https://github.com/snakemake/snakemake-workflow-catalog/blob/main/scripts/generate-catalog.py
    url = "https://raw.githubusercontent.com/snakemake/snakemake-workflow-catalog/main/data.js"
    repo_infos = json.loads(requests.get(url).text.partition("\n")[2], timeout=10)
    for repo_info in repo_infos:
        if repo_info["standardized"]:
            raise NotImplementedError
            yield WorkflowApp(
                workflow_engine_name="snakemake",
                url="https://github.com/" + repo_info["full_name"],
                display_name=repo_info["full_name"],
                repo_url="https://github.com/" + repo_info["full_name"],
                revisions=[],
            )
