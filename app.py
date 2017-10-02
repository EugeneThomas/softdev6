from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

# landing page
@app.route("/")
def hello_world():
    return render_template("Form.html")

@app.route("/response")
def response():
    d = request.args
    retStr = d['first']
    retStr += " " + d['last'] + ","
    retStr += " Hi!"
    return render_template('response.html', greet = retStr)

if __name__ == "__main__":
    app.debug = True
    app.run()
