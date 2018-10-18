import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/predict"):
def predict():
    input_data = request.get_json()
    return jsonify({"status": 404, "message": "Model not found."})

if __name__ == "main":
    app.run(port=5000, debug=True)