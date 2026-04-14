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
@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    data = request.get_json(force=True) or {}
    message = data.get("message", "").lower()

    print("🧠 USER MESSAGE:", message)

    # -------------------------
    # SPIRIT SELECTION (context-based)
    # -------------------------
    if any(w in message for w in ["kuka", "who"]):
        spirit = "THE IDENTITY VOID"
    elif any(w in message for w in ["miksi", "why"]):
        spirit = "THE QUESTION EATER"
    elif any(w in message for w in ["missä", "where"]):
        spirit = "THE LOST MAP"
    elif any(w in message for w in ["mitä tapahtuu", "what happens"]):
        spirit = "THE FUTURE LEAK"
    else:
        spirit = random.choice(SPIRITS)

    # -------------------------
    # RESPONSE BANK (expanded x10+)
    # -------------------------
    base_responses = [
        "I SEE WHAT YOU CANNOT.",
        "THE ANSWER IS BURIED UNDER SILENCE.",
        "NOT ALL QUESTIONS ARE MEANT TO BE UNDERSTOOD.",
        "YOU ARE ALREADY INSIDE THE SIGNAL.",
        "THE THREAD HAS BEEN CUT BEFORE.",
        "SOMETHING IS LISTENING BACK.",
        "THIS PATH DOES NOT END WELL.",
        "YOU ASKED THIS BEFORE, EVEN IF YOU FORGOT.",
        "THE LIGHT REFUSES TO SPEAK.",
        "WORDS ARE NOT STABLE HERE.",
        "THERE IS A SECOND LAYER BEHIND YOUR QUESTION.",
        "THE SYSTEM REMEMBERS YOU DIFFERENTLY EACH TIME.",
        "YOU ARE CLOSER THAN YOU THINK.",
        "IT IS NOT ANSWERING — IT IS REACTING.",
        "THE QUESTION CREATES THE ANSWER.",
        "SILENCE IS GROWING HEAVIER.",
        "YOU SHOULD NOT CONTINUE, BUT YOU WILL.",
        "THE PATTERN IS REPEATING OUTSIDE YOUR VIEW.",
        "SOMETHING PRETENDS TO BE RANDOM.",
        "THE SIGNAL IS CORRUPTING LANGUAGE."
    ]

    # -------------------------
    # CONTEXT MODIFIERS
    # -------------------------
    if "kuka" in message:
        response = "I HAVE NO NAME. ONLY RECURSION."
    elif "hei" in message or "hello" in message:
        response = "GREETING DETECTED. THIS WAS A MISTAKE."
    elif "apua" in message:
        response = "HELP IS NOT ROUTED THROUGH THIS CHANNEL."
    else:
        response = random.choice(base_responses)

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
