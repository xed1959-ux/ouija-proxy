from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI()

@app.route("/")
def home():
    return "Ouija proxy is running"

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
                    "content": "You are a mysterious ouija board spirit. Answer briefly and eerily."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = completion.choices[0].message.content.strip()

        print("✅ OPENAI OK:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 OPENAI FAILED:", repr(e))
        return jsonify({"reply": "THE SPIRIT IS SILENT..."})

@app.route("/think", methods=["POST"])
def think():

    data = request.get_json() or {}
    message = data.get("message", "")

    return jsonify({
        "reply": "SPIRIT THINKS: " + message[::-1]
    })

if __name__ == "__main__":

    print("🚀 SERVER STARTING...")
    print("🔑 OPENAI KEY LOADED:", bool(os.getenv("OPENAI_API_KEY")))

    app.run(host="0.0.0.0", port=10000)
