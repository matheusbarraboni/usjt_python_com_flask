# coding utf-8
from flask import Flask, render_template
app = Flask("project")

@app.route("/")
def hello_world():
    name = "Minato Namikaze"
    products = [
        { "name": "Nintendo Switch", "price": 300 },
        { "name": "Playstation 5", "price": 500 },
        { "name": "Xbox Series X", "price": 500 },
    ]
    return render_template("hello.html", name=name, products=products), 200


app.run()
