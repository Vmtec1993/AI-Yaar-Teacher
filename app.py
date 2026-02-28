from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🧠 FREE DEMO KNOWLEDGE BASE
def ai_yaar_reply(message, language):
    msg = message.lower()

    if "ai kya" in msg or "what is ai" in msg:
        if language == "Marathi":
            return "😄 सोप्या शब्दात सांगायचं तर, AI म्हणजे मशीनला माणसासारखं स्मार्ट बनवणं. उदा: मोबाईलचा फेस लॉक."
        elif language == "English":
            return "😄 Simply put, AI means making machines smart like humans, such as phone face unlock."
        else:
            return "😄 Simple bolu? AI matlab machine ko insaan jaisa smart banana, jaise mobile ka face lock."

    if "use" in msg or "kaise" in msg:
        return "AI ka use learning, business, content writing aur automation mein hota hai 👍"

    if "career" in msg or "future" in msg:
        return "AI future ka skill hai 🚀 AI Engineer, Prompt Expert, AI Business jaise roles hote hain."

    return "😊 Main AI Yaar hoon. AI seekhne ke liye kuch bhi poochho, main simple language mein samjhaunga."

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
