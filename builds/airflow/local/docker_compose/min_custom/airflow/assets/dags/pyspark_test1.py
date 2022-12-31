

from datetime import timedelta

from pprint import pprint

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG('pyspark_test', 
        dagrun_timeout=timedelta(minutes=3),
        description='use case of sparkoperator in airflow',
        start_date=pendulum.datetime(2022, 12, 6, tz="UTC"),
        max_active_runs=1,
        schedule_interval=None,
        catchup=False
    ) as dag:

    spark_submit_local = SparkSubmitOperator(
		application ='/opt/mnt/bigdata/pylib/spark/app/pyspark_app_test.py' ,
		conn_id='spark_custom_remote', 
		task_id='pyspark_test_task'
        #application_args="{{ ds }}",
    )

    spark_submit_local



