
#!/usr/local/bin/python3.10
import os
import requests
import json
from pprint import pprint

def test_get_list():
    
    username = "admin"
    password = "airflow"
    port = "8080"
        
    try:
        api_endpoint = f"http://localhost:{port}/api/v1/dags?limit=100&only_active=true"
        headers = {'Content-Type': 'application/json'}
        data = '{ "conf": "{}" }'
        resp = requests.get(api_endpoint, auth=(username, password), headers=headers, data=data, timeout=1.5)
        print(f"{resp=}({type(resp)})")

        resp_dict = (resp.json())
        print(f"{type(resp_dict)=}")
        for key, values in resp_dict.items():
            print(f"\n{key=}:")
            if isinstance(values, list):
                for v in values:
                    print(f"\tul: {v=}")
            else:
                print(f"\tdiv: {values=}")    
            
                
        
    except Exception as e:
        print(f"err: {e}")

        

    """

    res = requests.get(api_endpoint, auth=(username, password), headers=headers, data=data, timeout=1.5)
    print(f"{res=}({type(res)})")
    from pprint import pprint
    #pprint(dir(res))
    
    'iter_content',
    'iter_lines',


        res=<Response [200]>(<class 'requests.models.Response'>)
        res.apparent_encoding='ascii'
        res.encoding='utf-8'
        res.headers={'Server': 'gunicorn', 'Date': 'Mon, 02 Jan 2023 17:46:56 GMT', 'Connection': 'close', 'Content-Type': 'application/json', 'Content-Length': '13021', 'X-Robots-Tag': 'noindex, nofollow'}
        res.history=[]
        res.ok=True
        res.raw=<urllib3.response.HTTPResponse object at 0x7f9b866249d0>
        res.status_code=200
        res.url='http://localhost:8080/api/v1/dags?limit=100&only_active=true'
    
    print(f'{res.apparent_encoding=}')
    #print(f'{res.content=}')
    print(f'{res.encoding=}')
    print(f'{res.headers=}')
    print(f'{res.history=}')
    print(f'{res.ok=}')
    print(f'{res.raw=}')
    print(f'{res.status_code=}')
    #print(f'{res.text=}')
    print(f'{res.url=}')
    #pprint(res.json())
        
    try:
        api_endpoint = f"http://localhost:{port}/api/v1/dags?limit=100&only_active=true"
        headers = {'Content-Type': 'application/json', 'username': username, 'password': password}
        data = '{ "conf": "{}" }'
        res = requests.get(api_endpoint, headers=headers, data=data, timeout=1.5)
        print(f"{res=}({type(res)})")
        
    except Exception as e:
        print(f"err: {e}")
    """

        

def test_scenarios():

    #url = "http://localhost:8251/api/v1/dags/{dag_id}/dagRuns"
    username = "admin"
    password = "airflow"
    port = "8251"
    host_names = ["localhost", "127.0.0.1", "0.0.0.0", "192.168.192.5", "192.168.80.7", "airflow", "min_custom_airflow_1"]

    """
    print('\nno auth')
    for host in host_names:
        try:
            api_endpoint = f"http://{host}:{port}/api/v1/dags/example_02_custom/dagRuns"
            headers = {'Content-Type': 'application/json'} #, 'username': username, 'password': password}
            data = '{ "conf": "{}" }'
            requests.post(api_endpoint, headers=headers, data=data, timeout=1.5) #auth=(username, password),
            print(f'{host=} .. IT WORKED!!!!!')
        except Exception as e:
            es = str(e).split(':')
            if len(es) < 4:
                es = str(e).split(',')
                print(f'err: {es[0]}, {es[-1]}')
            else:
                print(f'err: {es[0]}, {es[-2]}, {es[-1]}')

    print('\nauth in headers...')
    for host in host_names:
        try:
            api_endpoint = f"http://{host}:{port}/api/v1/dags/example_02_custom/dagRuns"
            headers = {'Content-Type': 'application/json', 'username': username, 'password': password}
            data = '{ "conf": "{}" }'
            requests.post(api_endpoint, headers=headers, data=data, timeout=1.5)
            print(f'{host=} .. IT WORKED!!!!!')
        except Exception as e:
            es = str(e).split(':')
            if len(es) < 4:
                es = str(e).split(',')
                print(f'err: {es[0]}, {es[-1]}')
            else:
                print(f'err: {es[0]}, {es[-2]}, {es[-1]}')
    """
    print('\nauth in post-auth')
    if os.environ.get("AIRFLOW_API_URL"):
        print("airflow_host found")
        #host_names.append(os.environ["AIRFLOW_HOST"])
        host_names.append(os.environ["AIRFLOW_API_URL"])
    for host in host_names:
        try:
            api_endpoint = f"http://{host}:{port}/api/v1/dags/example_02_custom/dagRuns"
            headers = {'Content-Type': 'application/json'}
            data = '{ "conf": "{}" }'
            requests.post(api_endpoint, auth=(username, password), headers=headers, data=data, timeout=1.5) 
            print(f'{host=} .. IT WORKED!!!!!')
        except Exception as e:
            es = str(e).split(':')
            if len(es) < 4:
                es = str(e).split(',')
                print(f'err: {es[0]}, {es[-1]}')
            else:
                print(f'err: {es[0]}, {es[-2]}, {es[-1]}')

def test_post_v3():
    
    if os.environ.get("AIRFLOW_API_URL"):
        try:
            username = os.environ['AIRFLOW_USERNAME']
            password = os.environ['AIRFLOW_PASSWORD']
            endpoint = "/dags/example_02_custom/dagRuns"
            api = f"{os.environ['AIRFLOW_API_URL_IN_NETWORK']}"
            api_endpoint = api.replace("8251", "8080") + endpoint
            print(f'{api_endpoint=}')
            headers = {'Content-Type': 'application/json'}
            data = '{ "conf": "{}" }'
            requests.post(api_endpoint, auth=(username, password), headers=headers, data=data, timeout=1.5) 

        except Exception as e:
            es = str(e).split(':')
            if len(es) < 4:
                es = str(e).split(',')
                print(f'err: {es[0]}, {es[-1]}')
            else:
                print(f'err: {es[0]}, {es[-2]}, {es[-1]}')

def print_json_response(resp):
    resp_dict = resp.json()
    print(f"{type(resp_dict)=}")
    pprint(resp_dict)
    """
    for key, values in resp_dict.items():
        print(f"\n{key=}:")
        if isinstance(values, list):
            for v in values:
                print(f"\tul: {v=}")
        else:
            print(f"\tdiv: {values=}")  
    """

def test_airflow_api_from_within_container_on_same_network():
    
    try:
        api_url = f"{os.environ['AIRFLOW_API_URL_IN_NETWORK']}"
        endpoint = "/dags/example_02_custom/dagRuns"
        api_endpoint = api_url + endpoint
        print(f'{api_endpoint=}')
        headers = {'Content-Type': 'application/json'}
        data = '{ "conf": {} }'
        resp = requests.post(api_endpoint, auth=(os.environ['AIRFLOW_USERNAME'], os.environ['AIRFLOW_PASSWORD']), headers=headers, data=data, timeout=1.5) 
        print_json_response(resp)

    except Exception as e:
        print(f'err: {e}')

def test_airflow_api_from_the_host():
    """ only for use from either the host machine (aka mac) or from a container outside of the network that airflow container is apart of"""
    try:
        api_url = f"{os.environ['AIRFLOW_API_URL_FROM_HOST']}"
        endpoint = "/dags/example_02_custom/dagRuns"
        api_endpoint = api_url + endpoint
        print(f'{api_endpoint=}')
        headers = {'Content-Type': 'application/json'}
        data = '{ "conf": "{}" }'
        resp = requests.post(api_endpoint, auth=(os.environ['AIRFLOW_USERNAME'], os.environ['AIRFLOW_PASSWORD']), headers=headers, data=data, timeout=1.5) 
        print_json_response(resp)

    except Exception as e:
        print(f'err: {e}')

    

def main():
    #test_scenarios()
    #test_get_list()
    #test_post_v3()

    test_airflow_api_from_within_container_on_same_network()
    


if __name__ == "__main__":
    main()
