
"""
This DAG is an example of what a real workflow might look like.
Of course this is a slimed down version and has some create resources
until real sources can be built up.

~~~ This DAG under construction ~~~~
~~-- WARNING - IN PROGRESS --~~

Overview:
 - build out basic workflow templating, abstraction, and support libraries
"""

import os
import random
from datetime import datetime
import hashlib
import shutil

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

args = {
    "client_id": "lala",
    "project_id": "ctc",
    "folder_mode": "0o777",
    "file_criteria": {
        "files": (3,10),
        "entries": (5,20),
        "values": (100,500),
    },
}   

@task
def base(): pass

@task
def process_client_data(params):
    files = []
    src = os.environ.get('CLIENT_SRC_FOLDER', '/opt')

    dest = '/opt'
    if 'CLIENT_INGESTION_FOLDER' in os.environ:
        dest = os.environ["CLIENT_INGESTION_FOLDER"].format(client_id=params["client_id"])

    filename_tmpl = "{client_id}_{project_id}_{file_id}.txt"
    line_header = "id,project,desc,data,date"
    line_tmpl = "{line_id},ctc,record_{line_id},{value},{dte}"

    utc = datetime.utcnow()
    batch_id = hashlib.md5(utc.strftime("%Y%m%d%H%M%S%Z")).hexdigest()[:9]

    batch_src_path = os.path.join(src, batch_id)
    os.mkdir(batch_src_path, params["folder_mode"])

    # create random amount of files
    for file_id in range(random.randint(*params["file_criteria"]["files"])):

        # generate a file name
        file_name = filename_tmpl.format(
            client_id=params["client_id"],
            project_id=params["project_id"],
            file_id=file_id
        )
        files.append(file_name)
        full_file_path = os.path.join(batch_src_path, file_name)

        with open(full_file_path, 'w+') as f:
            f.write("{}\n".format(line_header))

            # add random amount of lines
            for line_id in range(random.randint(*params["file_criteria"]["entries"])):

                utc = datetime.utcnow()

                _line = line_tmpl.format(
                    line_id=line_id,
                    value=random.randint(*params["file_criteria"]["values"]),
                    dte=utc.strftime("%Y-%m-%dT%H:%M:%S.%Z")
                )
                f.write("{}\n".format(_line))
    
    # move files
    batch_dest_path = os.path.join(dest, batch_id)
    os.mkdir(batch_dest_path, params["folder_mode"])

    for _file in files:
        shutil.copyfile(
            os.path.join(batch_src_path, _file),
            os.path.join(batch_dest_path, _file))


@task
def end(): pass

with DAG(
    dag_id="util__generate_"+args["client_id"]+"_data", 
    start_date=datetime(2022, 10, 10), 
    schedule=None,
    catchup=False
) as dag:

    process_data = process_client_data(args)

    base() >> process_client_data >> end()

