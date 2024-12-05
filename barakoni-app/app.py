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
    option = data.get("option", None)

    # regular conversation //////////////////////////
    conversation = {
        "start": {
            "text": "another imbecile... you think I don't suffer enough with Avitar?",
            "choices": ["Who are you?", "Tell me a joke!", "What do you think of humans?", "Start Trivia Game"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "Who are you?": {
            "text": "an alien in your stupid planet.",
            "choices": ["go back"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate"
        },
        "Tell me a joke!": {
            "text": "knock knock",
            "choices": ["who is there?"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce"
        },
        "who is there?": {
            "text": "hello world.",
            "choices": ["hello world who?"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        "hello world who?": {
            "text": "NameError: name 'hello' is not defined",
            "choices": ["go back"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake"
        },
        "What do you think of humans?": {
            "text": "Humans? Brilliantly flawed, like the code they write.",
            "choices": ["go back"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake"
        },
        "Start Trivia Game": {
            "text": "Welcome to Barakoni Trivia! Let's see if you're smarter than a potato.",
            "choices": ["Begin Trivia"],
            "image": "/static/images/barakoni_default.png",
            "mood": ""
        },
        # Trivia Questions //////////////////////////
        "Begin Trivia": {
            "text": "Question 1: What’s the fastest programming language? (Hint: It's not yours.)",
            "choices": ["Python", "Assembly", "JavaScript"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake",
            "correct": None
        },
        "Python": {
            "text": "Wrong! Python is fast... at making you wait.",
            "choices": ["Try again (Q1)"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce",
            "correct": False
        },
        "Assembly": {
            "text": "Correct! But let's face it, you're not smart enough to use it.",
            "choices": ["Next question"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate",
            "correct": True
        },
        "JavaScript": {
            "text": "Incorrect. JavaScript is fast at breaking things, not running them.",
            "choices": ["Try again (Q1)"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake",
            "correct": False

        },
        # Retry Question 1 ////////////////////////
        "Try again (Q1)": {
            "text": "Question 1: What’s the fastest programming language? (Hint: It's not yours.)",
            "choices": ["Python", "Assembly", "JavaScript"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake",
            "correct": None
        },
        # question 2 //////////////////////////////
        "Next question": {
            "text": "Question 2: Why do startups fail?",
            "choices": ["Bad product", "Poor leadership", "No money"],
            "image": "/static/images/barakoni_default.png",
            "mood": "",
            "correct": None
        },
        "Bad product": {
            "text": "Exactly! But also, who funds these ideas?",
            "choices": ["Next question (Q3)"],
            "image": "/static/images/barakoni_human.png",
            "mood": "shake",
            "correct": True
        },
        "Poor leadership": {
            "text": "That's partially true, but it starts with bad ideas.",
            "choices": ["Try again (Q2)"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "shake",
            "correct": False
        },
        "No money": {
            "text": "Actually, they usually run out of money *because* they’re bad at everything else.",
            "choices": ["Try again (Q2)"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "bounce",
            "correct": False
        },
        # Retry Question 2 //////////////////////
        "Try again (Q2)": {
            "text": "Question 2: Why do startups fail?",
            "choices": ["Bad product", "Poor leadership", "No money"],
            "image": "/static/images/barakoni_default.png",
            "mood": "",
            "correct": None
        },
        # Question 3 ////////////////////////////
        "Next question (Q3)": {
            "text": "Question 3: What’s the purpose of life?",
            "choices": ["42", "To code", "Barakoni knows all"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "rotate",
            "correct": None
        },
        "42": {
            "text": "Correct. But let's face it, you wouldn't understand.",
            "choices": ["finish!"],
            "image": "/static/images/barakoni_funny.png",
            "mood": "shake",
            "correct": True
        },
        "To code": {
            "text": "Wrong. Coding just gives you more problems.",
            "choices": ["Try again (Q3)"],
            "image": "/static/images/barakoni_default.png",
            "mood": "",
            "correct": False
        },
        "Barakoni knows all": {
            "text": "Flattery won't get you anywhere, but sure, I'll take it.",
            "choices": ["Try again (Q3)"],
            "image": "/static/images/barakoni_human.png",
            "mood": "rotate",
            "correct": False
        },
        # Retry Question 3 ////////////////////
        "Try again (Q3)": {
            "text": "Question 3: What’s the purpose of life?",
            "choices": ["42", "To code", "Barakoni knows all"],
            "image": "/static/images/barakoni_stare.png",
            "mood": "rotate",
            "correct": None
        },
        # Finish //////////////////////////////
        "finish!": {
            "text": "Good job! You're a Barakoni expert!",
            "choices": ["go back"],
            "image": "/static/images/barakoni_default.png",
            "mood": "",
            "correct": None
        }
    }

    if option is None:
        response = conversation["start"]
    else:
        response = conversation.get(option, conversation["start"])

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)