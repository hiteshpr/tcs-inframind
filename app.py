from flask import Flask, request, render_template
from flask_cors import CORS
app = Flask(__name__)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    
    password = request.form['password']
    userId = request.form['userId']
    name = request.form['name']
    age = request.form['age']
    favSports = request.form['favSports']
    gender = request.form['gender']

    print(password, userId, name, age, favSports, gender)

    return "hello world!"

if __name__ == '__main__':
    app.run()