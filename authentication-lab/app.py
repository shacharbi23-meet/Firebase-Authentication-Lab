from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

config = {"apiKey": "AIzaSyCAUIlBaXwTW5VuAsfEKBH-Iq6rBfxS_Rc",
"authDomain": "a-demo-96540.firebaseapp.com",
"projectId": "a-demo-96540",
"storageBucket": "a-demo-96540.appspot.com",
"messagingSenderId": "604078986811",
"appId": "1:604078986811:web:1f1d1d1dc26109e2c16e1e",
"measurementId": "G-DF593TBGXY",
"databaseURL": ""}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



if __name__ == '__main__':
    app.run(debug=True)