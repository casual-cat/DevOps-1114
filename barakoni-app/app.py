import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"

responses = {
    "correct": [
        "Correct! You actually got one right.",
        "Amazing, even a stopped clock is right twice a day.",
        "Correct! I'm... mildly impressed.",
    ],
    "wrong": [
        "Wrong! Did you even try?",
        "Nope, that’s not it. Try again.",
        "You couldn't be more wrong if you tried.",
    ],
    "time_up": [
        "Too slow! Time waits for no one, especially not you.",
        "Time’s up! Better luck next time.",
        "You missed it. Was it that hard?",
        "Tick-tock, genius. You failed."
    ]
}

conversation = {
    "start": {
        "text": "another imbecile... you think I don't suffer enough with Avitar?",
        "choices": ["Who are you?", "Tell me a joke!", "What do you think of humans?", "Start Trivia Game"],
        "image": "/static/images/barakoni_default.png",
        "mood": ""
    },
    "Who are you?": {
        "text": "an alien in your stupid planet.",
        "choices": ["Go back"],
        "image": "/static/images/barakoni_human.png",
        "mood": "rotate"
    },
    "Tell me a joke!": {
        "text": "Knock knock...",
        "choices": ["Who's there?"],
        "image": "/static/images/barakoni_funny.png",
        "mood": "bounce"
    },
    "Start Trivia Game": {
        "text": "Welcome to Barakoni Trivia! Let's see if you're smarter than a potato.",
        "choices": ["Begin Trivia"],
        "image": "/static/images/barakoni_default.png",
        "mood": ""
    },
    # Trivia logic
    "Begin Trivia": {
        "text": "Question 1: What’s the fastest programming language? (Hint: It's not yours.)",
        "choices": ["Python", "Assembly", "JavaScript"],
        "image": "/static/images/barakoni_stare.png",
        "mood": "shake"
    },
    "Python": {
        "text": random.choice(responses["wrong"]),
        "choices": ["Try again (Q1)"],
        "image": "/static/images/barakoni_funny.png",
        "mood": "bounce",
        "correct": False
    },
    "Assembly": {
        "text": random.choice(responses["correct"]),
        "choices": ["Next question"],
        "image": "/static/images/barakoni_human.png",
        "mood": "rotate",
        "correct": True
    },
    "JavaScript": {
        "text": random.choice(responses["wrong"]),
        "choices": ["Try again (Q1)"],
        "image": "/static/images/barakoni_funny.png",
        "mood": "shake",
        "correct": False
    },
    "Try again (Q1)": {
        "text": "Question 1: What’s the fastest programming language? (Hint: It's not yours.)",
        "choices": ["Python", "Assembly", "JavaScript"],
        "image": "/static/images/barakoni_stare.png",
        "mood": "shake"
    },
    "Next question": {
        "text": "Question 2: Why do startups fail?",
        "choices": ["Bad product", "Poor leadership", "No money"],
        "image": "/static/images/barakoni_default.png",
        "mood": ""
    },
    "Bad product": {
        "text": random.choice(responses["correct"]),
        "choices": ["Finish Trivia"],
        "image": "/static/images/barakoni_human.png",
        "mood": "shake",
        "correct": True
    },
    "Poor leadership": {
        "text": random.choice(responses["wrong"]),
        "choices": ["Try again (Q2)"],
        "image": "/static/images/barakoni_stare.png",
        "mood": "shake",
        "correct": False
    },
    "No money": {
        "text": random.choice(responses["wrong"]),
        "choices": ["Try again (Q2)"],
        "image": "/static/images/barakoni_funny.png",
        "mood": "bounce",
        "correct": False
    },
    "Try again (Q2)": {
        "text": "Question 2: Why do startups fail?",
        "choices": ["Bad product", "Poor leadership", "No money"],
        "image": "/static/images/barakoni_default.png",
        "mood": ""
    },
    "Timeout": {
        "text": random.choice(responses["time_up"]),
        "choices": ["Try again"],
        "image": "/static/images/barakoni_funny.png",
        "mood": ""
    },
    "Finish Trivia": {
        "text": "Trivia completed! Your final score will reset for the next session.",
        "choices": ["Back to Menu"],
        "image": "/static/images/barakoni_funny.png",
        "mood": "",
        "isTriviaEnd": True
    }
}

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
    option = data.get("option", None)
    response = conversation.get(option, conversation["start"])
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
