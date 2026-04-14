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

    data = request.get_json() or {}
    message = data.get("message", "")

    try:
        print("ABOUT TO CALL OPENAI")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a mysterious ouija board spirit. Answer briefly and eerily."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = completion.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        print("OPENAI ERROR:", str(e))
        return jsonify({
            "reply": "THE SPIRIT IS SILENT..."
        })

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
