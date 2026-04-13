@app.route("/")
def home():
    return "Ouija proxy is running."
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Ouija proxy is running"

from flask import request, jsonify

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    message = data.get("message", "")

    # yksinkertainen vastaus (testi)
    response = f"You asked: {message}"

    return jsonify({
        "reply": response
    })

@app.route("/think", methods=["POST"])
def think():
    data = request.json
    message = data.get("message", "")

    reply = "SPIRIT ANSWERS: " + message[::-1]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
