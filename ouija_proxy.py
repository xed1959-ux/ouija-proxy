from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------
# ROOT (TESTI ETUSIVU)
# -------------------------
@app.route("/")
def home():
    return "Ouija proxy is running"

# -------------------------
# ASK (AI / CHAT ENDPOINT)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}

    message = data.get("message", "")

    import random

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
# THINK (TESTILEIKKI)
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
# LOCAL RUN (Render ei käytä tätä)
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
