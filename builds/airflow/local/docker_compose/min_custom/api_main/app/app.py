#!/opt/venv/bin/python
import os
import requests
from pprint import pprint

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from utils import download_image, generate_prompt


@app.route("/")
def index():
    return render_template("index.html")


def trigger_dag_v2(dag_id=""):
    """ only for use from either the host machine (aka mac) or from a container outside of the network that airflow container is apart of"""
    try:
        api_url = f"{os.environ['AIRFLOW_API_URL_IN_NETWORK']}"
        endpoint = "/dags/example_02_custom/dagRuns"
        api_endpoint = api_url + endpoint
        print(f'{api_endpoint=}')
        headers = {'Content-Type': 'application/json'}
        data = '{ "conf": {} }'
        resp = requests.post(api_endpoint, auth=(os.environ['AIRFLOW_USERNAME'], os.environ['AIRFLOW_PASSWORD']), headers=headers, data=data, timeout=1.5) 
        pprint(resp)

    except Exception as e:
        print(f'err: {e}')

"""
def trigger_dag(dag_id):
    print(f'## trigger_dag({dag_id}) ##')

    host = os.environ["AIRFLOW_HOST"]
    username = "admin"
    password = "airflow"
    #api_endpoint = "http://192.168.192.5:8251/api/v1/dags/{dag_id}/dagRuns"
    api_endpoint = f"http://{host}:8251/api/v1/dags/example_02_custom/dagRuns"
    print(f"\t- {api_endpoint=}")

    headers = {'Content-Type': 'application/json'} #, 'username': username, 'password': password}
    print(f"\t- {headers=}")
    data = '{ "conf": "{}" }'
    print(f"\t- {data=}")
    #return requests.post(api_endpoint, headers=headers, data=data)
    return requests.post(api_endpoint, auth=(username, password), headers=headers, data=data)
"""
@app.route("/airflow_request", methods=("GET", "POST"))
def airflow_request():
    """use a dag_id from the form to trigger an airflow DAG"""
    print('\nairflow_request:')
    example_dag_id = "example_02_custom"
    example_url = f"http://localhost:8251/api/v1/dags/{example_dag_id}/dagRuns"
    
    if request.method == "POST":
        print('\tpost!')
        dag_id = request.form["dag_id"]
        print(f"{dag_id=}")
        response = trigger_dag_v2(dag_id)

        print(f"{response=}({type(response)})")

        return redirect(url_for("airflow_request", result=response))

    result = request.args.get("result")
    return render_template("airflow_request.html", example_url=example_url, example_dag_id=example_dag_id, result=result)

@app.route("/pet", methods=("GET", "POST"))
def pet():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("pet", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("pet.html", result=result)

@app.route("/image_gen", methods=("GET", "POST"))
def image_gen():
    """
    1 to 10 images 
    res: 256x256, 512x512, or 1024x1024 pixels"""
    if request.method == "POST":
        # keywords example: "a white siamese cat"
        keywords = request.form["keywords"]
        print(f"{keywords=}")

        response = openai.Image.create(
            prompt=keywords,
            n=2,
            size="1024x1024"
        )
        print(f"{len(response['data'])=}")
        result = ""
        for i in range(len(response['data'])):
            image_url = response['data'][i]['url']
            print(f"{i}){image_url=}")
            if result == "":
                result = download_image(image_url, prefix='_'.join(keywords.split()))
            else:
                result += " | " + download_image(image_url, prefix='_'.join(keywords.split()))
        print(f"{result=}")
        return redirect(url_for("image_gen", result=result))

    result = request.args.get("result")
    return render_template("image_gen.html", result=result)


@app.route("/devchatbot", methods=("GET", "POST"))
def devchatbot():
    """
    prompt example:
    "You: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do you make an alert appear after 10 seconds?\nJavaScript chatbot"
    """
    if request.method == "POST":
        chat_input = request.form["chat_input"]
        
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=chat_input,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"]
        )
        print(f"{response=}")
        return redirect(url_for("devchatbot", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("devchatbot.html", result=result)

@app.route("/horrorstorygenerator", methods=("GET", "POST"))
def horrorstorygenerator():
    """
    prompt example:               
    Topic: wrench\nTwo-Sentence Horror Story:
    """
    if request.method == "POST":
        keywords = request.form["keywords"]
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=keywords,
            temperature=0.8,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        print(f"{response=}")
        return redirect(url_for("horrorstorygenerator", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("horrorstorygenerator.html", result=result)


@app.route("/chat", methods=("GET", "POST"))
def chat():
    """
    prompt example:
    The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:
    """
    if request.method == "POST":
        chat_input = request.form["chat_input"]
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chat_input,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        print(f"{response=}")
        return redirect(url_for("chat", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("chat.html", result=result)

@app.route("/studynotes", methods=("GET", "POST"))
def studynotes():
    """
    prompt example:
    The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:
    """
    if request.method == "POST":
        keywords = request.form["keywords"]
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=keywords,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        print(f"{response=}")
        return redirect(url_for("studynotes", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("studynotes.html", result=result)


@app.route("/createproductname", methods=("GET", "POST"))
def createproductname():
    """
    prompt example:
    Product description: A home milkshake maker\nSeed words: fast, healthy, compact.\nProduct names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n\nProduct description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.
    """
    if request.method == "POST":
        keywords = request.form["keywords"]
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=keywords,
            temperature=0.8,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        print(f"{response=}")
        return redirect(url_for("createproductname", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("createproductname.html", result=result)



