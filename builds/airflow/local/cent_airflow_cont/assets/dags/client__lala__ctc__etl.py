
"""
This DAG is an example of what a real workflow might look like.
Of course this is a slimed down version and has some create resources
until real sources can be built up.

~~~ This DAG under construction ~~~~
~~-- WARNING - IN PROGRESS --~~

Overview:
 - build out basic workflow templating, abstraction, and support libraries
 - leverages xcom
"""
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# reusable utils and tools
from workflow_lib import get_client_meta, extract_filename_args
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl


args = extract_filename_args(__file__)
print(f'args: {args}')

tmpl_cmd = 'echo custom var1={{ params.var1 }};'
custom_params = {"var1": "43"}

def get_url_params(**kwargs):
    params = kwargs["ti"].xcom_pull_tapd()
    print('tapd url params: {}'.format(params))


# A DAG represents a workflow, a collection of tasks   
with DAG(
    dag_id=args["dag_id"], 
    start_date=datetime(2022, 11, 9), 
    schedule=None,
    catchup=False,
    tags=["xcom", "sample"]) as dag:

    def gather_client_meta():
        get_client_meta(args["client_id"])

    
    # Tasks are represented as operators                                                                                                                                                                                                                      
    extract = BashOperator(
        task_id="extract",
        bash_command=extract_bash_cmd,
        params=custom_params)

    @task()
    def step2():
        print("airflow")

    # Set dependencies between tasks                                                                                                                                                                                                                          
    step1 >> step2()