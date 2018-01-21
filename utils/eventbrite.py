import urllib2, json
import google

ebrite_base="https://www.eventbriteapi.com/v3/events/?"

#retrieves key from key.txt
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[0]
print key

'''
access_url(query) - Function to pull data from the Eventbrite API
 * query parameter is used to access specific information in API
 * used to access an event
 * and subsequently, to pull information about that movie
KEEP TRACK OF HOW OFTEN THIS FXN IS CALL TO NOT GO OVER QUOTAS.
'''

def access_url(query):
    acc = ebrite_base
    if (query == ""):
        print "Nothing to search for..."
    else:
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

def get_events(query):
    d = access_url(query)
    events = d["events"]
    '''
    top_events = d["top_match_events"]
    results = {}
    results["events"] = events
    results["top_events"] = top_events
    return results
    '''
    return events


def advancedsearch_raw(address, query, radius):
    link = ebrite_base
    if (query == ""):
        print ("Nothing to search for...")
    if (address == ""):
        print ("No address given...")
    else:
        try:
            coord = google.get_lat_lng(address)
            #zipcode = google.get_zipcode(address)
            link += "q="
            q = query.replace(' ', '+')
            link += q
            link += "&token=" + key
            a = address.replace(' ', '+')
            link += "&location.address=" + a 
            link += "&sort_by=best"
            link += "&location.latitude=" + str(coord[0])
            link += "&location.longitude=" + str(coord[1])
            link += "&location.within=" + str(radius) + "mi"
            print "\n\nhere!\n\n"
            print link
            data = urllib2.urlopen(link)
            d = json.loads(data.read())
            return d['events']
        except:
            print repr(key)
            print "Key is incorrect, or quota reached."
            return []

def advancedsearch(address, query, radius):
    events = advancedsearch_raw(address, query, radius)
    processed = []
    newDict = {}
    for event in events:
        newDict["url"] = event["url"]
        newDict["name"] = event["name"]["text"]
        newDict["status"] = event["status"]
        try:
            shortened = event["description"]["text"].split(" ")
            shortened = shortened[:50]
            str1 = ' '.join(shortened)
            newDict["description"] = str1 + "..."
        except:
            print "No description."
            newDict["description"] = "No description."
        newDict["venue"] = event["venue_id"]
        start = event["start"]["local"]
        dStart = start.split("T")[0]
        tStart = start.split("T")[1]
        newDict["dStart"] = dStart
        newDict["tStart"] = tStart
        newDict["tzone"] = event["start"]["timezone"]
        end = event["end"]["local"]
        dEnd = end.split("T")[0]
        tEnd = end.split("T")[1]
        newDict["dEnd"] = dEnd
        newDict["tEnd"] = tEnd
        newDict["logo"] = event["logo_id"]
        processed.append(newDict)
        newDict = {}
    return processed
    
'''  
<br>
  <!--
  {% for i in d %}
  <form action = {{i["url"]}} method = 'POST' style="text-align:left">
    <h3> {{ i["name"]["text"]}} </h3>
    <p>{{i["status"]}}</p>
   <p>{{i["venue_id"]["address"]}}</p><br>
    <p>{{ i["description"]["text"] }} </p>
    <input type = "hidden" name = "title" value = {{ i[0] }}>
    <input type = "hidden" name = "url" value = {{ i[1] }}>
    <a href = {{i["url"]}}><button type="submit" class="btn btn-info">More Info</button></a>-->
    <br><br>
  </form>
  {% endfor %}
'''
