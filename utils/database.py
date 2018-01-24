#To hash passwords:
from hashlib import *
from hashlib import sha1

#To work with sqlite databses: 
import sqlite3

import ast
import csv      
import json


f ="utils/database.db"
db = sqlite3.connect(f)
c = db.cursor()

#Create the Users table with username, password, first name, last name, and email 
command1_create = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, firstname TEXT, lastname TEXT, email TEXT)"
#Create the search history table with all the users and their search history
command2_create = "CREATE TABLE IF NOT EXISTS search_history (username BLOB, history TEXT)"
c.execute(command1_create)
c.execute(command2_create)

db.commit() #save changes
db.close()  #close database

#Returning all account information
def return_accounts_info():
    f="utils/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM users"
    accs = c.execute(q)
    users = {}
    for user in accs:
        username = user[0]
        password = user[1]
        firstname = user[2]
        users[username] = {}
        users[username]['password'] = password
        users[username]['firstname'] = firstname
    return users

#Verifying user credentials 
def verify_user(username, password):
    accounts_info = return_accounts_info()
    if not(username in accounts_info):
        return False
    
    if (accounts_info[username]['password'] == sha1(password).hexdigest()):
        return True
    
    return False

#Adding new user
def add_user(username, password1, verifypass1,  first_name, last_name, email):
    f="utils/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    
    accounts_info = return_accounts_info()

    if username in accounts_info: 
        return "Error 1"

    elif password1 != verifypass1:
        return "Error 2" 

    else:
        password = sha1(password1).hexdigest()
    
        command = "INSERT INTO users VALUES(?,?,?,?,?)"
        c.execute(command, (username, password, first_name, last_name, email))
        db.commit()
        db.close()
        return True

    return False

#Adding new user search history
def add_history(username, search_query):
    f="utils/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "INSERT INTO search_history VALUES(?, ?)"
    c.execute(command, (username, search_query))
    db.commit()
    db.close()

    return True


#Return user search history
def return_history(username):
    lst=[] 
    f="utils/database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT * FROM search_history"
    searches = c.execute(q)
    saved_history = {}
    for entry in searches:
        if entry[0] == username: 
            history = entry[1]
            saved_history[username] = {}
            saved_history[username]['history'] = lst
            saved_history[username]['history'].append(history)
            

    return saved_history

