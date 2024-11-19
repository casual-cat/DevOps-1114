from flask import Flask

app = Flask(__name__) 

#HOME ROUTE
@app.route('/')
def home():
    return "Nah Uh"

@app.route('/greet/<name>')
def greeting(name):
    return f"hey, {name}!"

@app.route('/about')
def about():
    return "uhm what the sigma?"

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 5000, debug=True)

