
"""
This DAG is an example of what a real workflow might look like.
"""

from datetime import datetime
import hashlib

from airflow import DAG
from airflow.decorators import task
#from airflow.operators.empty import EmptyOperator
#from airflow.operators.python import PythonOperator
#from airflow.operators.bash import BashOperator

import logging

from workflow_lib import generate_client_files, display_dir_content

log = logging.getLogger(__name__)

args = {
    "client_id": "lala",
    "project_id": "ctc",
    "file_criteria": {
        "files": (2,3),
        "entries": (2,3),
        "values": (100,500),
    },
}   


@task
def base():
    utc = datetime.utcnow()
    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:6]

@task
def process_client_data(args):
    src, dest = generate_client_files(args)
    display_dir_content(src)
    display_dir_content(dest)


@task
def end():
    utc = datetime.utcnow()
    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:6]

with DAG(
    dag_id="lala_ctc_gen_dag", 
    start_date=datetime(2023, 12, 29), 
    schedule=None,
    catchup=False
) as dag:

    base_op = base()
    client_op = process_client_data(args)
    end_op = end()

    base_op >> client_op >> end_op


