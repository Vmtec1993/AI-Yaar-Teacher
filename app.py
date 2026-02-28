from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def ai_yaar_reply(message, language):
    msg = message.lower()

    lessons = {
        "lesson1": {
            "Hindi": "📘 AI matlab machine ko smart banana, jaise mobile ka face lock ya Google suggestions.",
            "Marathi": "📘 AI म्हणजे मशीनला स्मार्ट बनवणं, जसं मोबाईलचा फेस लॉक किंवा Google.",
            "English": "📘 AI means making machines smart, like phone face unlock or Google suggestions."
        },
        "lesson2": {
            "Hindi": "📱 AI daily life me Maps, YouTube, Camera, Instagram jaise apps me use hota hai.",
            "Marathi": "📱 AI रोजच्या जीवनात Maps, YouTube, Camera, Instagram मध्ये वापरला जातो.",
            "English": "📱 AI is used in Maps, YouTube, Camera, Instagram in daily life."
        },
        "lesson3": {
            "Hindi": "🤖 ChatGPT ka use learning, content writing, planning aur business me hota hai.",
            "Marathi": "🤖 ChatGPT चा वापर शिकणे, कंटेंट आणि बिझनेससाठी होतो.",
            "English": "🤖 ChatGPT is used for learning, content writing, planning and business."
        },
        "lesson4": {
            "Hindi": "💰 AI se freelancing, content creation aur automation ke through earning hoti hai.",
            "Marathi": "💰 AI वापरून freelancing आणि automation मधून कमाई होते.",
            "English": "💰 AI helps earn via freelancing, content creation and automation."
        },
        "lesson5": {
            "Hindi": "🚀 AI future ka skill hai. AI Engineer, Prompt Expert jaise careers hote hain.",
            "Marathi": "🚀 AI हे future skill आहे. AI Engineer, Prompt Expert असे career असतात.",
            "English": "🚀 AI is a future skill. Careers include AI Engineer and Prompt Expert."
        }
    }

    if msg in lessons:
        return lessons[msg].get(language, lessons[msg]["Hindi"])

    if "ai kya" in msg or "what is ai" in msg:
        return lessons["lesson1"].get(language)

    return "😊 Main AI Yaar hoon. Lesson buttons dabao ya AI se related kuch bhi poochho."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    language = data.get("language", "Hindi")
    reply = ai_yaar_reply(message, language)
    return jsonify({"reply": reply})

@app.route("/")
def home():
    return "AI YAAR FREE DEMO Backend is LIVE 🚀"

if __name__ == "__main__":
    app.run()
