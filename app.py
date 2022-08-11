# coding utf-8
from flask import Flask
app = Flask("project")

@app.route("/")
def hello_world():
    html_string = "<html><head><title>Hello World</title></head><body><h1>Hello World</h1></body></html>"
    return html_string, 200

app.run()
