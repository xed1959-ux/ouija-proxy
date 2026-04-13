from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/think", methods=["POST"])
def think():
    data = request.json
    message = data.get("message", "")

    reply = "SPIRIT ANSWERS: " + message[::-1]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
