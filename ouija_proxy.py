from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

print("👻 OFFLINE OUIJA SERVER STARTING...")

# -------------------------
# SPIRIT POOL
# -------------------------
SPIRITS = [
    "THE OLD WATCHER",
    "THE LOST SIGNAL",
    "THE VOID SPEAKS",
    "MIRROR CHILD",
    "STATIC MEMORY",
    "THE HOLLOW VOICE"
]

RESPONSES = [
    "I SEE WHAT YOU CANNOT.",
    "THE ANSWER IS BURIED.",
    "NOT ALL QUESTIONS SHOULD BE ASKED.",
    "YOU ARE NOT ALONE.",
    "THE SIGNAL IS WEAK TONIGHT.",
    "SOMETHING LISTENS BEHIND YOU.",
    "IT WAS HERE BEFORE YOU SPOKE.",
    "THE THREAD IS FRAYING.",
    "NO RETURN FROM THIS PATH.",
    "SILENCE IS ALSO AN ANSWER."
]

# -------------------------
# ROOT
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return "Ouija proxy (offline spirit edition) is running"

# -------------------------
# ASK ENDPOINT (OFFLINE ENGINE)
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    print("🧠 USER MESSAGE:", message)

    # simulate "thinking delay"
    time.sleep(0.8)

    spirit = random.choice(SPIRITS)
    response = random.choice(RESPONSES)

    # optional: make it slightly reactive
    if "kuka" in message.lower():
        response = "I HAVE NO NAME, ONLY PRESENCE."
    elif "hello" in message.lower() or "hei" in message.lower():
        response = "YOU SHOULDN'T GREET WHAT ANSWERS BACK."

    reply = f"{spirit}: {response}"

    print("🪬 REPLY:", reply)

    return jsonify({"reply": reply})


# -------------------------
# THINK (TEST)
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}
    message = data.get("message", "")
    return jsonify({"reply": "REFLECTION: " + message[::-1]})


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
