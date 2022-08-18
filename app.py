# coding utf-8
from flask import Flask, render_template, request, session, redirect, url_for
from config import secret_key, admin_secret

app = Flask("project")
app.secret_key = secret_key

@app.route("/")
def hello_world():
    name = "Minato Namikaze"
    products = [
        { "name": "Nintendo Switch", "price": 300 },
        { "name": "Playstation 5", "price": 500 },
        { "name": "Xbox Series X", "price": 500 },
    ]
    return render_template("hello.html", name=name, products=products), 200

@app.route("/test")
@app.route("/test/<variable>")
def funcao_teste(variable = ""):
    return f"New test route<br>Variable: {variable}", 200

@app.route("/form")
def form():
    return render_template("form.html"), 200

@app.route("/form_receive", methods=["POST"])
def form_recebe():
    if request.method == "POST":
        name = request.form["name"]
        return f"Name: {name}"
    return "Forbidden. GET method is not allowed!", 200

@app.route("/login")
def login():
    return render_template("login.html"), 200

@app.route("/validate_login", methods=["POST"])
def validate_login():
    if (request.form["username"] == admin_secret["username"] and 
        request.form["password"] == admin_secret["password"]):
        session["username"] = request.form["username"]
        session["code"] = 1
        return redirect(url_for("restricted_access"))
    else:
        return "invalid username/password, try again", 401

@app.route("/restricted")
def restricted_access():
    if session["code"] == 1:
        return f"Welcome to the restricted area, {session['username']}", 200
    else:
        return "Invalid access", 401

app.run()
