from typing import Iterable
import json
import requests

from .workflows2 import WorkflowApp2


def snakemake_registry() -> Iterable[WorkflowApp2]:
    data_url = "https://raw.githubusercontent.com/snakemake/snakemake-workflow-catalog/main/data.js"
    data = json.loads(requests.get(data_url).text.partition("\n")[2])
