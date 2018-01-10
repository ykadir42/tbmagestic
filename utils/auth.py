from flask import redirect, url_for, request, session, flash
import database, hashlib

# scrits for logging in
# Logs user in (from form)

def login():
    users = database.getUsers()
    # checks credentials for login
    if request.form.get('username') in users:
        hash_object = hashlib.sha224(request.form.get('password'))
        hashed_pass = hash_object.hexdigest()
        if hashed_pass == users[request.form.get('username')]:
            session['username'] = request.form.get('username')
            return redirect(url_for('profile'))
        else:
            flash("Yikes! Bad password")
            return redirect(url_for('authentication'))
    else:
        flash("Yikes! Bad username")
        return redirect(url_for('authentication'))


# Signs user up for the website (from form)
def signup2():
    users = database.getUsers()
    # checks if credentials for flash message
    if request.form.get('username') in users:
        flash("Yikes! Username already taken")
        return redirect(url_for('crt_acct'))
    elif request.form.get('password0') != request.form.get('password1'):
        flash("Yikes! Passwords do not match")
        return redirect(url_for('crt_acct'))
    else:
        flash("Yay! Please log in with your new credentials!")
        hash_object = hashlib.sha224(request.form.get('password0'))
        hashed_pass = hash_object.hexdigest()
        database.addUser(request.form.get('username'), hashed_pass)
        return redirect(url_for('authentication'))

def signup():
    if request.form.get('password0') != request.form.get('password1'):
        flash("Yikes! Passwords do not match")
        return redirect(url_for('crt_acct'))
    else:
        flash("Yay! Please log in with your new credentials!")
        hash_object = hashlib.sha224(request.form.get('password0'))
        hashed_pass = hash_object.hexdigest()
        #database.addUser(request.form.get('username'), hashed_pass)
        return redirect(url_for('authentication'))

if __name__ == '__main__':
    database.addUser("elmo", "goldfish")
#print database.getUsers()
