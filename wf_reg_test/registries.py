import re
import json
from pathlib import Path
from typing import Iterable

from tqdm import tqdm
import github
import requests

from .workflows import Workflow, Registry


github_client = github.Github(json.loads(Path("secrets.json").read_text())["github"])


def nf_core_registry() -> Registry:
    """Takes ~1s to retrieve all ~90 wfs in the nf-core registry.

    Source: https://github.com/nf-core/nf-co.re/blob/master/update_pipeline_details.php#L90
    See also: https://nf-co.re/
    """
    ignored_repos_ini = requests.get("https://raw.githubusercontent.com/nf-core/nf-co.re/master/ignored_repos.ini").text
    ignored_repos_ini = ignored_repos_ini[:ignored_repos_ini.find("[ignore_topics]")]
    ignored_repos = {
        match.group(1)
        for match in re.finditer(r"repos\[\] = \"(.*)\"", ignored_repos_ini)
    }
    registry = Registry(
        display_name="nf-core",
        url="https://nf-co.re/",
        workflows=[],
    )
    repos = github_client.get_user("nf-core").get_repos()
    for repo in tqdm(repos, desc="nf-core"):
        if repo.name not in ignored_repos:
            registry.workflows.append(Workflow(
                engine="nextflow",
                url="https://nf-co.re/" + repo.name,
                display_name=repo.name,
                repo_url="https://github.com/" + repo.full_name,
                revisions=[],
                registry=registry
            ))
    return registry

def snakemake_registry() -> Registry:
    """
    Takes <1s to get all 1781 workflows in the Snakemake-workflow-catalog

    Source: https://github.com/snakemake/snakemake-workflow-catalog/blob/main/scripts/generate-catalog.py
    See also: https://snakemake.github.io/snakemake-workflow-catalog/
    """
    url = "https://raw.githubusercontent.com/snakemake/snakemake-workflow-catalog/main/data.js"
    repo_infos = json.loads(requests.get(url, timeout=10).text.partition("\n")[2])
    registry = Registry(
        display_name="snakemake-workflow-catalog",
        url="https://snakemake.github.io/snakemake-workflow-catalog/",
        workflows=[],
    )
    for repo_info in tqdm(repo_infos, desc="snakemake"):
        if repo_info["standardized"]:
            registry.workflows.append(Workflow(
                engine="snakemake",
                url="https://github.com/" + repo_info["full_name"],
                display_name=repo_info["full_name"],
                repo_url="https://github.com/" + repo_info["full_name"],
                revisions=[],
                registry=registry,
            ))
    return registry
