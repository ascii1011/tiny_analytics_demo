
"""General utility library to support DAGs"""

import os
import random
from datetime import datetime
import hashlib
import shutil

from pathlib import Path

import logging

__all__ = ['get_account_meta', 'extract_filename_args', 'generate_client_files', 'display_dir_content']

log = logging.getLogger(__name__)


def gen_batch_id():
    utc = datetime.utcnow()
    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:24]
    

def generate_client_files(args):
    filename_tmpl = "{client_id}_{project_id}_{batch_id}_{file_id}.txt"
    files = []

    batch_id = gen_batch_id()

    line_arg_tmpl = {
        "client_id": args["client_id"],
        "project_id": args["project_id"],
        "batch_id": batch_id,
        "file_id": "",
    }

    batch_src_path = os.path.join(os.environ.get("CLIENT_BATCH_ROOT", "/opt/tmp"), batch_id)
    os.mkdir(batch_src_path, 0o777)
    print(f"batch_src_path: {batch_src_path}")

    batch_dest_path = os.path.join(os.environ.get("INGESTION_ROOT", "/opt/tmp/dump"), batch_id)
    os.mkdir(batch_dest_path, 0o777)
    print(f"batch_dest_path: {batch_dest_path}")

    for file_id in range(random.randint(*args["file_criteria"]["files"])):
        line_args = line_arg_tmpl.copy()
        line_args.update({"file_id": file_id})
        file_name = filename_tmpl.format(**line_args)
        files.append(file_name)
        full_file_path = os.path.join(batch_src_path, file_name)

        print(f"generating: {full_file_path}")

        with open(full_file_path, 'w+') as f:
            line_header = "id,project,desc,data,date"
            print(f" . -{line_header}")
            f.write("{}\n".format(line_header))
            for line_id in range(random.randint(*args["file_criteria"]["entries"])):
                #print('generate_line({}, {})'.format(line_id, args["file_criteria"]["values"]))
                line = generate_line(line_id, args["file_criteria"]["values"])
                print(f"  -{line}")
                f.write("{}\n".format(line))

    print("\n\n### Temporarily copy directly from client data source to platform ingestion area")
    copy_files(batch_src_path, batch_dest_path, files)

    print('-')
    print(f'batch_id({type(batch_id)}: {batch_id}')
    print('-')

    return batch_src_path, batch_dest_path

def display_dir_content(path, desc):
    print(f"##[{desc}] ls {path}")
    for (root, dirs, file) in os.walk(path):
        for f in file:
            print(f)

def generate_line(line_id, values):
    utc = datetime.utcnow()
    return "{line_id},ctc,record_{line_id},{value},{dte}".format(
        line_id=line_id,
        value=random.randint(*values),
        dte=utc.strftime("%Y-%m-%dT%H:%M:%S.%f")
    )

def copy_files(src, dest, files):

    for _file in files:
        shutil.copyfile(
            os.path.join(src, _file),
            os.path.join(dest, _file))

    
def get_client_ingestion_path(execution_date, project_id, client_id, client_data_root):
    ex = "/opt/mnt/workflows/ingest/{client_id}/project_id}/{execution_date}"
    _path = f"{client_data_root}/{client_id}/{project_id}/{execution_date}"

    return _path.format(
        client_data_root=client_data_root,
        client_id=client_id,
        project_id=project_id,
        execution_date=execution_date
    )


def get_account_meta(client_id):
    """Fake db abstraction to get account meta"""
    client_meta = {
        "lala": {
            "id": 100,
            "name": "LaLA LLC.",
            "owner": "lala",
            "project_meta": {"ctc": {"var8": "888"}},
        }
    }

    return client_meta.get(client_id, {})


def extract_filename_args(_filename):
    """Attempt to extract args from DAG.__file__

    Args:
    _filename: str: __file__
    Return: dict
    """
    dag_type = client_id = project_id = workflow_id = file_basename = None
    args = {}
    try:
        file_basename = Path(_filename).stem

        # route per dag_type (i.e. util, client, etc...)
        filename_parts = file_basename.split('__')
        if len(filename_parts) == 4:

            if file_basename.startswith("client__"):
            
                dag_type, client_id, project_id, workflow_id = file_basename.split('__')

                args = {
                    "dag_type": dag_type,
                    "client_id": client_id,
                    "project_id": project_id,
                    "workflow_id": workflow_id,
                }
                
                args.update({
                    "tags": args.values(),
                    "dag_id": file_basename
                })

        if len(filename_parts) == 2:

            if file_basename.startswith("util__"):

                args = {
                    "dag_id": file_basename
                }
    
    except:
        pass

    finally:
        return args


def main():

    args = {
        "client_id": "lala",
        "project_id": "ctc",
        "file_criteria": {
            "files": (2,3),
            "entries": (2,4),
            "values": (10,50),
        },
    }   

    generate_client_files(args)



if __name__ == "__main__":
    main()
    pass