

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
from workflow_lib import extract_filename_args, get_files_from_path, get_line_count_from_file
from bash_templates import extract_bash_cmd_tmpl, load_bash_cmd_tmpl

args = extract_filename_args(__file__)

with DAG(
    dag_id=args["dag_id"], 
    start_date=pendulum.datetime(2022, 11, 28, tz="UTC"), 
    schedule=None,
    catchup=False,
    tags=args["tags"]) as dag:


    @task()
    def context(args, ti=None):
        """get account meta.  typically retrived by db"""
        print(f'args: {args}')

        ti.xcom_push(key="src_data_path", value='/opt/mnt/raw_data/dna/bige105/mabuya_atlantica')
    


    @task
    def list_filenames(ti=None):
        limit = 0
        src_data_path = None
        while limit < 10 and src_data_path == None:
            src_data_path = ti.xcom_pull(task_ids="context", key="src_data_path")
            print(f'{limit}) src_data_path: {src_data_path}')
            limit += 1

        tmp_file_list = get_files_from_path(src_data_path)
        final_list = [file_path for file_path in tmp_file_list if 'mabuya_aln.fasta' in file_path]
        return final_list

    @task
    def count_lines(filename):
        return get_line_count_from_file(filename)

    @task
    def total(lines):
        return sum(lines)

    counts = count_lines.expand(
        filename=list_filenames()
    )

    context(args) >> total(lines=counts)