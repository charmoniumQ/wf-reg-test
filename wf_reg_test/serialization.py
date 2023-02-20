from datetime import datetime as DateTime
import dataclasses
import pickle
import shutil
import sys
import pathlib
import urllib.parse
import warnings
from typing import cast, Mapping, Any

import lazy_object_proxy  # type: ignore
import yaml
import pickle
import charmonium.freeze
import charmonium.time_block
import tqdm
import upath
import zlib

from .workflows import RegistryHub, Registry, Workflow, Revision, Execution, File, FileBundle
from .util import expect_type, get_current_revision, merge_dicts, groupby_dict, raise_, upath_to_url
from .config import cache_path
# TODO: Figure out if I even need to take an argument for index_path, since I'm also importing cache_path directly.

"""

I used to do something like `yaml.dump(hub)`. No de/serialization
code needed! This has several disadvantages:

- All the data ends up in one file. I can't tell if a diff adds an
  execution or adds a workflow. One time I accidentally re-added the
  same workflows.

- If the model of the data in RAM is identical to the model in disk,
  it is hard to do migrations. You have to read the data from disk
  into the data in RAM, using one model and then write it back using
  another model.

- It is difficult to re-scan the registries without throwing out
  existing executions, since executions were stored in workflow
  objects in the same file.

So I define a de/serialization routine here, which stores the
registries, workflows, revisions, and executions in separate files.

"""

# encode will escape spaces and slashes in the name.
encode = urllib.parse.quote_plus


def write_text(path: upath.UPath, text: str) -> None:
    # with charmonium.time_block.ctx(f"write_text({path.name})"):
    path.write_text(text)


def read_text(path: upath.UPath) -> str:
    # with charmonium.time_block.ctx(f"read_text({path.name})"):
    return path.read_text()


def cached_read_bytes(path: upath.UPath) -> bytes:
    cache_dest = cache_path / urllib.parse.quote(upath_to_url(path), safe="")
    if not cache_dest.exists():
        ret = path.read_bytes()
        cache_dest.write_bytes(ret)
        return ret
    else:
        return cache_dest.read_bytes()


@charmonium.time_block.ctx("serialize")
def serialize(hub: RegistryHub, path: upath.UPath, warn: bool = True) -> None:
    if warn:
        for warning in hub.check_invariants():
            warnings.warn(warning)

    # This doesn't work so well for UPaths
    # if path.exists():
    #     shutil.rmtree(path)
    if not path.exists():
        path.mkdir()

    write_text(path / "index.yaml", yaml.dump([
        {
            "display_name": registry.display_name,
            "url": registry.url,
        }
            for registry in hub.registries
    ]))

    unique_machines = {
        execution.machine
        for registry in hub.registries
        for workflow in registry.workflows
        for revision in workflow.revisions
        for execution in revision.executions
        if execution.machine
    }
    write_text(path / f"machines.yaml", yaml.dump({
        machine.short_description: machine
        for machine in unique_machines
    }))

    for registry in hub.registries:
        name = encode(registry.display_name)
        write_text(path / f"{name}_workflows.yaml", yaml.dump([
            {
                "engine": workflow.engine,
                "url": workflow.url,
                "display_name": workflow.display_name,
                "repo_url": workflow.repo_url,
            }
            for workflow in registry.workflows
        ]))
        write_text(path / f"{name}_revisions.yaml", yaml.dump([
            {
                "display_name": revision.display_name,
                "url": revision.url,
                "rev": revision.rev,
                "datetime": revision.datetime,
                "workflow": workflow.display_name,
            }
            for workflow in registry.workflows
            for revision in workflow.revisions
        ]))
        (path / f"{name}_executions.pkl").write_bytes(pickle.dumps([
            {
                "machine": execution.machine.short_description if execution.machine else "<unknown>",
                "datetime": execution.datetime,
                # Note that FileBundle.files are too big to store in the rest of the object.
                # Instead we store a thunk that looks up the FileBundle based on the workflow and archive hash.
                # Using the workflow to define the storage location helps batch the downloads.
                # Within that file, the archive hash uniquely points to the file map.
                # If two archives are the same, its ok to only store their file map once; it should be identical.
                "outputs": execution.outputs.archive,
                "logs": execution.logs.archive,
                "condition": execution.condition,
                "resources": execution.resources,
                "status_code": execution.status_code,
                "wf_reg_test_revision": execution.wf_reg_test_revision,
                "revision": revision.display_name,
                "workflow": workflow.display_name,
                "workflow_error": execution.workflow_error,
            }
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ]))

        file_bundles = [
            file_bundle
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
            for file_bundle in [execution.outputs, execution.logs]
        ]
        real_file_bundles = [
            file_bundle
            for file_bundle in file_bundles
            if not is_lazy_object_proxy(file_bundle.files)
        ]
        if len(real_file_bundles) > 4:
            real_file_bundles = tqdm.tqdm(real_file_bundles, desc="file bundles")
        for file_bundle in real_file_bundles:
            file_bundle_path = path / "files" / f"{file_bundle.archive.hash_val}"
            file_bundle_path.write_bytes(pickle.dumps(file_bundle.files))
            file_bundle.files = lazy_object_proxy.Proxy(
                lambda: pickle.loads(file_bundle_path.read_bytes())
            )
            assert is_lazy_object_proxy(file_bundle.files)

    if warn:
        stored_hub = deserialize(path, warn=False)
        # if stored_hub != hub:
        #     warnings.warn("hub != stored_hub, see diff.log")
        #     upath.UPath("diff.log").write_text(
        #         charmonium.freeze.summarize_diff(
        #             hub,
        #             stored_hub,
        #             charmonium.freeze.Config(
        #                 ignore_all_code=True,
        #                 ignore_all_classes=True,
        #                 ignore_dict_order=True,
        #             ),
        #         )
        #     )


@charmonium.time_block.ctx("deserialize")
def deserialize(path: upath.UPath, warn: bool = True) -> RegistryHub:
    registry_dicts = yaml.load(
        read_text(path / "index.yaml"),
        Loader=yaml.Loader,
    )
    hub = RegistryHub(
        registries=[
            Registry(
                display_name=registry_dict["display_name"],
                url=registry_dict["url"],
                workflows=[],
            )
            for registry_dict in registry_dicts
        ]
    )
    machine_map = yaml.load(
        read_text(path / f"machines.yaml"),
        Loader=yaml.Loader,
    )

    for registry in hub.registries:
        name = encode(registry.display_name)

        workflow_dicts = yaml.load(
            read_text(path / f"{name}_workflows.yaml"),
            Loader=yaml.Loader,
        )
        workflows_map: dict[str, Workflow] = {}
        for workflow_dict in workflow_dicts:
            workflow = Workflow(
                engine=workflow_dict["engine"],
                url=workflow_dict["url"],
                display_name=workflow_dict["display_name"],
                repo_url=workflow_dict["repo_url"],
                revisions=[],
                #registry=registry,
            )
            registry.workflows.append(workflow)
            workflows_map[workflow.display_name] = workflow

        revision_dicts = yaml.load(
            read_text(path / f"{name}_revisions.yaml"),
            Loader=yaml.Loader,
        )
        revision_map: dict[tuple[str, str], Revision] = {}
        for revision_dict in revision_dicts:
            workflow = workflows_map[revision_dict["workflow"]]
            revision = Revision(
                display_name=revision_dict["display_name"],
                url=revision_dict["url"],
                datetime=expect_type(DateTime, revision_dict["datetime"]),
                rev=revision_dict["rev"],
                executions=[],
                workflow=workflow,
            )
            workflow.revisions.append(revision)

            revision_map[workflow.display_name, revision.display_name] = revision

        executions_path = path / f"{name}_executions.pkl"
        if executions_path.exists():
            execution_dicts_pkl = executions_path.read_bytes()
            execution_dicts = pickle.loads(execution_dicts_pkl)
        else:
            execution_dicts = []

        for execution_dict in execution_dicts:
            revision = revision_map[execution_dict["workflow"], execution_dict["revision"]]
            for file_bundle_key in ["outputs", "logs"]:
                if isinstance(execution_dict[file_bundle_key], File):
                    files = cast(Mapping[pathlib.Path, File], lazy_object_proxy.Proxy(
                        lambda:
                        pickle.loads(cached_read_bytes(path / "files" / f"{execution_dict[file_bundle_key].archive.hash_val}"))
                    ))
                    execution_dict[file_bundle_key] = FileBundle(execution_dict[file_bundle_key], files)
                else:
                    raise TypeError(f"execution.{file_bundle_key} of Execution {execution_dict['datetime']} of Revision {execution_dict['revision']} of Workflow {execution_dict['workflow']} is type {type(execution_dict[file_bundle_key])}")
            execution = Execution(
                machine=machine_map.get(execution_dict["machine"]),
                datetime=expect_type(DateTime, execution_dict["datetime"]),
                outputs=execution_dict["outputs"] if execution_dict["outputs"] is not None else FileBundle.blank(),
                logs=execution_dict["logs"] if execution_dict["logs"] is not None else FileBundle.blank(),
                condition=execution_dict["condition"],
                resources=execution_dict["resources"],
                status_code=execution_dict["status_code"],
                revision=revision,
                wf_reg_test_revision=execution_dict.get("wf_reg_test_revision", get_current_revision()),
                workflow_error=execution_dict.get("workflow_error", None),
            )

            revision.executions.append(execution)

    if warn:
        for warning in hub.check_invariants():
            warnings.warn(warning)

    return hub


def is_lazy_object_proxy(obj: Any) -> bool:
    return hasattr(obj, "__factory__")
