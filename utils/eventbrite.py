import urllib2, json
import google

ebrite_base="https://www.eventbriteapi.com/v3/events/search?"

#retrieves key from key.txt
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[0]
#print key

'''
access_url(query) - Function to pull data from the Eventbrite API
 * query parameter is used to access specific information in API
 * used to access an event
 * and subsequently, to pull information about that movie
KEEP TRACK OF HOW OFTEN THIS FXN IS CALL TO NOT GO OVER QUOTAS.
'''

def access_url(query):
	acc = ebrite_base
	try:
		acc += "q="
		q = query.replace(' ', "%20")
		acc += q
		acc += "&token=" + key
		data = urllib2.urlopen(acc)
		d = json.loads(data.read())
		return d
	except:
		print "Key is incorrect, or quota reached."
		return []

def get_events(query):
	d = access_url(query)
	if("top_match_events" in d and "events" in d):
		events = d["top_match_events"] + d["events"]
	elif ("events" in d):
		events = d["events"]
	elif ("top_match_events" in d):
		events = d["top_match_events"]
	else:
		events = None
	'''
	top_events = d["top_match_events"]
	results = {}
	results["events"] = events
	results["top_events"] = top_events
	return results
	'''
	return events

def access_url_location(query, latitude, longitude):
	acc = ebrite_base
	try:
		acc += "q="
		q = query.replace(' ', "%20")
		acc += q
		acc += "&location.latitude=" + latitude
		acc += "&location.longitude=" + longitude
		acc += "&location.within=2mi"
		acc += "&token=" + key
		#print acc
		data = urllib2.urlopen(acc)
		d = json.loads(data.read())
		return d
	except:
		print "Key is incorrect, or quota reached."
		return []

def get_events_location(query, latitude, longitude):
	d = access_url_location(query, latitude, longitude)
	#print d
	if("top_match_events" in d and "events" in d):
		events = d["top_match_events"] + d["events"]
	elif ("events" in d):
		events = d["events"]
	elif ("top_match_events" in d):
		events = d["top_match_events"]
	else:
		events = None
	'''
	top_events = d["top_match_events"]
	results = {}
	results["events"] = events
	results["top_events"] = top_events
	return results
	'''
	return events

def advancedsearch(address, query, radius):
	link = ebrite_base
	link += "token=" + key
	try:
		coord = google.get_lat_lng(address)
		if(query != ''):
			link += "&q="
			q = query.replace(' ', '%20')
			link += q
		if(address != ''):
			link += "&location.address="
			a = address.replace(' ', '%20')
			link += a
		link += "&location.within="
		if(radius != ''):
			r = radius.replace(' ', '%20')
			link += r + "mi"
		else:
			link += "2mi"
		print link
		data = urllib2.urlopen(link)
		print data
		d = json.loads(data.read())
		print d
		return d['events']
	except:
		print repr(key)
		print "Key is incorrect, or quota reached."
		return []

# def advancedsearch(address, query, radius):
#     events = advancedsearch_raw(address, query, radius)
#     processed = []
#     newDict = {}
#     for event in events:
#         newDict["url"] = event["url"]
#         newDict["name"] = event["name"]["text"]
#         newDict["status"] = event["status"]
#         try:
#             shortened = event["description"]["text"].split(" ")
#             shortened = shortened[:50]
#             str1 = ' '.join(shortened)
#             newDict["description"] = str1 + "..."
#         except:
#             print "No description."
#             newDict["description"] = "No description."
#         newDict["venue"] = event["venue_id"]
#         start = event["start"]["local"]
#         dStart = start.split("T")[0]
#         tStart = start.split("T")[1]
#         newDict["dStart"] = dStart
#         newDict["tStart"] = tStart
#         newDict["tzone"] = event["start"]["timezone"]
#         end = event["end"]["local"]
#         dEnd = end.split("T")[0]
#         tEnd = end.split("T")[1]
#         newDict["dEnd"] = dEnd
#         newDict["tEnd"] = tEnd
#         newDict["logo"] = event["logo_id"]
#         processed.append(newDict)
#         newDict = {}
#     return processed
