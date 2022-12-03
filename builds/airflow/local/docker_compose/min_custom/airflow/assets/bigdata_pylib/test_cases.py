#!/usr/local/bin/python3.10

import os
import pathlib

from pprint import pprint

def test_db_client_abs(debug=False):
    """new db.mongo lib support Nov, 2022"""
    from db.mongo import client_get_file_criteria
    
    pprint(client_get_file_criteria('lala', debug))


def test_db_platform_abs(debug=False):
    """new db.mongo lib support Nov, 2022"""
    from db.mongo import platform_get_project_meta
    pprint(platform_get_project_meta('lala', 'ctc', debug))


def sequence_analysis_absv2(debug=False):
    if debug: print("# sequence_analysis_absv2!!() #")
    from analysis.dna.caltech_edu.basic import get_dna_pair_compute_similarity_scores, get_dna_map_combination_pairs, map_dna_files, to_graph_edges
    from algorithms.dijkstra import dijk_spla
    list_of_files = ['/opt/mnt/raw_data/dna/bige105/mabuya_atlantica/mabuya_aln.fasta',]
    
    dna_map = map_dna_files(list_of_files, debug)
    combo_pairs = get_dna_map_combination_pairs(dna_map, debug)
    scores = get_dna_pair_compute_similarity_scores(combo_pairs, dna_map, debug)
    print('\nscores:')
    pprint(scores)

    edges = to_graph_edges(scores, debug)
    print('\n#edges:')
    pprint(edges)

    res = dijk_spla(edges)
    print('dijkstra:')
    pprint(res)



def sequence_analysis_abs(debug=False):
    if debug: print("# sequence_analysis_abs() #")
    from analysis.dna.caltech_edu.basic import sequence_analysis
    list_of_files = ['/opt/mnt/raw_data/dna/bige105/mabuya_atlantica/mabuya_aln.fasta',]
    sequence_analysis(list_of_files, debug)
    
def covidtracking_api(debug=False):
    # Gets totalTestResultsIncrease field from Covid API for given state and returns value
    import requests
    import json

    def send_request(url):
        res = []
        try:
            raw = requests.get(url)
            #print(f"raw: {raw}")
            #print(f"::{dir(raw)}")

            res = raw.text
            #print(f"res: {res}")

        except Exception as e:
            print(f"error: {e}")

        finally:
            return res

    def get_format(url):
        output = send_request(url)
        
        fields, example_row = output.strip().split('\n')
        return fields.split(',')

    def get_data(url):
        output = send_request(url)
        data = json.loads(output)[0]
        return data

    def get_us_covid_stats():
        field_url = 'https://api.covidtracking.com/v1/us/current.csv'
        fields = get_format(field_url)
        print(f"\nfields: {fields}")

        data_url = 'https://api.covidtracking.com/v1/us/current.json'
        data = get_data(data_url)
        print(f"\ndata:")
        pprint(data)

    get_us_covid_stats()

def tesseract_ocr_test(debug):
    from PIL import Image
    import pytesseract
    import numpy as np

    filename = '/opt/mnt/raw_data/dna/1_python-ocr.jpg'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    print(f"text: {text}")



    filename2 = '/opt/mnt/raw_data/dna/1_python-ocr.jpg'
    img2 = np.array(Image.open(filename2))
    text2 = pytesseract.image_to_string(img2)
    print(f"text2: {text2}")

def tool__display_dir_content():
    from workflow_lib import get_files_from_path, display_dir_content

    path = "/opt/mnt/raw_data/dna"
    print(f"\nget_files_from_path: {get_files_from_path(path)}")

    print(f"\ndisplay_dir_content: {display_dir_content(path)}")

def test_ls_files():
    from workflow_lib import ls_files
    path = "/opt/mnt/raw_data/dna"
    ls_files(path, ['jpg'])

def test_image_to_text_abs(debug=False):
    print('^^text image_to_text_abs:')
    from convert.ocr import image_dir_to_text
    path = "/opt/mnt/raw_data/dna"
    resolution = 'high' #['low','high']
    results = image_dir_to_text(path, resolution, debug=debug)
    print('\n^^results:')
    pprint(results)


def main():
    debug = False
    print('')
    print('===================================')
    print(f'=====start test ({debug=}) ====\n-')

    test_image_to_text_abs(debug)
    
    #ls_files()

    #tool__display_dir_content()

    #tesseract_ocr_test(debug)

    #covidtracking_api(debug)

    #sequence_analysis_abs(debug)
    #sequence_analysis_absv2(debug)

    #test_db_client_abs(debug)
    #test_db_platform_abs(debug)

    print('-\n========== end test ==========\n')

if __name__ == "__main__":
    main()