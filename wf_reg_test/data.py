from .workflows import WorkflowApp
from .engines import Nextflow
from .repos import GitHubRepo


def get_data() -> list[WorkflowApp]:
    return [
        WorkflowApp(
            url="https://nf-co.re/mag",
            repo=GitHubRepo(
                user="nf-core",
                repo="mag",
                only_use_tagged_commits=True,
            ),
            workflow_engine=Nextflow(),
        ),
    ]
