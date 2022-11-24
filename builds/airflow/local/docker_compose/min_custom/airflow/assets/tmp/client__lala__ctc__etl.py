
"""
This DAG is an example of what a real workflow might look like.
Of course this is a slimed down version and has some create resources
until real sources can be built up.

Overview:
 - build out basic workflow, templating, abstraction, and support libraries

Note:  This only a simple example.  Real world scenarios are much more complex with many services backing them.

This DAG shall be triggered automatically by another process after client data has landed in an ingestion area.
The process below shows a process where
 - step 1) filename args: the dag filename provides basic client/project/workflow indicators
 - step 2) project_meta: project specific meta data(from filename args). 
            holds various meta for down stream operations (ex. routing, validation, etc..)
 - step 3) batch_id: should of been provided with the triggered meta.
 - step 4) extract: moves uploaded files to staging; extract if needed
 - step 5) transform: normalization, triggers possible verification or modification of data
 - step 6) load: copies extracted/transformed data to a data store for further use

~~~ This DAG under construction ~~~~
~~-- WARNING - IN PROGRESS --~~

"""

from datetime import datetime
import random

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# reusable utils and tools
from workflow_lib import get_account_meta, extract_filename_args
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl

args = extract_filename_args(__file__)
#print(f'args: {args}')                                                                                                                                                                                                                            


@task()
def project_meta(args):
    """get account meta.  typically retrived by db"""
    a = get_account_meta(args["client_id"])

    return a["project_meta"][args["project_id"]]


@task()
def batch_id():
    """returns a batch_id.  typically passed when this DAG is triggered"""
    bid = random.randint(10000,100000)
    print(f'bid: {bid}')
    return bid

@task()
def transform(args, **context):
    """Works on staging area data might 
    performs normalization, verification, or even  validation
    """
    print('transforming ... ')
    print(f'ti: {str(context["ti"])}')
    print(f'args: {str(args)}')
    
    bid = context["ti"].xcom_pull(task_ids=['batch_id'])[0]
    print(f'bid: {bid}')
    
    project_id = context["ti"].xcom_pull(task_ids=['project_meta'])[0]
    print(f'project_id: {project_id}')

    

#def get_url_params(**kwargs):
#    params = kwargs["ti"].xcom_pull_tapd()
#    print('tapd url params: {}'.format(params))
 
with DAG(
    dag_id=args["dag_id"], 
    start_date=datetime(2022, 10, 10), 
    schedule=None,
    catchup=False) as dag:

    op_project_meta = project_meta(args)

    op_batch_id = batch_id()

    # Copies data from ingestion area to staging and might extract if needed (zip, tar.gz, etc..)
    # typically data is not moved because of verification and historical purposes.  important is downstream data is lost (can replay)
    op_extract = BashOperator(
        task_id="extract",
        bash_command=extract_bash_cmd_tmpl,
        params=args)

    
    op_transform = transform(args)

    # Copy data from staging to a different location for endpoint or possibly analytics 
    load = BashOperator(
        task_id="load",
        bash_command=load_bash_cmd_tmpl,
        params=args)

    # Set dependencies between tasks                                                                                                                                                                                                                         
    op_project_meta >> op_batch_id >> op_extract >> op_transform >> load
