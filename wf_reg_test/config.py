import pathlib

import upath

from .util import AzureCredential


cache_path = pathlib.Path(".cache")
cache_path.mkdir(exist_ok=True)


data_path = upath.UPath(
    "abfs://data3/",
    account_name="wfregtest",
    credential=AzureCredential(),
)


index_path = upath.UPath(
    "abfs://index3/",
    account_name="wfregtest",
    credential=AzureCredential(),
)
