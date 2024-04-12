from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<name>")
def get_page(name):
    directors = json.load(open("./templates/directors_films.json"))
    if name == "home":
        return home_page()
    return render_template(f"{name}.html", directors = directors)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)