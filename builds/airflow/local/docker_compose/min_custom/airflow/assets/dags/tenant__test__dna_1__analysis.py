

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
#from analysis.dna.caltech_edu.basic import sequence_analysis
from analysis.dna.caltech_edu.basic import get_dna_pair_compute_similarity_scores, get_dna_map_combination_pairs, map_dna_files

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

        ti.xcom_push(key="debug", value='True')
        ti.xcom_push(key="src_data_path", value='/opt/mnt/raw_data/dna/bige105/mabuya_atlantica')
    
    @task
    def list_filenames(ti=None):
        limit = 0
        src_data_path = None
        while limit < 10 and src_data_path == None:
            src_data_path = ti.xcom_pull(task_ids="context", key="src_data_path")
            print(f'resolve attempt({limit}) src_data_path: {src_data_path}')
            limit += 1

        tmp_file_list = get_files_from_path(src_data_path)

        # basically only trying to pull one of the files for this case as the rest are duplicates
        return [file_path for file_path in tmp_file_list if 'mabuya_aln.fasta' in file_path]
    
    @task
    def dna_map(ti=None):
        return map_dna_files(
            ti.xcom_pull(task_ids="list_filenames"), 
            ti.xcom_pull(task_ids="context", key="debug")
            )

    @task
    def dna_combo_pairs(ti=None):
        return get_dna_map_combination_pairs(
            ti.xcom_pull(task_ids="dna_map"), 
            ti.xcom_pull(task_ids="context", key="debug")
            )

    @task
    def scores(ti=None):  
        return get_dna_pair_compute_similarity_scores(
            ti.xcom_pull(task_ids="dna_combo_pairs"), 
            ti.xcom_pull(task_ids="dna_map"), 
            ti.xcom_pull(task_ids="context", key="debug")
            )

    context(args) >> list_filenames() >> dna_map() >> dna_combo_pairs() >> scores()