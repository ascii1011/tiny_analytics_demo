
from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

def extract_args():
    dag_id = Path(__file__).stem
    return {
        "dag_id": dag_id,
    }

args = extract_args()

tmpl_cmd = 'echo custom var1={{ params.var1 }};'
custom_params = {"var1": "43"}


# A DAG represents a workflow, a collection of tasks                                                                                                                                                                                                          
with DAG(dag_id=args["dag_id"], start_date=datetime(2022, 11, 9), schedule=None) as dag:

    # Tasks are represented as operators                                                                                                                                                                                                                      
    step1 = BashOperator(
        task_id="step1",
        bash_command=tmpl_cmd,
        params=custom_params)

    @task()
    def step2():
        print("airflow")

    # Set dependencies between tasks                                                                                                                                                                                                                          
    step1 >> step2()