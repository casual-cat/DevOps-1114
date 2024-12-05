from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class Design(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer, default=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dress-up')
def dress_up():
    return render_template('dress_up.html')

@app.route('/gallery')
def gallery():
    designs = Design.query.order_by(Design.votes.desc()).all()
    return render_template('gallery.html', designs=designs)

@app.route('/vote/<int:design_id>', methods=['POST'])
def vote(design_id):
    design = Design.query.get_or_404(design_id)
    design.votes += 1
    db.session.commit()
    return redirect(url_for('gallery'))

if __name__ == '__main__':
    db.create_all()  
    app.run(debug=True)
