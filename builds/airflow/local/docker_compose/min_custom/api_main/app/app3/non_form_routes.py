


from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from lib.ai import *



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
        return redirect(url_for("pet", result=pet_name(request)))

    return render_template("pet.html", result=request.args.get("result"))


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

@app.route("/image_gen2", methods=("GET", "POST"))
def image_gen2():
    if request.method == "POST":
        return redirect(url_for("image_gen", result=generate_images(result)))

    return render_template("image_gen.html", result=request.args.get("result"))

@app.route("/devchatbot", methods=("GET", "POST"))
def devchatbot():
    if request.method == "POST":
        return redirect(url_for("devchatbot", result=dev_chat_bot(request)))

    result = request.args.get("result")
    return render_template("devchatbot.html", result=result)

@app.route("/horrorstorygenerator", methods=("GET", "POST"))
def horrorstorygenerator():
    if request.method == "POST":
        return redirect(url_for("horrorstorygenerator", result=generate_horror_story(request)))

    result = request.args.get("result")
    return render_template("horrorstorygenerator.html", result=result)

@app.route("/chat", methods=("GET", "POST"))
def chat():
    if request.method == "POST":
        return redirect(url_for("chat", result=generic_chat_bot(request)))

    result = request.args.get("result")
    return render_template("chat.html", result=result)

@app.route("/studynotes", methods=("GET", "POST"))
def studynotes():
    if request.method == "POST":
        return redirect(url_for("studynotes", result=study_notes(request)))

    result = request.args.get("result")
    return render_template("studynotes.html", result=result)

@app.route("/createproductname", methods=("GET", "POST"))
def createproductname():
    if request.method == "POST":
        return redirect(url_for("createproductname", result=create_product_name(request)))

    result = request.args.get("result")
    return render_template("createproductname.html", result=result)

