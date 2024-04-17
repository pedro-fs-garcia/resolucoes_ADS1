from flask import Flask, render_template, redirect, request, url_for
import json

app = Flask(__name__)


@app.route("/")
def home_page():
    return redirect ("/home")


@app.route("/<name>")
def get_page(name):
    directors = json.load(open("./templates/directors_films.json", encoding="UTF-8"))
    perguntas = json.load(open("./templates/questions.json", encoding="UTF-8"))
    if name == "home":
        return render_template(f"index.html", directors = directors, perguntas=perguntas)

    return render_template(f"{name}.html", directors = directors, perguntas=perguntas)


@app.route("/get_answer", methods=["POST", "GET"])
def get_answer():
    perguntas = json.load(open("./templates/questions.json"))
    respostas={}
    for i in range(1,6):
        respostas[f"answer{i}"] = request.form[f"answer{i}"]
    
    return f"<p>{respostas.values()}</p>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)