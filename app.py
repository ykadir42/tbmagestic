from flask import Flask, render_template, redirect, request, session, flash
from utils import eventbrite
from utils import database
import os



app = Flask(__name__)
#encrypts the values that you put in our cookie
app.secret_key = os.urandom(32)


@app.route("/")
def root():
	return render_template("index.html")

@app.route("/login")
def login():
        return render_template("login.html")

@app.route("/login_redirect")
def login_redirect():
        #If logout: 
        if "submit" in request.args and request.args["submit"] == "Logout":
		session["username"] = ""
		flash("You logged out.")
                return redirect("/")
        #If logged in:   
        if "username" in request.args and session.get('username'):
                return redirect("/")

        username = ""
        password = ""

        #Grabbing user info: 
        if "user" in request.args and "pass" in request.args:
		username = request.args["user"].lower()
		password = request.args["pass"]

        #If not correct login info:
        if not database.verify_user(username, password):
                error = "Incorrect information. Please try again."
                return render_template("error.html", error=error)
        else: 
              session["username"] = username
	      return redirect("/")

        return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method=="POST":
		return request.form['user']
	return render_template('register.html')


@app.route('/register_redirect', methods=["GET", "POST"])
def register_redirect():
    user = request.form["user"]
    password1 = request.form["pass"]
    verifypass1 = request.form["pass_repeat"]
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    email = request.form["email"]

    #Adding user to database
    add_user = database.add_user(user, password1, verifypass1, first_name, last_name , email)

    if add_user:
            return redirect("/")
    elif add_user == "Error 1":
            flash('Error, username taken. Redirecting to the register page')
	    return render_template('register.html')

    elif add_user == "Error 2":
            flash('Error, passwords did not match. Redirecting to the register page')
	    return render_template('register.html')

    return add_user


@app.route("/user_info")
def return_user_info():
        if session.get('username'):
                try: 
                        username = session.get('username')
                        accs = database.return_accounts_info()
                        text = "Welcome " + accs[username]['firstname'] +" !"

                        #Grabs user's past searches 
                        saved_searches = database.return_history(username)
                        return render_template("user_info.html", text = text, history=saved_searches[username]['history'])
                except:
                        return render_template("user_info.html", text = text, history="No saved searches")
                        
        
        
        else:
                return redirect("/login")

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

        if session.get('username'):
                #Adds search to user's search history
                username = session.get('username')
                print "Added to search history"
                database.add_history(username,form["query"])
                
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
        #Grabbing user input
	address = request.args["inputAddress"]
        query = request.args["inputQuery"]
	radius = request.args["inputRadius"]

        #Grabbing info from eventbrite
	results = eventbrite.advancedsearch(address, query, radius)

        if session.get('username'):
                username = session.get('username')
                print "Added to search history"
                database.add_history(username,query)
                
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



if __name__ == "__main__":
	app.debug = True
	app.run()
