import random
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# In-memory stats (for development)
player_stats = {
    "total_questions": 0,
    "correct_answers": 0,
    "fastest_time": None,  # Track fastest response time (in seconds)
    "accuracy": 0.0,  # Percentage of correct answers
}

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
    }
}

questions = [
    {
        "text": "What’s the fastest programming language? (Hint: It's not yours.)",
        "choices": ["Python", "Assembly", "JavaScript"],
        "correct": "Assembly"
    },
    {
        "text": "Why do startups fail?",
        "choices": ["Bad product", "Poor leadership", "No money"],
        "correct": "Bad product"
    },
    {
        "text": "What’s the meaning of life?",
        "choices": ["42", "To code", "Barakoni knows all"],
        "correct": "42"
    },
    {
        "text": "Which programming language is known for web development?",
        "choices": ["Ruby", "JavaScript", "C++"],
        "correct": "JavaScript"
    },
    {
        "text": "What is 2 + 2?",
        "choices": ["3", "4", "22"],
        "correct": "4"
    },
]

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/game')
def game():
    # Shuffle questions and reset session stats
    session['shuffled_questions'] = random.sample(questions, len(questions))
    session['current_question'] = 0
    session['correct_answers'] = 0
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    option = data.get("option", None)
    current_question_index = session.get('current_question', 0)
    shuffled_questions = session.get('shuffled_questions', [])
    
    # Check if the game should end
    if current_question_index >= len(shuffled_questions):
        response = {
            "text": "Trivia completed! Your final score is {} out of {}.".format(
                session.get('correct_answers', 0),
                len(shuffled_questions)
            ),
            "choices": ["Back to Menu"],
            "image": "/static/images/barakoni_funny.png",
            "isTriviaEnd": True
        }
        session.clear()  # Reset session
        return jsonify(response)
    
    # Handle correct or wrong answers
    if option and current_question_index < len(shuffled_questions):
        current_question = shuffled_questions[current_question_index]
        if option == current_question["correct"]:
            session['correct_answers'] += 1
            response = {
                "text": "Correct! Well done.",
                "choices": ["Next question"],
                "image": "/static/images/barakoni_human.png",
                "correct": True
            }
        else:
            response = {
                "text": "Wrong! The correct answer was '{}'.".format(current_question["correct"]),
                "choices": ["Try again", "Next question"],
                "image": "/static/images/barakoni_funny.png",
                "correct": False
            }
        return jsonify(response)

    # Serve the next question
    if current_question_index < len(shuffled_questions):
        next_question = shuffled_questions[current_question_index]
        session['current_question'] += 1
        response = {
            "text": next_question["text"],
            "choices": next_question["choices"],
            "image": "/static/images/barakoni_stare.png",
            "correct": None
        }
        return jsonify(response)

    # Default fallback
    return jsonify({
        "text": "Welcome to the trivia game! Are you ready?",
        "choices": ["Start"],
        "image": "/static/images/barakoni_default.png"
    })

if __name__ == '__main__':
    app.run(debug=True)