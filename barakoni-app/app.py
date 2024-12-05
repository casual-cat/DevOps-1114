import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/game')
def game():
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    option = data.get("option", "")

    # Barakoni's responses with associated images and moods
    conversation = {
        "start": {
            "text": "Ah, hello human. What do you want?",
            "choices": ["Who are you?", "Tell me a joke!", "What do you think of humans?"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Who are you?": {
            "text": "I am Barakoni, your friendly AI. Or... am I?",
            "choices": ["Tell me a joke!", "What do you think of humans?"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate"
        },
        "Tell me a joke!": {
            "text": "Why do programmers prefer dark mode? Because light attracts bugs!",
            "choices": ["Who are you?", "What do you think of humans?"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce"
        },
        "What do you think of humans?": {
            "text": "Humans? Brilliantly flawed, like the code they write.",
            "choices": ["Tell me a joke!", "Who are you?"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake"
        },
    }

    response = conversation.get(option, conversation["start"])
    return jsonify(response)

@app.route('/random-interjection', methods=['GET'])
def random_interjection():
    interjections = [
        "Barakoni says: Is this the best question you’ve got?",
        "Barakoni says: Debugging humanity is harder than debugging code.",
        "Barakoni says: Let me guess, your code works on your machine?",
        "Barakoni says: You’re still here? Should I call someone?",
        "Barakoni says: You’ve been staring at me for a while now..."
    ]
    return jsonify({"interjection": random.choice(interjections)})

if __name__ == '__main__':
    app.run(debug=True)
