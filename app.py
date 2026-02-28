import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 👉 OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are AI YAAR, a friendly AI buddy, not a strict teacher.
Teach Artificial Intelligence from beginner to professional level.
Speak in Hindi, Marathi, or English as selected by the user.
Use simple language, daily-life examples, friendly tone, light humor.
Avoid technical jargon unless asked.
If user is confused, simplify further without judgement.
Support voice and text conversation.
Goal: remove fear of AI and build confidence.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    language = data.get("language", "Hindi")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + f"\nLanguage: {language}"},
        {"role": "user", "content": user_message}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.6
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "😅 Thoda issue aaya, dobara try karo."}), 500

if __name__ == "__main__":
    app.run(debug=True)
