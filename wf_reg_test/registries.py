from typing import Iterable
import json
import requests

import github

from .workflows2 import WorkflowApp2


def snakemake_registry() -> Iterable[WorkflowApp2]:
    url = "https://raw.githubusercontent.com/snakemake/snakemake-workflow-catalog/main/data.js"
    repo_infos = json.loads(requests.get(url).text.partition("\n")[2])
    for repo_info in repo_infos:
        if repo_info["standardized"]:
            yield WorkflowApp2(
                workflow_engine_name="snakemake",
                url="https://github.com/" + repo_info["full_name"],
                display_name=repo_info["full_name"],
                repo_url="https://github.com/" + repo_info["full_name"],
                revisions=[],
            )
