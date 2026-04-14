from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

print("🚀 SERVER STARTING...")

# -------------------------
# OPENAI CLIENT
# -------------------------
api_key = os.getenv("OPENAI_API_KEY")

print("🔑 OPENAI KEY LOADED:", bool(api_key))

client = OpenAI(api_key=api_key)

# -------------------------
# ROOT
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return "Ouija proxy is running"

# -------------------------
# ASK ENDPOINT
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    try:
        data = request.get_json() or {}
        message = data.get("message", "")

        print("🧠 USER MESSAGE:", message)
        print("ABOUT TO CALL OPENAI")

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "You are a mysterious Ouija board spirit. Answer briefly, slightly eerie, but helpful."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = response.output_text

        print("✅ OPENAI RESPONSE OK")

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 OPENAI FAILED:", repr(e))
        return jsonify({"reply": "THE SPIRIT IS SILENT..."})


# -------------------------
# THINK (test endpoint)
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}
    message = data.get("message", "")
    return jsonify({"reply": "SPIRIT MIRRORS: " + message[::-1]})


# -------------------------
# RUN (LOCAL ONLY)
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
