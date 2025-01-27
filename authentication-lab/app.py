from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            print("Error, identification failed. Please try again.")
    return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user= {"Name":request.form['fullname'], "Usename": request.form['username'], "Bio": request.form['bio']}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('add_tweet'))
        except:
            print("Error, identification failed. Please try again.")
    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        try:
            tweet = {"Title": request.form['title'], "Text": request.form['text'], "UID":  login_session["user"]["localId"]}
            db.child("Tweets").push(tweet)
            return redirect(url_for('all_tweets'))
        except:
            print("Error, couldn't make a post.")
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


@app.route('/all_tweets', methods = ['GET', 'POST'])
def all_tweets():
    return render_template('tweets.html', tweets = db.child('Tweets').get().val())

config = {"apiKey": "AIzaSyCAUIlBaXwTW5VuAsfEKBH-Iq6rBfxS_Rc",
"authDomain": "a-demo-96540.firebaseapp.com",
"projectId": "a-demo-96540",
"storageBucket": "a-demo-96540.appspot.com",
"messagingSenderId": "604078986811",
"appId": "1:604078986811:web:1f1d1d1dc26109e2c16e1e",
"measurementId": "G-DF593TBGXY",
"databaseURL": "https://a-demo-96540-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()



if __name__ == '__main__':
    app.run(debug=True)