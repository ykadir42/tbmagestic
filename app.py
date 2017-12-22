from flask import Flask, render_template, redirect, url_for, request
import urllib, urllib2, json

app = Flask(__name__)

@app.route("/")
def root():
    query = "Stuyvesant"
    return render_template("index.html")

@app.route("/home")
def home():
	query = request.args["query"]
	print "query: " + query

	#events
	cmd = "https://www.eventbriteapi.com/v3/events/search/?q=" + urllib.quote(query) + "&token=SON34CONY7CHJOP4LXMU&location.address=345%20Chambers%20St,%20New%20York,%20NY%2010282&location.within=2mi"
	print " " + cmd + " "
	uResp = urllib2.urlopen(cmd)
	data = uResp.read()
	d = json.loads(data)
	events = d["events"]
	for event in events:
		if not "venue_id" in event:
			events.remove(event)

	#venues
	addresses = []
	for i in range(10):
		cmd = "https://www.eventbriteapi.com/v3/venues/" + events[i]["venue_id"] + "?token=SON34CONY7CHJOP4LXMU"
		#print " " + cmd + " "
		uResp = urllib2.urlopen(cmd)
		data = uResp.read()
		d = json.loads(data)
		#print d
		addresses.append(d["address"]["localized_address_display"])

	#directions
	directions = []
	for i in range(10):
		cmd = "https://maps.googleapis.com/maps/api/directions/json?origin=Stuyvesant%20High%20School&destination="+ urllib.quote(addresses[i]) + "&key=AIzaSyALW1zijvrQPm_RLEiR0O-3Em1f-tz4ULY"
		print " " + cmd + " "
		uResp = urllib2.urlopen(cmd)
		data = uResp.read()
		d = json.loads(data)
		#print d
		directions.append(d["routes"][0]["legs"][0]["steps"])

	return render_template("demo.html", addresses = addresses, directions = directions, events = events)

if __name__ == "__main__":
    app.debug = True
    app.run()
