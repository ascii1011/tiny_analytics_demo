
"""
https://docs.astronomer.io/learn/airflow-passing-data-between-tasks
https://covidtracking.com/data/api
"""
import json
import pendulum

from airflow import DAG
from airflow.decorators import task
#from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

from api import get_request

with DAG('util__covid_tracking',
         start_date=pendulum.datetime(2022, 11, 29, tz="UTC"),
         max_active_runs=1,
         schedule_interval="@daily",
         catchup=False
         ) as dag:

    @task()
    def current_us_covid_stats():

        field_url = 'https://api.covidtracking.com/v1/us/current.csv'
        field_res = get_request(field_url)
        fields, example_row = field_res.strip().split('\n')
        fields = fields.split(',')
        print(f"\nCurrent Fields: {fields}")

        data_url = 'https://api.covidtracking.com/v1/us/current.json'
        data_res = get_request(data_url)
        data = json.loads(data_res)[0]
        print(f"\ndata:")
        for k,v in data.items():
            print(f"{k} = '{v}'")

    @task()
    def wa_increase():
        """
        Gets totalTestResultsIncrease field from Covid API for given state and returns value
        """

        state = 'wa'
        url = f'https://api.covidtracking.com/v1/states/{state}/current.json'

        data_res = get_request(url)
        print(f"data_res: {data_res}")

        data = json.loads(data_res)
        print(f"data: {data}")

        print(f"increase: {data['totalTestResultsIncrease']}")

        #res = get_request(url)
        #return json.loads(res)[0]['totalTestResultsIncrease']

    current_us_covid_stats() >> wa_increase()