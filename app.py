from flask import Flask, render_template, redirect, url_for, request
import urllib, urllib2, json
from utils import eventbrite

app = Flask(__name__)

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
    query = "Stuyvesant"
    return render_template("index.html")

@app.route("/search")
def search():
    #address = remove_space(request.args["address"])
    #print address
    #query = remove_space(request.args["query"])    
    #radius = remove_space(request.args["radius"]) 
    results = eventbrite.get_events(request.args["query"])
    print results
    return render_template("search.html", d = results)

if __name__ == "__main__":
    app.debug = True
    app.run()

'''
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
'''
