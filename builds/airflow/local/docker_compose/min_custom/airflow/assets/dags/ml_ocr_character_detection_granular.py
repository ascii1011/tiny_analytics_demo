

# [dag] ml_ocr_character_detection.py
""" updated
This DAG is almost the same as the first version, except 
it appears to drill down and found out exactly where it 
needs to apply its features too, instead of the entire image.
This is an important point as the process in this DAG 
is best suited for high quality image processing pipelines.
High quanlity images means a lot of calculations and in pipelines
it is best to keep those calculations to a minimum.

src: https://builtin.com/data-science/python-ocr [2nd part]
"""

import os
from pathlib import Path

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.exceptions import AirflowFailException

from workflow_lib import get_files_from_path, display_dir_content, ls_files


args = {
    "src_data_path": "/opt/mnt/raw_data/dna",
    "debug": True,
}

# A DAG represents a workflow, a collection of tasks #
with DAG(dag_id="ml_ocr_character_detection_granular", start_date=pendulum.datetime(2022, 11, 29, tz="UTC"), schedule=None) as dag:

    @task()
    def context(args, ti=None):
        """get account meta.  typically retrived by db"""
        print(f'{args=}')

        ti.xcom_push(key="debug", value=args["debug"])
        ti.xcom_push(key="src_data_path", value=args["src_data_path"])

    @task
    def ocr_lowres(args):
        from convert.ocr import image_dir_to_text
        resolution = 'low' #['low','high']
        results = image_dir_to_text(args["src_data_path"], resolution, args["debug"])
        print(f"{results=}")

    @task
    def ocr_highres(args):
        from convert.ocr import image_dir_to_text
        resolution = 'high' #['low','high']
        results = image_dir_to_text(args["src_data_path"], resolution, args["debug"])
        print(f"{results=}")


    context(args) >>  ocr_lowres(args) >> ocr_highres(args)