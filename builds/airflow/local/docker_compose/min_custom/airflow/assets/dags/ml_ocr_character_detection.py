
# [dag] ml_ocr_character_detection.py
"""
This DAG is a first step in extracting characters from images and 
attempting to detect what language they may have come from.


src: https://builtin.com/data-science/python-ocr [1st part]
"""

import pendulum
from airflow import DAG
from airflow.decorators import task

from workflow_lib import get_files_from_path, path_from_xcom


args = {
    "src_data_path": "/opt/mnt/raw_data/dna",
    "debug": True,
}

# A DAG represents a workflow, a collection of tasks #
with DAG(dag_id="ml_ocr_character_detection", start_date=pendulum.datetime(2022, 11, 29, tz="UTC"), schedule=None) as dag:

    @task()
    def context(args, ti=None):
        """get account meta.  typically retrived by db"""
        print(f'{args=}')

        ti.xcom_push(key="debug", value='True')
        ti.xcom_push(key="src_data_path", value=args["src_data_path"])
    
    @task
    def extract_characters(args, ti=None):

        from PIL import Image
        import pytesseract
        import numpy as np
        import cv2

        file_list = get_files_from_path(args["src_data_path"])

        for i, file_path in enumerate(file_list):
             if file_path.endswith('.jpg'):
                #filename = '/opt/mnt/raw_data/dna/1_python-ocr.jpg'
                img = np.array(Image.open(file_path))
                text = pytesseract.image_to_string(img)
                text = text.strip()
                print(f"{i}) [{file_path}] text: '{text}'")

                if text == "":
                    print('trying to cut noise...')
                    norm_img = np.zeros((img.shape[0], img.shape[1]))
                    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
                    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
                    img = cv2.GaussianBlur(img, (1, 1), 0)
                    text = pytesseract.image_to_string(img)
                    print(f"--cut noise text: {text}")



    context(args) >> extract_characters(args)