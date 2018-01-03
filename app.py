from flask import Flask, render_template, redirect, url_for, request
import urllib, urllib2, json

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

@app.route("/home")
def home():
    address = remove_space(request.args["address"])
    #print address
    query = remove_space(request.args["query"])    
    radius = remove_space(request.args["radius"]) 
    print "query: " + query
    print "address: " + address
    print "radius: " + radius
    
    #events
    link = "https://www.eventbriteapi.com/v3/events/search/?q="
    link += query
    link += "&token=SON34CONY7CHJOP4LXMU&"
    link += "location.address="
    link += address
    link += "&location.within="
    link += radius
    link += "mi"

    print link

   
    uResp = urllib2.urlopen(link)
    data = uResp.read()
    d = json.loads(data)
    events = d["events"]
    top_events = d["top_match_events"] 
    

    return render_template("return_page.html", d = events, f = top_events)

if __name__ == "__main__":
    app.debug = True
    app.run()

    
'''
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
''' 
