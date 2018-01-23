from flask import Flask, render_template, redirect, url_for, request, session
import urllib, urllib2, json
from utils import eventbrite, auth
import os

app = Flask(__name__)
#encrypts the values that you put in our cookie
app.secret_key = os.urandom(32)

def remove_space(text):
    index = 0
    for character in text:
        if character == " ":
            text = text[0:index] + text[index+1:]
        else:
            index += 1
    return text

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
     #CURRENT DEFAULT WHILE GEOLOCATION DOESN'T WORK
    results = eventbrite.advancedsearch("New York", request.args["query"], 2)
    return render_template("search.html", d = results)

@app.route("/advancedsearch")
def advancedsearch():
    return render_template("advancedsearch.html")

@app.route("/advancedresults")
def advancedresults():
    address = request.args["inputAddress"]
    query = request.args["inputQuery"]
    radius = request.args["inputRadius"]
    results = eventbrite.advancedsearch(address, query, radius)
    return render_template("search.html", d = results)

@app.route("/event", methods=['GET', 'POST'])
def event():
    args = request.form.to_dict()
    print "\n\nARGS COMIN THRU \n\n"
    print args
    return render_template("eventpage.html", e = args)

#login authentication
@app.route('/login', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        flash("Yikes! You're already signed in.")
        return redirect('profile')
    # user entered login form
    elif request.form.get('login'):
        print "login"
        return auth.login()
    # user didn't enter form
    else:
        return render_template('login.html', title = "Login")

#signup
@app.route('/signup', methods=['GET', 'POST'])
def crt_acct():
    # user already logged in
    if session.get('username'):
        flash("Yikes! You're already signed in.")
        return redirect('profile')
    # user already filled out signup form
    elif request.form.get('signup'):
        return auth.signup()
    else:
        return render_template('signup.html', title = "Signup" )

if __name__ == "__main__":
    app.debug = True
    app.run()
