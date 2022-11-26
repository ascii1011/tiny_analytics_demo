

from datetime import datetime
from pprint import pprint

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# reusable utils and tools
from workflow_lib import get_project_meta, extract_filename_args
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl

args = extract_filename_args(__file__)
args.update({"batch_id": "abc"})
#print(f'args: {args}')        
# 
#
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
def context(args, ti=None):
    """get account meta.  typically retrived by db"""
    #ti.xcom_push(key="client_id", value=args["client_id"])
    #ti.xcom_push(key="project_id", value=args["project_id"])
    
    meta = get_project_meta(args["client_id"], args["project_id"])
    #ti.xcom_push(key="file_format", value=meta["file_format"])
    ti.xcom_push(key="workflow", value=meta["workflow_action_order"][args["workflow_id"]])
    #ti.xcom_push(key="actions", value=meta["actions"])

    
    
with DAG(
    dag_id=args["dag_id"], 
    start_date=datetime(2022, 11, 23), 
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