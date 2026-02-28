from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def ai_yaar_reply(message, language):
    msg = message.lower()

    lessons = {
        "lesson1": {
            "Hindi": "📘 AI matlab machine ko smart banana, jaise mobile ka face lock ya Google suggestions.",
            "Marathi": "📘 AI म्हणजे मशीनला स्मार्ट बनवणं, जसं मोबाईलचा फेस लॉक.",
            "English": "📘 AI means making machines smart, like phone face unlock."
        },
        "lesson2": {
            "Hindi": "📱 AI Maps, YouTube, Camera, Instagram jaise apps me use hota hai.",
            "Marathi": "📱 AI Maps, YouTube, Camera, Instagram मध्ये वापरला जातो.",
            "English": "📱 AI is used in Maps, YouTube, Camera, Instagram."
        },
        "lesson3": {
            "Hindi": "🤖 ChatGPT ka use learning, content aur planning ke liye hota hai.",
            "Marathi": "🤖 ChatGPT चा वापर शिकण्यासाठी आणि कंटेंटसाठी होतो.",
            "English": "🤖 ChatGPT is used for learning and content."
        },
        "lesson4": {
            "Hindi": "💰 AI se freelancing, content creation aur automation se earning hoti hai.",
            "Marathi": "💰 AI वापरून freelancing आणि automation मधून कमाई होते.",
            "English": "💰 AI helps earn via freelancing and automation."
        },
        "lesson5": {
            "Hindi": "🚀 AI future ka skill hai. AI Engineer aur Prompt Expert ban sakte ho.",
            "Marathi": "🚀 AI हे future skill आहे. AI Engineer होता येतं.",
            "English": "🚀 AI is a future skill. You can become an AI Engineer."
        }
    }

    if msg in lessons:
        return lessons[msg].get(language, lessons[msg]["Hindi"])

    if "ai kya" in msg or "what is ai" in msg:
        return lessons["lesson1"].get(language)

    return "😊 Main AI Yaar hoon. Neeche lesson buttons dabao ya AI se related sawal poochho."

@app.route("/")
def home():
    return "AI YAAR FREE DEMO Backend is LIVE 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    message = data.get("message", "")
    language = data.get("language", "Hindi")
    reply = ai_yaar_reply(message, language)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
