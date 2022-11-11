

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
                {
                    "id": "ctc", 
                    "task_params": {"var8": "888"}
                },
            ]
        }
    }

    return client_meta.get(client, {})


def extract_filename_args(_filename):
    dag_type = client_id = project_id = workflow_id = file_basename = None
    
    try:
        file_basename = Path(_filename).stem

        # route per dag_type (i.e. util, client, etc...)
        filename_parts = file_basename.split('__')
        if len(filename_parts) == 4:

            if file_basename.startswith("client__"):
                client_dag_id_tmpl = "{client_id}_{project_id}_{workflow_id}"
            
                dag_type, client_id, project_id, workflow_id = file_basename.split('__')

                args = {
                    "dag_type": dag_type,
                    "client_id": client_id,
                    "project_id": project_id,
                    "workflow_id": workflow_id,
                }
                
                args.update({
                    "tags": args.values(),
                    "dag_id": client_dag_id_tmpl.format(**file_basename)
                })

        if len(filename_parts) == 2:

            if file_basename.startswith("util__"):



    
    except:
        pass

    finally:

        return args
