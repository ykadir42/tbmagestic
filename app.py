from flask import Flask, render_template
import urllib, urllib2

app = Flask(__name__)

@app.route("/")
def home():
    query = "My home address"
    return render_template("embed_demo.html", query = urllib.quote(query))

if __name__ == "__main__":
    app.debug = True
    app.run()
