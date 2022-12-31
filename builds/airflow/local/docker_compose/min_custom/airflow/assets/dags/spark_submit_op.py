

from datetime import timedelta

from pprint import pprint

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

from testing.generate_data_files import generate_files

with DAG('spark_submit_demo', 
        dagrun_timeout=timedelta(minutes=6),
        description='use case of sparkoperator in airflow',
        start_date=pendulum.datetime(2022, 12, 6, tz="UTC"),
        max_active_runs=1,
        schedule_interval=None,
        catchup=False
    ) as dag:


    @task
    def data_files():
        path = '/opt/mnt/raw_data/test/generated'

        args = {
            "context": {"client": "moomoo", "project": "ube"},
            "file_count": 3,
            "row_count": 4,
            "cols": [
                {"col_name": "rand_chars", "pattern": "random", "type": "ascii_lowercase", "len": 3},
            ],
            "path": path,
            "debug": True,
        }
        
        report = generate_files(**args)
        print('\nreport:')
        pprint(report)

        return report["path"]

    spark_submit_local = SparkSubmitOperator(
		application ='/opt/mnt/bigdata/pylib/anant_us__spark_etl.py' ,
		conn_id='spark_local', 
		task_id='spark_submit_task'
    )

    data_files() >> spark_submit_local

if __name__ == "__main__":
    dag.cli()



