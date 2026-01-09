from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["pelerinage"]
collection = db["inscriptions"]

@app.route("/", methods=["GET"])
def home():
    return {"status": "API OK"}

@app.route("/inscription", methods=["POST"])
def inscription():
    data = request.json

    if not data:
        return jsonify({"error": "Données manquantes"}), 400

    collection.insert_one(data)

    return jsonify({"message": "Inscription enregistrée"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
