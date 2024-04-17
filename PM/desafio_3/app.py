from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)


@app.route("/")
def home_page():
    return redirect ("/home")


@app.route("/<name>")
def get_page(name):
    directors = json.load(open("./templates/directors_films.json"))
    if request.method == "POST":
        req = request.form
        search = req["search"]
        return redirect("/directors")
    
    if name == "home":
        return render_template(f"index.html", directors = directors)
    return render_template(f"{name}.html", directors = directors)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)