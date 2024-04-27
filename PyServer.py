from flask import Flask, render_template, request, redirect, session
from flask_basicauth import BasicAuth

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return render_template('index.html')
        else:
            return render_template('unauthorized.html')

@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
