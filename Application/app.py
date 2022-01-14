from flask import Flask, render_template, redirect, request

import joblib

#Passing main context
app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])

        marks = str(round(model.predict([[hours]])[0][0]))
    
    return render_template('index.html', predicted_marks = marks)

if __name__ == '__main__':
    app.run(debug=True)