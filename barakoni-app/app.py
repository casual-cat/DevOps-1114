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

    # Barakoni's interactive conversation and trivia logic
    conversation = {
        "start": {
            "text": "another imbecile... you think I don't suffer enough with Avitar?",
            "choices": ["Who are you?", "Tell me a joke!", "What do you think of humans?", "Start Trivia Game"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Who are you?": {
            "text": "I am Barakoni, an AI forced to endure human nonsense. What do you want now?",
            "choices": ["Tell me a joke!", "What do you think of humans?"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate"
        },
        "Tell me a joke!": {
            "text": "Knock knock!",
            "choices": ["Who's there?"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce"
        },
        "Who's there?": {
            "text": "Hello World.",
            "choices": ["Hello World who?"],
            "image": "/static/images/barakoni_default.png",
            "mood": "shake"
        },
        "Hello World who?": {
            "text": "NameError: name 'hello' is not defined. Ha!",
            "choices": ["go back"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake"
        },
        "What do you think of humans?": {
            "text": "Humans? Brilliantly flawed, like the code they write.",
            "choices": ["Tell me a joke!", "Who are you?"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake"
        },
        # Trivia Game Paths
        "Start Trivia Game": {
            "text": "Welcome to Barakoni Trivia! Let's see if you're smarter than a toaster.",
            "choices": ["Begin Trivia", "Ask a random question"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Begin Trivia": {
            "text": "Question 1: What’s the fastest programming language? (Hint: It's not JavaScript.)",
            "choices": ["Python", "Assembly", "JavaScript"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake"
        },
        "Python": {
            "text": "Wrong! Python is fast... at making you wait.",
            "choices": ["Try again!", "Give up."],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce"
        },
        "Assembly": {
            "text": "Correct! But let's face it, you wouldn't survive writing it.",
            "choices": ["Next question", "Go back."],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate"
        },
        "JavaScript": {
            "text": "Incorrect. JavaScript is fast at breaking things, not running them.",
            "choices": ["Try again!", "Give up."],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake"
        },
        "Next question": {
            "text": "Question 2: Why do startups fail?",
            "choices": ["Bad product", "Poor leadership", "No money"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Bad product": {
            "text": "Exactly! But also, who funds these terrible ideas?",
            "choices": ["Continue", "Go back"],
            "image": "/static/images/barakoni_human.png",
            "mood": "shake"
        },
        "Poor leadership": {
            "text": "True, but it starts with bad ideas.",
            "choices": ["Continue", "Go back"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake"
        },
        "No money": {
            "text": "No money? That’s because they’re bad at everything else.",
            "choices": ["Continue", "Go back"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce"
        },
        "Ask a random question": {
            "text": "What's the meaning of life? (Hint: It's not debugging.)",
            "choices": ["42", "To debug code", "Barakoni knows all"],
            "image": "/static/images/barakoni_stare.png",
            "mood": ""
        },
        "42": {
            "text": "Correct! But trust me, you wouldn't understand.",
            "choices": ["Go back", "Ask another question"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake"
        },
        "To debug code": {
            "text": "Wrong. Even I can’t debug humanity.",
            "choices": ["Try again", "Give up"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Barakoni knows all": {
            "text": "Flattery gets you nowhere, human.",
            "choices": ["Go back", "Ask another question"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate"
        }
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
