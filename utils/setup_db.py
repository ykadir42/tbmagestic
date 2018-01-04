import sqlite3

f = "../data/filmadillo.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#create user/pwd and history table
c.execute("CREATE TABLE users (user TEXT, pass TEXT, PRIMARY KEY(user))")
c.execute("CREATE TABLE history (user TEXT, movie TEXT, plot TEXT, url TEXT)")

db.commit() #save changes
db.close()  #close database
