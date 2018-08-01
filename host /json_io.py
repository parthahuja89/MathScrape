import sys

from flask import Flask,render_template, request, redirect , Response
import random,json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/receiver', methods = ['GET ', 'POST'])
def worker():
    #reads the json file
    data = request.get_json()

    result = ""

    for counter in data:
        result += str(counter['make'])


if __name__ == '__main__':
    app.run()

