from flask import Flask, request, jsonify
from openai import OpenAI 
import os

app = Flask(__name__)

client = OpenAI(api_key=os. environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are MANISH.AI, a powerful AI assistant created by Manish.
You speak Hindi and English naturally.
You help everyone smartly.
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)