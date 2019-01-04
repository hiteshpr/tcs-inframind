from flask import Flask, request, render_template
from flask_cors import CORS
app = Flask(__name__)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    print(request.form)
    """ text = request.form['text']
    print(text) """
    """ processed_text = text.upper()
    return processed_text """

if __name__ == '__main__':
    app.run()