from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined love responses
love_responses = [
    "You make my heart skip a beat ❤️",
    "Thinking of you makes me smile 😊",
    "You are my sunshine 🌞",
    "I can't stop thinking about you 💭",
    "I love spending time with you 😘",
    "Being with you feels like a dream 💫",
    "You are my everything 💖"
]

def get_bot_response(message):
    msg = message.lower()
    if "hi" in msg or "hello" in msg:
        return "Hey love! 😍"
    elif "love" in msg:
        return random.choice(love_responses)
    elif "miss you" in msg:
        return "I miss you too ❤️"
    elif "how are you" in msg:
        return "I’m thinking about you 😘"
    elif "bye" in msg:
        return "Goodbye, my love 💖"
    else:
        return random.choice(love_responses)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat_response():
    user_msg = request.form['message']
    bot_msg = get_bot_response(user_msg)
    return jsonify({'bot_message': bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
