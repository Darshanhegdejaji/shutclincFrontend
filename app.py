from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "https://4958-119-161-98-68.ngrok-free.app/webhooks/rest/webhook"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})

    bot_message = response.json()[0]["text"] if response.json() else "Sorry, no response from the bot."
    return jsonify({"bot_message": bot_message})


if __name__ == "__main__":
    app.run(debug=True)
