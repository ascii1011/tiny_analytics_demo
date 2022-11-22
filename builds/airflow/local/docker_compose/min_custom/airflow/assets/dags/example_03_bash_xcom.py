
from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.bash import BashOperator

def extract_args():
    dag_id = Path(__file__).stem
    return {
        "dag_id": dag_id,
    }

args = extract_args()

tmpl_cmd = 'echo push_me_{{ params.var1 }}_{{ params.var2 }}'
custom_params = {"var1": "1", "var2": "2"}

with DAG(
    dag_id=args["dag_id"], 
    start_date=datetime(2022, 11, 9), 
    schedule=None,
    catchup=False,
    tags=["xcom", "sample"]) as dag:

    base = BashOperator(
        task_id="base", 
        bash_command="echo base xcom examples",
        do_xcom_push=False)

    step1_push = BashOperator(
        task_id="step1_push", 
        bash_command=tmpl_cmd,
        params=custom_params)

    step2_push = BashOperator(
        task_id="step2_push", 
        bash_command=tmpl_cmd,
        params={"var1": "111", "var2": "g"})

    step3_pull = BashOperator(
        task_id="step3_pull", 
        bash_command='echo "xcoms: {{ ti.xcom_pull(task_ids=[\'step1_push\', \'step2_push\']) }}"',
        do_xcom_push=False)

    base >> step1_push >> step2_push >> step3_pull
