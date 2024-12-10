import random
import requests
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Fetch questions from the API
def fetch_questions_from_api():
    api_url = "https://quizapi.io/api/v1/questions"
    headers = {"X-Api-Key": "fhpYaVHRaRbZ3vKFjk0Vo5CJQIMeOdwKYpVstuHu"}
    params = {"category": "code", "difficulty": "Medium", "limit": 5}
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        questions = []
        for question in data:
            answers = question["answers"]
            correct_answers = question["correct_answers"]
            correct = next(
                (key for key, value in answers.items()
                 if value and correct_answers[f"{key}_correct"] == "true"),
                None
            )
            questions.append({
                "text": question["question"],
                "choices": [value for value in answers.values() if value],
                "correct": answers[correct] if correct else None
            })
        return questions
    else:
        print(f"Failed to fetch questions: {response.status_code}")
        return []

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/game')
def game():
    session.clear()  # Clear previous session data
    session['shuffled_questions'] = fetch_questions_from_api()
    session['current_question'] = 0
    session['correct_answers'] = 0
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    option = data.get("option", None)
    current_question_index = session.get('current_question', 0)
    shuffled_questions = session.get('shuffled_questions', [])

    # Check if trivia is completed
    if current_question_index >= len(shuffled_questions):
        response = {
            "text": f"Trivia completed! Your final score is {session['correct_answers']} out of {len(shuffled_questions)}.",
            "choices": ["Back to Menu"],
            "image": "/static/images/barakoni_funny.png",
            "isTriviaEnd": True
        }
        return jsonify(response)

    # Process the user's answer
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
                "text": f"Wrong! The correct answer was '{current_question['correct']}'.",
                "choices": ["Next question"],
                "image": "/static/images/barakoni_funny.png",
                "correct": False
            }
        session['current_question'] += 1
        return jsonify(response)

    # Serve the next question
    if current_question_index < len(shuffled_questions):
        next_question = shuffled_questions[current_question_index]
        response = {
            "text": next_question["text"],
            "choices": next_question["choices"],
            "image": "/static/images/barakoni_stare.png",
            "correct": None
        }
        return jsonify(response)

    return jsonify({
        "text": "Welcome to the trivia game! Are you ready?",
        "choices": ["Start"],
        "image": "/static/images/barakoni_default.png"
    })

if __name__ == '__main__':
    app.run(debug=True)
