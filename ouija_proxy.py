from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# -------------------------
# ROOT
# -------------------------
@app.route("/")
def home():
    return "Ouija proxy is running"

# -------------------------
# ASK (AI / spirit response)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}

    message = data.get("message", "")

    responses = [
        "I AM NOT WHAT YOU THINK.",
        "I WAS HERE BEFORE YOU.",
        "YOU SHOULD NOT ASK THAT.",
        "THE ANSWER IS UNCLEAR.",
        "YES",
        "NO"
    ]

    response = random.choice(responses)

    return jsonify({
        "reply": response
    })

# -------------------------
# THINK (optional test endpoint)
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}

    message = data.get("message", "")

    reply = "SPIRIT ANSWERS: " + message[::-1]

    return jsonify({
        "reply": reply
    })

# -------------------------
# LOCAL RUN ONLY
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
