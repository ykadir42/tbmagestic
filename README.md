<span style="color:lightblue;">e.g.</span>
=====

Users will receive a wide variety of events from the Eventbrite API based on their location, found by Google Maps Geolocation API. Currently, geolocation is still in progress, but a user can use the advanced search options to search for events near a certain address and within a certain radius.

# How to Run

Before being able to use the website, you will have to acquire the Eventbrite API key and set it up. Make an account [here](https://www.eventbrite.com/) and click on your name, then Account Settings>Developer>App Management. Click "CREATE A NEW APP" and fill out the form to request an API key. The key will now appear in your App Management page. Copy the API key into a plain text file named key.txt and place the file in the same directory as app.py. Now call `python app.py` in the terminal and navigate to localhost:5000 on your browser to use out website.