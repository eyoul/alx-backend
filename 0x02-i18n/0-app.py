from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('0-index.html', name=name)