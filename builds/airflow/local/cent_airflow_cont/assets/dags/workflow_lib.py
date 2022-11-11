

from pathlib import Path

__all__ = ['get_client_meta', 'extract_filename_args']


def get_client_meta(client):
    """Fake db abstraction"""
    client_meta = {
        "lala": {
            "id": 100,
            "name": "LaLA LLC.",
            "owner": "lala",
            "project_id": [
                {"id": "ctc", "task_params": {"var8": "888"}},
            ]
        }
    }

    return client_meta.get(client, {})


def extract_filename_args(_filename):
    dag_type = client_id = project_id = workflow_id = file_basename = None
    
    try:
        file_basename = Path(_filename).stem

        dag_type, client_id, project_id, workflow_id = file_basename.split('__')
    
    except:
        pass

    finally:

        return {
            "dag_id": file_basename,
            "dag_type": dag_type,
            "client_id": client_id.split('_')[1],
            "project_id": project_id.replace('job', ''),
            "workflow_id": workflow_id,
        }
