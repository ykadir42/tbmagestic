import sqlite3
from flask import request, flash

if __name__ == '__main__':
    # initialize database
    db = sqlite3.connect("data/eg.db")
    c = db.cursor()
    # table for user login
    c.execute("CREATE TABLE users (user TEXT, pass TEXT, PRIMARY KEY(user))")
    #table with all saved movies
    c.execute("CREATE TABLE history (user TEXT, movie TEXT, PRIMARY KEY(user))")
    # save and close database
    db.commit()
    db.close()

# -----FUNCTIONS FOR LOGIN SYSTEM-----


# returns a dictionary for user data {user: pass}
def getUsers():
    db = sqlite3.connect("data/eg.db")
    c = db.cursor()
    a = 'SELECT user, pass FROM users'
    x = c.execute(a)
    users = {}
    for line in x:
        users[line[0]] = line[1]
    db.close()
    return users


# add the login to the database
def addUser(user, password):
    db = sqlite3.connect("data/eg.db")
    c = db.cursor()
    vals = [user, password]
    c.execute("INSERT INTO users VALUES(?, ?)", vals)
    db.commit()
    db.close()

# --------------------------------------------------


#----------------FUNCTIONS FOR USERS----------------

def get_user_history(user):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("SELECT movie, plot, url FROM history WHERE user= ?", [user])
    movies = []
    for line in x:
        movies.append(line)
    db.close()
    return movies

#add movie into user's list of saved movies
def add(user, movie, plot, url):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    vals = [user, movie, plot, url]
    #hass the movie already saved?
    if check(user, movie) == True:
        x = c.execute("INSERT INTO history VALUES(?, ?, ?, ?)", vals)
    db.commit()
    db.close()

#looks for this movie where the person who saved it is this user
#to check if the movie has already been saved
def check(user, movie):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("SELECT movie FROM history WHERE user= ?", [user])
    print x
    for line in x:
        print line
        if movie == line[0]:
            db.close()
            return False
    db.close()
    return True

#remove this movie from the user's list
def remove(user, movie):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("DELETE FROM history WHERE user= ? AND movie = ?", [user, movie])
    db.commit()
    db.close()

#print "---------\n\n" +  + "\n\n-------------"
