from datetime import datetime as DateTime
import pickle
import shutil
import sys
import urllib.parse
import warnings

import yaml
import charmonium.freeze
import charmonium.time_block as ch_time_block
import upath

from .workflows import RegistryHub, Registry, Workflow, Revision, Execution
from .util import expect_type, get_current_revision

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


@ch_time_block.decor()
def serialize(hub: RegistryHub, path: upath.UPath, warn: bool = True) -> None:
    if warn:
        for warning in hub.check_invariants():
            warnings.warn(warning)

    # This doesn't work so well for UPaths
    # if path.exists():
    #     shutil.rmtree(path)
    if not path.exists():
        path.mkdir()

    (path / "index.yaml").write_text(yaml.dump([
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
    (path / f"machines.yaml").write_text(yaml.dump({
        machine.short_description: machine
        for machine in unique_machines
    }))

    for registry in hub.registries:
        name = encode(registry.display_name)
        (path / f"{name}_workflows.yaml").write_text(yaml.dump([
            {
                "engine": workflow.engine,
                "url": workflow.url,
                "display_name": workflow.display_name,
                "repo_url": workflow.repo_url,
            }
            for workflow in registry.workflows
        ]))
        (path / f"{name}_revisions.yaml").write_text(yaml.dump([
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
        (path / f"{name}_executions.yaml").write_text(yaml.dump([
            {
                "machine": execution.machine.short_description if execution.machine else "<unknown>",
                "datetime": execution.datetime,
                "outputs": execution.outputs,
                "logs": execution.logs,
                "condition": execution.condition,
                "resources": execution.resources,
                "status_code": execution.status_code,
                "wf_reg_test_revision": execution.wf_reg_test_revision,
                "revision": revision.display_name,
                "workflow": workflow.display_name,
            }
            for workflow in registry.workflows
            for revision in workflow.revisions
            for execution in revision.executions
        ]))

    if warn:
        stored_hub = deserialize(path, warn=False)
        charmonium.freeze.config.ignore_all_code = True
        charmonium.freeze.config.ignore_all_classes = True
        charmonium.freeze.config.ignore_dict_order = True
        assert hub == stored_hub, charmonium.freeze.summarize_diff(hub, stored_hub)


@ch_time_block.decor()
def deserialize(path: upath.UPath, warn: bool = True) -> RegistryHub:
    registry_dicts = yaml.load(
        (path / "index.yaml").read_text(),
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
        (path / f"machines.yaml").read_text(),
        Loader=yaml.Loader,
    )
    for registry in hub.registries:
        name = encode(registry.display_name)

        workflow_dicts = yaml.load(
            (path / f"{name}_workflows.yaml").read_text(),
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
                registry=registry,
            )
            registry.workflows.append(workflow)
            workflows_map[workflow.display_name] = workflow

        revision_dicts = yaml.load(
            (path / f"{name}_revisions.yaml").read_text(),
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

        execution_dicts = yaml.load(
            (path / f"{name}_executions.yaml").read_text(),
            Loader=yaml.Loader,
        )
        for execution_dict in execution_dicts:
            revision = revision_map[execution_dict["workflow"], execution_dict["revision"]]
            execution = Execution(
                machine=machine_map.get(execution_dict["machine"]),
                datetime=expect_type(DateTime, execution_dict["datetime"]),
                outputs=execution_dict["outputs"],
                logs=execution_dict["logs"],
                condition=execution_dict["condition"],
                resources=execution_dict["resources"],
                status_code=execution_dict["status_code"],
                revision=revision,
                wf_reg_test_revision=execution_dict.get("wf_reg_test_revision", get_current_revision()),
            )
            revision.executions.append(execution)

    if warn:
        for warning in hub.check_invariants():
            warnings.warn(warning)

    return hub
