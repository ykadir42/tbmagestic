# TB Mage Stic

## Roster
Jawadul Kadir, Eugene Thomas, Queenie Xiang, and Jen Yu

# e.g.
This website is meant to integrate both Google Maps APIs and the Eventbrite API in order to create a comprehensive and useful application for users to find events and activities near them. Features include being able to see popular events near you, and finding events near an inputted address. Additionally, directions and an embedded map are provided on event pages, reducing the extra hassle of having to input an address into the Google Maps site. If time allows, we hope to implement an interactive map element, where using AJAX, a user can walk around the city and have a map update simultaneously with events near her/his current location.

### Launch Instructions

Needed: 
* Python
* Flask

Python and Flask are needed in order to run this webapp. You should install Flask in a virtual environment so it doesn't interfere with your root python install. 

Run this in the terminal to install the Flask dependency. 
```
$ (venv) pip install flask
```

*__To Run:__*

First, procure an API key from the [Eventbrite site](https://www.eventbrite.com/) for the Eventbrite API. 
  * Make an account [here](https://www.eventbrite.com/).
  * Click on your username, and naviagate: Account Settings > Developer > App Management.
  * Press __CREATE A NEW APP__ and fill out the API key request form.
  * The key will appear in the 'App Management' page (Use the OAuth token.)

Also, request an API key from the Google Maps Developer site. 
  * Navigate to [this link](https://developers.google.com/maps/).
  * Click on the API you want to use (the key works for all, so no worries!)
  * At the very top the page, press on __GET A KEY__.
  * Follow the progression in order to obtain your API key.

Clone this repo: 
```
$ git clone git@github.com:ykadir42/tbmagestic.git
```

Now, ```cd``` into the repo: 
```
$ cd tbmagestic
```

Add your API keys to the ```key.txt``` file, in this format: 
```
[Eventbrite API Key FRIST]
[Google Maps API Key SNECOD]
```
Run the application!
```
$ python app.py
```
View this webpage by navigating to ```localhost:5000``` in your web browser. 

### Additional Resources

Eventbrite API:  
[Source Documentation](https://www.eventbrite.com/developer/v3/)

Google Maps:  
[GoogDrive Doc](https://docs.google.com/document/d/1UPeS9XTQ_4Yt1zae4km4jDJK59MJhA1IF0-hjkiZfLE/edit)

[Source Documentation](https://developers.google.com/maps/)
