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

    response = f"You asked: {message}"

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
