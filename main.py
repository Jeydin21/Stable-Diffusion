from flask import Flask, render_template, request
from functions import *

app = Flask('Flask App', static_folder='static', template_folder="templates")

@app.route('/', methods = ["GET", "POST"])
def home():
  return render_template("index.html")

@app.route('/results', methods = ["GET", "POST"])
def resultsPage():
  prompt = str(request.form.get('prompt'))
  amount = str(request.form.get('amount'))
  images = getData(prompt, amount)
  return render_template("results.html", data = images)

app.run(host = '0.0.0.0', port = 6969, threaded = True)