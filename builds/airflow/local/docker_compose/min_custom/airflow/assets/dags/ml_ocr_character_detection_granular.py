

# [dag] ml_ocr_character_detection.py
"""
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
    def extract_characters(args, ti=None):

        from PIL import Image
        from pytesseract import Output
        import pytesseract
        import numpy as np
        import cv2

        debug = ti.xcom_pull(task_ids="context", key="debug")

        path = args["src_data_path"]
        file_list = get_files_from_path(path)

        for i, file_path in enumerate(file_list):
             if file_path.endswith('.jpg'):
                print('')
                print('___________________________________')
                print(f"file_path: {file_path}")

                ext = '.' + file_path.split('.')[-1]


                image = cv2.imread(file_path)

                if debug: 
                    print('')
                    print('results:')
                results = pytesseract.image_to_data(image, output_type=Output.DICT)
                for k, v in results.items():
                    if debug: 
                        print(f">> {k}: {v}")

                text_concat = ''.join(results["text"]).strip()
                if debug: 
                    print('')
                    print(f"\n{text_concat=}")

                if text_concat == "":
                    #raise AirflowFailException("No 'text' elements found !!!")
                    print('NO TEXT FOUND, MOVING ON...')
                    continue

                """
                for i in range(0, len(results["text"])):
                    x = results["left"][i]
                    y = results["top"][i]

                    w = results["width"][i]
                    h = results["height"][i]

                    text = results["text"][i]
                    conf = int(results["conf"][i])

                    if conf > 70:
                        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(image, text, (x, y - 10), 

                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
                # commented out as we do not want to actually try show the images within a DAG log 
                #cv2.imshow(image)

                try:
                    save_as_file_path = file_path.replace(ext, '1'+ext)
                    print('')
                    print(f"{save_as_file_path=}")
                    cv2.imwrite(save_as_file_path, image)
                    cv2.waitKey(0)
                except:
                    pass
                """

        ls_files(args["src_data_path"], ['jpg'])

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


    context(args) >> extract_characters(args) >> ocr_lowres(args) >> ocr_highres(args)