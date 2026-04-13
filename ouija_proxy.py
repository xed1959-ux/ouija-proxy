from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# 🔑 Lisää oma API-avain Renderiin environment variableen:
# OPENAI_API_KEY
client = OpenAI()

# -------------------------
# ROOT
# -------------------------
@app.route("/")
def home():
    return "Ouija proxy is running (AI spirit active)"

# -------------------------
# ASK (REAL AI SPIRIT)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    message = data.get("message", "")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an ancient mysterious ouija board spirit. "
                        "You answer briefly, cryptically, and slightly eerie. "
                        "Never be too long. Speak like a spirit."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = response.choices[0].message.content.strip()

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "THE SPIRIT IS SILENT..."}), 500

# -------------------------
# THINK (TEST ENDPOINT)
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}
    message = data.get("message", "")

    reply = "SPIRIT ANSWERS: " + message[::-1]

    return jsonify({"reply": reply})

# -------------------------
# LOCAL RUN ONLY
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
