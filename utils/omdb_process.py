import urllib2, json
import nyt_process as nyt

omdb_base="http://www.omdbapi.com/?apikey="

#retrieves key from key.txt
f = open("key.txt", "r")
txt = f.read()
key = txt.split('\n')[1]

#Keep track of how often this function is called!
#DON'T go over quotas!!

'''
access_url(query) - Function to pull data from the OMDB API
 * query parameter is used to access specific information in API
 * used to access a movie that the user already searched for
 * and subsequently, to pull information about that movie
KEEP TRACK OF HOW OFTEN THIS FXN IS CALL TO NOT GO OVER QUOTAS.
'''
def access_url(query):
    acc = omdb_base + key
    if (query == ""):
        print "give me something to search for"

    else:
       try:
           acc += "&t="
           q = query.replace(' ', "+")
           acc += q
           data = urllib2.urlopen(acc)
           d = json.loads(data.read())
           return d
       except:
           print "your key is wrong or you have reached your monthy quota!"

'''
get_info(query) - Function to pull data from the OMDB API
 * query parameter is used to access information about a specific movie in API
 * used after the user selects a movie to view info about
 * returns a dictionary of all information extracted from OMDB API
'''
def get_info(query):
    d = access_url(query)
    info = {} #creates dictionary of information needed
    info["Title"] = d["Title"]
    info["Year"] = d["Year"]
    info["Genre"] = d["Genre"]
    info["Plot"] = d["Plot"]
    info["Poster"] = d["Poster"]
    info["Director"] = d["Director"]
    return info
