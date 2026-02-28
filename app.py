from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

USERS = {}  # demo login memory

LESSONS = {
    "lesson1": "📘 AI matlab machine ko smart banana, jaise mobile ka face lock.",
    "lesson2": "📱 AI Maps, YouTube, Camera, Instagram me use hota hai.",
    "lesson3": "🤖 ChatGPT ka use learning aur content ke liye hota hai.",
    "lesson4": "💰 AI se freelancing aur automation se earning hoti hai.",
    "lesson5": "🚀 AI future ka skill hai. AI Engineer ban sakte ho."
}

QUIZ = {
    "lesson1": {
        "q": "AI ka simple matlab kya hai?",
        "options": ["Machine ko smart banana", "Internet", "Mobile", "Game"],
        "answer": 0
    },
    "lesson2": {
        "q": "AI ka use kaha hota hai?",
        "options": ["Maps", "YouTube", "Camera", "All"],
        "answer": 3
    }
}

@app.route("/")
def home():
    return "AI YAAR FREE DEMO Backend is LIVE 🚀"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    name = data.get("name")
    USERS[name] = {"progress": []}
    return jsonify({"msg": f"Welcome {name} 👋"})

@app.route("/lesson", methods=["POST"])
def lesson():
    data = request.json
    lesson = data.get("lesson")
    user = data.get("user")

    if lesson in ["lesson4", "lesson5"]:
        return jsonify({"locked": True, "msg": "🔒 Pro course hai. Upgrade karo!"})

    USERS[user]["progress"].append(lesson)
    return jsonify({"content": LESSONS.get(lesson)})

@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.json
    lesson = data.get("lesson")
    return jsonify(QUIZ.get(lesson))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
