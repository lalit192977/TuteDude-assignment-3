from flask import Flask, request
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo



load_dotenv()
app = Flask(__name__)

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["flask_tutorial"]
collection = db["todo_items"]


@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello :) from Backend for Todo_Task"

@app.route("/submit", methods =['POST'])
def submit():
    form_data = request.json
    print(form_data)
    collection.insert_one(form_data)
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True, port=9000)


