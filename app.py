from flask import Flask, render_template, redirect, request, session, flash
from utils import eventbrite
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

def dateConversion(string):
	year = string[:4]
	month = string[5:7]
	day = string[8:]
	return month + "-" + day + "-" + year

def timeConversion(string):
	hours = int(string[:2])
	minute = string[3:5]
	tOfDay = 'am'
	if hours > 12:
		hours = hours - 12
		tOfDay = 'pm'
	hour = str(hours)
	return hour + ":" + minute + " " + tOfDay

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
	print "request" + str(request)
	print "args" + str(request.args)
	print "form" + str(request.form)
	form = request.form
	#print form['latitude'];
	if("latitude" in form):
		results = eventbrite.get_events_location(form["query"], form["latitude"], form["longitude"])
	else:
		results = eventbrite.get_events(form["query"])
	print results
	if(results == []):
		print "No results found"
		flash("Whoops! We couldn't find an event for you!")
		return render_template("search.html")
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
	print results
	if(results == []):
		print "No results found"
		flash("Whoops! We couldn't find an event for you!")
		return render_template("search.html")
	return render_template("search.html", d = results)

@app.route("/event", methods=['GET', 'POST'])
def event():
	args = request.form.to_dict()
	args['dS'] = dateConversion(args['dS'])
	args['dE'] = dateConversion(args['dE'])
	args['tS'] = timeConversion(args['tS'])
	args['tE'] = timeConversion(args['tE'])
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
