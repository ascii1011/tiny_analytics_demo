
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

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

args = {
    "client_id": "lala",
    "file_criteria": {
        "files": 3,
        "entries": 10,
    },
}   


@task
def process_client_data(params):
    src = os.environ.get('CLIENT_SRC_FOLDER', '/opt')
    dest = os.environ.get('CLIENT_INGESTION_FOLDER', '/opt').format(client_id=client_id)

    filename_tmpl = "client_data_{}.txt"
    line_header = "id,project,desc,data,date"
    line_tmpl = "{},ctc,record{},231,2022-10-01T08:01:22Z"


    for file_index in range(params["file_criteria"]["num_of_files"]):

        # generate
        with open(, w+) as f:

        # move
    

with DAG(
    dag_id="util__generate_"+args["client_id"]+"_data", 
    start_date=datetime(2022, 10, 10), 
    schedule=None,
    catchup=False,
    tags=["util","lala", "generate_data"]
) as dag:


    # base task

    process_data = process_client_data(args)
    
    # end task


    base >> process_client_data >> end

