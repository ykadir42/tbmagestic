import urllib2, json

places_base="https://maps.googleapis.com/maps/api/place/textsearch/json?"
details_base="https://maps.googleapis.com/maps/api/place/details/json?"

#retrieves key from key.txt
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[1]
#print key

'''
access_url(query) - Function to pull data from the Eventbrite API
 * query parameter is used to access specific information in API
 * used to access an event
 * and subsequently, to pull information about that movie
KEEP TRACK OF HOW OFTEN THIS FXN IS CALL TO NOT GO OVER QUOTAS.
'''

def access_url(query):
    acc = places_base
    if (query == ""):
        print "Nothing to search for..."
    else:
        try:
            acc += "query="
            q = query.replace(' ', "%20")
            acc += q
            acc += "&key=" + key
            data = urllib2.urlopen(acc)
            d = json.loads(data.read())
            return d
        except:
            print "Key is incorrect, or quota reached."

def get_lat_lng(address):
    link = places_base
    try:
        link += "query="
        a = address.replace(' ', '+')
        link += a
        link += "&key=" + key
        data = urllib2.urlopen(link)
        d = json.loads(data.read())
        print d["results"][0]["geometry"]["location"]
        coord = []
        coord.append(d["results"][0]["geometry"]["location"]["lat"])
        coord.append(d["results"][0]["geometry"]["location"]["lng"])
        return coord
    except:
        print "Address not found."

def get_placeid(address):
    link = places_base
    try:
        link += "query="
        a = address.replace(' ', '+')
        link += a
        link += "&key=" + key
        data = urllib2.urlopen(link)
        d = json.loads(data.read())
        print d['results'][0]['place_id']
        return d['results'][0]['place_id']
    except:
        print "Address not found."

def get_zipcode(address):
    placeid = get_placeid(address)
    link = details_base
    try:
        link += "placeid="
        link += placeid
        link += "&key=" + key
        data = urllib2.urlopen(link)
        d = json.loads(data.read())
        return d["result"]["address_components"][7]["long_name"]
    except:
        print "Placeid invalid."
