from .data import get_data

if __name__ == "__main__":
    for workflow_app in get_data():
        for date, revision in workflow_app.repo.get_revisions():
            with revision.materialize() as path:
                workflow_app.workflow_engine.run(path)
