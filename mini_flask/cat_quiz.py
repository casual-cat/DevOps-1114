from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What is your favorite time of day?", "options": ["morning", "afternoon", "evening", "night"]},
    {"question": "What is your favorite food?", "options": ["Chicken", "Fish", "Pasta", "Sushi"]},
    {"question": "What is your favorite color?", "options": ["Black", "Pink", "Red", "Blue"]},
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answers = [request.form.get(f"question{i}") for i in range(len(questions))]
        cat_type = calculate_cat_type(answers) 
        return render_template('result.html', cat_type=cat_type)
    return render_template('quiz.html', questions=questions)

def calculate_cat_type(answers):
    cat_scores = {
        "Siamese Cat!": 0,
        "Exotic Shorthair!": 0,
        "Persian Cat!": 0,
        "Bengal Cat!": 0,
        "Domestic Shorthair!": 0
    }
    
    for answer in answers:
        if answer == "morning":
            cat_scores["Siamese Cat!"] += 1
        if answer == "night":
            cat_scores["Exotic Shorthair!"] += 1
        if answer == "evening":
            cat_scores["Persian Cat!"] += 1
        if answer == "afternoon":
            cat_scores["Bengal Cat!"] += 1

        if answer == "Fish":
            cat_scores["Siamese Cat!"] += 1
        if answer == "Chicken":
            cat_scores["Exotic Shorthair!"] += 1
        if answer == "Sushi":
            cat_scores["Persian Cat!"] += 1
        if answer == "Pasta":
            cat_scores["Bengal Cat!"] += 1

        if answer == "Blue":
            cat_scores["Siamese Cat!"] += 1
        if answer == "Black":
            cat_scores["Exotic Shorthair!"] += 1
        if answer == "Pink":
            cat_scores["Persian Cat!"] += 1
        if answer == "Red":
            cat_scores["Bengal Cat!"] += 1

    selected_cat = max(cat_scores, key=cat_scores.get)

    if selected_cat == "Siamese Cat!":
        return {"type": "Siamese Cat!", 
                "description": "You are curious and love peaceful vibes!! :)", 
                "image": "static/siamese.gif"}
    elif selected_cat == "Exotic Shorthair!":
        return {"type": "Exotic Shorthair!", 
                "description": "You are a night owl and love to sleep!! :)", 
                "image": "static/exotic_shorthair.gif"}
    elif selected_cat == "Persian Cat!":
        return {"type": "Persian Cat!", 
                "description": "You are calm and enjoy the finer things in life!! :)", 
                "image": "static/persian.gif"}
    elif selected_cat == "Bengal Cat!":
        return {"type": "Bengal Cat!", 
                "description": "You are energetic and love to party!! :)", 
                "image": "static/bengal.gif"}
    else:
        return {"type": "Domestic Shorthair!", 
                "description": "You are friendly and love to cuddle!! :)", 
                "image": "static/domestic_shorthair.gif"}

# def calculate_cat_type(answers):
#     if "morning" in answers and "Fish" in answers and "Blue" in answers:
#         return {"type": "Siamese Cat!", 
#                 "description": "You are curious and love peaceful vibes!! :)", 
#                 "image": "static/siamese.gif"}
#     elif "night" in answers and "Chicken" in answers and "Black" in answers:
#         return {"type": "Exotic Shorthair!", 
#                 "description": "You are a night owl and love to sleep!! :)", 
#                 "image": "static/exotic_shorthair.gif"}
#     elif "evening" in answers and "Sushi" in answers and "Pink" in answers:
#         return {"type": "Persian Cat!", 
#                 "description": "You are calm and enjoy the little things in life!! :)", 
#                 "image": "static/persian.gif"}
#     elif "afternoon" in answers and "Pasta" in answers and "Red" in answers:
#         return {"type": "Bengal Cat!", 
#                 "description": "You are energetic and love to party!! :)", 
#                 "image": "static/bengal.gif"}
#     else:
#         return {"type": "Domestic Shorthair!", 
#                 "description": "You are friendly and love to cuddle!! :)", 
#                 "image": "static/domestic_shorthair.gif"}
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)