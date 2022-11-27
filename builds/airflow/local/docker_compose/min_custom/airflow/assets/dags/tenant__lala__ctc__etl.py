

import os
from pprint import pprint

import pendulum

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# use to fail a task
from airflow.exceptions import AirflowFailException

# reusable utils and tools
from workflow_lib import get_project_meta, extract_filename_args
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl

args = extract_filename_args(__file__)

"""                                                                                                                                                                                                                    
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
        "dest": "hdfs",
    },
    "validate": {
        "field": "project",
    }
},
"""

@task()
def context(args, dag_run=None, ti=None):
    """get account meta.  typically retrived by db"""
    print(f'args: {args}')
    print(f'dag_run: {dag_run}')
    print(f'ti: {ti}')

    trigger_context = dag_run.conf.get('context')
    print(f'trigger_context: {trigger_context}')

    client_id, project_id, batch_id = trigger_context.split('-')
    print(f'client: {client_id}, project: {project_id}, batch: {batch_id}')

    meta = get_project_meta(client_id, project_id)

    print(f'meta: {meta}')
         
    ti.xcom_push(key="workflow", value=meta["workflow_action_order"][args["workflow_id"]])

    ingestion_path = os.path.join(os.environ.get("INGESTION_ROOT"), client_id, project_id, batch_id)
    ti.xcom_push(key="ingestion_path", value=ingestion_path)
    
    extract_config = meta["actions"]["extract"]
    targz_filename = extract_config["tar_file_format"].format(
        client_id=client_id,
        project_id=project_id,
        batch_id=batch_id)
    ti.xcom_push(key="targz_filename", value=targz_filename)


    #ti.xcom_push(key="client_id", value=args["client_id"])
    #ti.xcom_push(key="project_id", value=args["project_id"])
    
    #ti.xcom_push(key="file_format", value=meta["file_format"])
    #ti.xcom_push(key="actions", value=meta["actions"])

    
    
with DAG(
    dag_id=args["dag_id"], 
    start_date=pendulum.datetime(2022, 11, 27, tz="UTC"), 
    schedule=None,
    catchup=False) as dag:

    op_context = context(args)

    # Copies data from ingestion area to staging and might extract if needed (zip, tar.gz, etc..)
    # typically data is not moved because of verification and historical purposes.  important is downstream data is lost (can replay)
    op_extract = BashOperator(
        task_id="extract",
        bash_command=extract_bash_cmd_tmpl,
        params=args)



    op_context  >> op_extract