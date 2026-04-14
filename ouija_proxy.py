from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# -------------------------
# OpenAI client (IMPORTANT: no api_key= here)
# Render reads OPENAI_API_KEY automatically
# -------------------------
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

    print("👻 ASK ENDPOINT HIT")

    data = request.get_json() or {}
    message = data.get("message", "")

    print("📩 MESSAGE:", message)
    print("🔑 KEY EXISTS:", os.getenv("OPENAI_API_KEY") is not None)

    if not message:
        return jsonify({"reply": "..."})

    try:
        print("⚡ CALLING OPENAI...")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a mysterious ouija board spirit. "
                        "Answer briefly, cryptically, and eerily."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = completion.choices[0].message.content.strip()

        print("✅ OPENAI RESPONSE OK")
        print("🧿 REPLY:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 OPENAI FAILED:", repr(e))
        return jsonify({"reply": "THE SPIRIT IS SILENT..."})

# -------------------------
# THINK (TEST)
# -------------------------
@app.route("/think", methods=["POST"])
def think():

    data = request.get_json() or {}
    message = data.get("message", "")

    return jsonify({
        "reply": "SPIRIT THINKS: " + message[::-1]
    })

# -------------------------
# LOCAL RUN ONLY
# -------------------------
if __name__ == "__main__":

    print("🚀 SERVER STARTING...")
    print("🔑 OPENAI KEY LOADED:", bool(os.getenv("OPENAI_API_KEY")))

    app.run(host="0.0.0.0", port=10000)
