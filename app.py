# coding utf-8
from flask import Flask, render_template
app = Flask("project")

@app.route("/")
def hello_world():
    return render_template("hello.html"), 200

app.run()
