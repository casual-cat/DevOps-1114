from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trivia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Integer)

def get_funny_trivia_questions():
    questions = [
        {
            "question": "What does CI/CD stand for?",
            "correct": "Continuous Integration/Continuous Deployment",
            "options": [
                "Continuous Integration/Continuous Deployment",
                "Commit Immediately/Code Daily",
                "Cannot Implement/Code Defunct",
                "Continuous Integration/Continuous Disruption"
            ],
            "image": "/static/images/barakoni_thinking.png"
        },
        {
            "question": "Which tool is primarily used for container orchestration?",
            "correct": "Kubernetes",
            "options": [
                "Kubernetes",
                "Docker",
                "Terraform",
                "Chef"
            ],
            "image": "/static/images/barakoni_smile.png"
        },
        {
            "question": "What does 'Infrastructure as Code' (IaC) aim to solve?",
            "correct": "Automating infrastructure provisioning",
            "options": [
                "Manual infrastructure setups",
                "Automating infrastructure provisioning",
                "Encrypting all traffic",
                "Rebooting servers hourly"
            ],
            "image": "/static/images/barakoni_surprised.png"
        }
    ]
    random.shuffle(questions)
    return questions[:10]

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/game')
def game():
    session['score'] = 0
    session['current_question'] = 0
    questions = get_funny_trivia_questions()
    session['questions'] = questions
    return render_template('game.html', question=questions[0], question_index=0, score=session['score'], image=questions[0]['image'])

@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    print("Received answer:", data)  # Debugging the payload
    print("Current session:", session)  # Debugging the session state

    question_index = session.get('current_question', 0)
    questions = session.get('questions', [])

    if question_index >= len(questions):
        return jsonify({"error": "No more questions!"})
    
    correct_answer = questions[question_index]['correct']
    user_answer = data.get('answer')
    correct = (user_answer == correct_answer)

    if correct:
        session['score'] += 10

    session['current_question'] += 1
    next_index = session['current_question']

    response = {
        "correct": correct,
        "correct_answer": correct_answer,
        "score": session['score'],
        "next_question": None
    }

    if next_index < len(questions):
        next_question = questions[next_index]
        response['next_question'] = {
            "question": next_question['question'],
            "options": next_question['options'],
            "image": next_question['image']
        }

    print("Response to frontend:", response)  # Debugging the response
    return jsonify(response)

@app.route('/highscores')
def highscores():
    scores = HighScore.query.order_by(HighScore.score.desc()).limit(10).all()
    return render_template('highscores.html', scores=scores)

@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.json
    name = data['name']
    score = session['score']
    high_score = HighScore(name=name, score=score)
    db.session.add(high_score)
    db.session.commit()
    return jsonify({"message": "Score saved!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
