
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
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# reusable utils and tools
from workflow_lib import get_client_meta, extract_filename_args
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl

args = extract_filename_args(__file__)
print(f'args: {args}')

@task(task_id="client_meta")
def client_meta(params):
    return get_client_meta(params["client_id"])

@task(task_id="transformation")
def transformation(params):
    print('transforming ... ')

def get_url_params(**kwargs):
    params = kwargs["ti"].xcom_pull_tapd()
    print('tapd url params: {}'.format(params))
 
with DAG(
    dag_id=args["dag_id"], 
    start_date=datetime(2022, 10, 10), 
    schedule=None,
    catchup=False,
    tags=args["tags"]) as dag:

    get_client_meta = client_meta(args)
                                                                                                                                                                                                                      
    extract = BashOperator(
        task_id="extract",
        bash_command=extract_bash_cmd_tmpl,
        params=args)

    transform = transformation(args)
                                                                                                                                                                                                                     
    load = BashOperator(
        task_id="load",
        bash_command=load_bash_cmd_tmpl,
        params=args)

    # Set dependencies between tasks                                                                                                                                                                                                                          
    get_client_meta >> extract >> transform >> load

