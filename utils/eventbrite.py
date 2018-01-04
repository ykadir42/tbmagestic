import urllib2, json

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
