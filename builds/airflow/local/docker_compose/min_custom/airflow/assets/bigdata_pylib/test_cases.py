##!/usr/local/bin/python3.10

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

def sequence_analysis_abs(debug=False):
    print("# sequence_analysis_abs() #")
    from analysis.dna.caltech_edu.basic import sequence_analysis

    res = sequence_analysis()
    print(f"res: {res}")
    
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
    debug = True

    covidtracking_api(debug)
    #sequence_analysis_abs(debug)
    #test_db_client_abs(debug)
    #test_db_platform_abs(debug)

if __name__ == "__main__":
    main()