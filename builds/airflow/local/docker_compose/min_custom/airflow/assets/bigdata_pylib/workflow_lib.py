
"""General utility library to support DAGs"""

import os
import random
from datetime import datetime
import hashlib
import shutil

from pathlib import Path

import logging

__all__ = [
    'get_account_meta', 'get_project_meta', 'extract_filename_args', 
    'generate_client_files', 'display_dir_content','get_dag_context',
    'copy_files', 'get_files_from_path', 'path_from_xcom', 'get_line_count_from_file',
    'ls_files']

log = logging.getLogger(__name__)


def get_line_count_from_file(file_path):
    def _count_generator(reader):
        b = reader(1024*1024)
        while b:
            yield b
            b = reader(1024*1024)

    with open(file_path, 'rb') as fp:
        counter = _count_generator(fp.raw.read)
        return sum(buffer.count(b'\n') for buffer in counter)
        


def get_dag_context(input_str):
    """abstraction to...
    
    - break down dag filename to grab client_id and project_id
    - return dag meta from db from project_id and workflow type
    
    client_meta = {
        "client_id": "lala",
        "project_id": "ctc",
        "file_criteria": {
            "files": (5,10),
            "entries": (20,30),
            "values": (100,50000),
        },
    }   
    """


    dag_id = Path(input_str).stem
    
    client_meta = {
        "dag_id": dag_id,
    }

    return client_meta

def gen_batch_id(size=24):
    utc = datetime.utcnow()
    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:size]


    

def generate_client_files(client_id, project_id, batch_id, file_criteria):
    filename_tmpl = "{client_id}_{project_id}_{batch_id}_{file_id}.txt"
    files = []

    line_arg_tmpl = {
        "client_id": client_id,
        "project_id": project_id,
        "batch_id": batch_id,
        "file_id": "",
    }

    batch_src_path = os.path.join(os.environ.get("CLIENT_BATCH_ROOT"), batch_id)
    print(f"batch_src_path: {batch_src_path}")
    
    batch_dest_path = os.path.join(os.environ.get("INGESTION_ROOT"), client_id, project_id, batch_id)
    print(f"batch_dest_path: {batch_dest_path}")

    resp = {
        "files": [],
        "src_path": batch_src_path,
        "dest_path": batch_dest_path,
        "errors": [],
    }

    for file_id in range(random.randint(*file_criteria["files"])):
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
            for line_id in range(random.randint(*file_criteria["entries"])):
                #print('generate_line({}, {})'.format(line_id, args["file_criteria"]["values"]))
                line = generate_line(line_id, file_criteria["values"])
                print(f"  -{line}")
                f.write("{}\n".format(line))

        #try:
        #    src_file = os.path.join(batch_src_path, file_name)
        #    dest_file = os.path.join(batch_dest_path, file_name)
        #    print(f"cp {src_file} {dest_file}")
        #    shutil.copyfile(src_file, dest_file)
        #    resp["files"].append({"file": file_name, "status": "copied"})
        #
        #except Exception as e:
        #    resp["files"].append({"file": file_name, "status": f"error{e}"})
            

    #print("\n\n### Temporarily copy directly from client data source to platform ingestion area")
    #copy_files(batch_src_path, batch_dest_path, files)
    #display_dir_content(batch_dest_path)

    display_dir_content(batch_src_path, "client-side: batch_src_path")

    

def generate_client_files_v2(args):
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

def path_from_xcom(ti, ti_task_id, ti_key):
    """assists with reliably retrieving path from xcom.
    """
    limit = 0
    path = None
    while limit < 10 and path == None:
        path = ti.xcom_pull(task_ids=ti_task_id, key=ti_key)
        print(f'resolve attempt({limit}) path: {path}')
        limit += 1

    return path

def get_files_from_path(path, extentions=[]):
    """returns list of full file paths.
    not ideal for passing as xcom"""
    files = []

    if not os.path.exists(path):
        print(f"path '{path}' does not exist, exiting...")
        return files

    for (root, dirs, file) in os.walk(path):
        for f in file:
            if extentions == []:
                files.append(path+'/'+f)

            elif f.split('.')[-1] in extentions:
                files.append(path+'/'+f)

    return files

def dir_content(path, only_ext=[], desc="folder content:", files_only=True, debug=False):
    if debug: print("$ dir_content(...)")
    files = []

    if not os.path.exists(path):
        print(f"path '{path}' does not exist, exiting...")
        return files

    print(f"$ ls {path}")
    for (root, dirs, file) in os.walk(path):
        if files_only != True:
            for _dir in dirs:
                print(f"dir: {_dir}/")

        for f in file:
            print(f"--file: {f}")
            files.append(os.path.join(path, f))

        break
    return files
    

def ls_files(path, extentions=[]):
    from os import listdir
    from os.path import isfile, join
    files = []

    if not os.path.exists(path):
        print(f"path '{path}' does not exist, exiting...")
        return files

    for f in listdir(path):
        if isfile(join(path, f)):
            if f.split('.')[-1] in extentions:
                #print(f)
                files.append(f)
    
    return files

def display_dir_content(path, desc="folder content:"):
    print("$ display_dir_content(...)")

    print(f"$ ls {path} | exists? {os.path.exists(path)}")
    for (root, dirs, file) in os.walk(path):
        for f in file:
            print(f"--file: {f}")
        break

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

    return _path


"""
def get_project_meta(client_id, project_id):
    return get_account_meta(client_id)["project_meta"].get(project_id, {})

def get_account_meta(client_id):
    #Platform side db holding
    
    #Fake db abstraction to get account meta
    

    return platform_db().get(client_id, {"id": 0})

def platform_db():
    return {
        "lala": {
            "id": 100,
            "name": "LaLA LLC.",
            "owner": "lala",
            "project_meta": {
                "ctc": {
                    "file_format": {
                        "extension": ".txt",
                        "headers": ["id","project","desc","data","date"],
                        "header_exists": True,
                        "field_types": ["increment", "str-5", "str-20, int-10, dtef"],
                    },
                    "workflow_action_order": {
                        "etl": ["extract"],
                    },
                    "actions": {
                        "extract": {
                            "unzip": True,
                            "tar_file_format": "{client_id}_{project_id}_{batch_id}.tar.gz",
                            "dest": "hdfs",
                        },
                        "validate": {
                            "field": "project",
                        }
                    },
                }
            },
        }
    }

"""


def extract_filename_args(_filename):
    """Attempt to extract args from DAG.__file__

    Args:
    _filename: str: __file__
    Return: dict
    """
    dag_type = client_id = project_id = workflow_id = file_basename = None
    file_basename = Path(_filename).stem

    args = {"dag_id": file_basename}
    try:
        

        # route per dag_type (i.e. util, client, etc...)
        filename_parts = file_basename.split('__')
        if len(filename_parts) == 4:

            if file_basename.startswith("tenant__"):
            
                dag_type, client_id, project_id, workflow_id = file_basename.split('__')

                args = {
                    "dag_type": dag_type,
                    "client_id": client_id,
                    "project_id": project_id,
                    "workflow_id": workflow_id,
                }
                
                args.update({
                    "tags": list(args.values()),
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
    #main()
    pass