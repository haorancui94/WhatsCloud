from flask import Flask
from flask import send_file, request
from flask import render_template
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return send_file('./templates/index.html')


@app.route('/predict', methods=['POST'])
def predict():
    sequence = '"'+"["+request.form["abc"]+"]"+'"'
    print(sequence)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
