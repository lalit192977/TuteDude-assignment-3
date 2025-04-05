from flask import Flask, request, render_template
import requests
import os


BACKEND_URL = "http://127.0.0.1:9000"
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
	# return render_template("index.html")

@app.route("/submit", methods= ["POST"])
def submit():
      form_data = dict(request.form)
      requests.post(BACKEND_URL + "/submit", json=form_data)
      return "Data submitted successfully"

if __name__ == "__main__":
	app.run(debug=True, port=8000)
