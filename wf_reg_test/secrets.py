import warnings
import json
from pathlib import Path
import github

secrets_path = Path("secrets.json")
if secrets_path.exists():
    secrets = json.loads(secrets_path.read_text())
    github_client = github.Github(secrets["github"])
else:
    warnings.warn("You do not have `secrets.json` credentials. Some things may be slow.")
    github_client = github.Github()
