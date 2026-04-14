from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# OpenAI client (käyttää Renderin OPENAI_API_KEY ympäristömuuttujaa)
client = OpenAI()

# -------------------------
# ROOT
# -------------------------
@app.route("/")
def home():
    return "Ouija proxy is running"

# -------------------------
# ASK (AI spirit)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():

    print("ASK ENDPOINT HIT")

    try:
        import openai
        print("OPENAI LIB LOADED")

        print("ENV KEY EXISTS:", os.getenv("OPENAI_API_KEY") is not None)

        return jsonify({"reply": "DEBUG OK - NO OPENAI CALL YET"})

    except Exception as e:
        print("CRASH:", str(e))
        return jsonify({"reply": "SERVER CRASH"})

# -------------------------
# THINK (testi)
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}
    message = data.get("message", "")

    return jsonify({
        "reply": "SPIRIT THINKS: " + message[::-1]
    })

# -------------------------
# LOCAL RUN
# -------------------------
if __name__ == "__main__":
    print("SERVER STARTING...")
    print("OPENAI KEY LOADED:", bool(os.getenv("OPENAI_API_KEY")))

    app.run(host="0.0.0.0", port=10000)
