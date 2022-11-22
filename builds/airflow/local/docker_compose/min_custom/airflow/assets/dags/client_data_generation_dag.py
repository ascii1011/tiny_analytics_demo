
"""
This DAG is an example of what a real workflow might look like.
Of course this is a slimed down version and has some create resources
until real sources can be built up.

~~~ This DAG under construction ~~~~
~~-- WARNING - IN PROGRESS --~~

Overview:
 - build out basic workflow templating, abstraction, and support libraries
"""

from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

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


#@task
#def base():
#    utc = datetime.utcnow()
#    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:6]

#@task
#def process_client_data(args):
#    src, dest = generate_client_files(args)
#    display_dir_content(src)
#    display_dir_content(dest)


#@task
#def end():
#    utc = datetime.utcnow()
#    return hashlib.md5(utc.strftime("%Y%m%d%H%M%S%f").encode('utf-8')).hexdigest()[:6]

with DAG(
    dag_id="util__generate_"+args["client_id"]+"_data", 
    start_date=datetime(2023, 12, 29), 
    schedule=None,
    catchup=False
) as dag:

    base_op = EmptyOperator(task_id="base")
    #process_data = process_client_data(args)

    #base() >> process_data >> end()
    hello = BashOperator(task_id="hello", bash_command="echo hello")
    hello1 = BashOperator(task_id="hello1", bash_command="echo hello")
    hello2 = BashOperator(task_id="hello2", bash_command="echo hello")

    step1_op = EmptyOperator(task_id="step1")
    step2_op = EmptyOperator(task_id="step2")
    end_op = EmptyOperator(task_id="end")

    base_op >> hello >> hello1 >> hello2 >> step1_op >> step2_op >> end_op

