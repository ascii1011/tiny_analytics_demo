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


def main():
    debug = False

    #covidtracking_api(debug)
    #sequence_analysis_abs(debug)
    sequence_analysis_absv2(debug)
    #test_db_client_abs(debug)
    #test_db_platform_abs(debug)

if __name__ == "__main__":
    main()