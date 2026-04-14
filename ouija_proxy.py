from flask import Flask, request, jsonify
from openai import OpenAI
import os
import traceback

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
# ASK ENDPOINT (SAFE MODE)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    try:
        # SAFE JSON PARSE (ei kaadu ikinä HTML-erroriin)
        data = request.get_json(force=True, silent=True)

        if not data:
            print("⚠️ NO JSON RECEIVED")
            return jsonify({"reply": "NO JSON RECEIVED"}), 400

        message = data.get("message", "")
        print("🧠 USER MESSAGE:", message)
        print("ABOUT TO CALL OPENAI")

        # OpenAI CALL
        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                input=f"You are a mysterious Ouija board spirit. Be short, eerie and cryptic.\nUser: {message}"
            )

            reply = response.output_text

            print("✅ OPENAI SUCCESS")
            print("🪬 REPLY:", reply)

            return jsonify({"reply": reply})

        except Exception as openai_error:
            print("🔥 OPENAI FAILED:")
            print(repr(openai_error))
            print(traceback.format_exc())

            return jsonify({
                "reply": "OPENAI ERROR",
                "detail": str(openai_error)
            }), 500

    except Exception as e:
        print("💀 FATAL ERROR:")
        print(repr(e))
        print(traceback.format_exc())

        return jsonify({
            "reply": "FATAL ERROR",
            "detail": str(e)
        }), 500


# -------------------------
# THINK (TEST ENDPOINT)
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
