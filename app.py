import pyrebase
import json
from webscraper import date, blog_id

config = {
  "apiKey": "#########################",
  "authDomain": "scraping-workouts.firebaseapp.com",
  "databaseURL": "https://scraping-workouts.firebaseio.com",
  "projectId": "scraping-workouts",
  "storageBucket": "scraping-workouts.appspot.com",
  "messagingSenderId": "48784455086",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

blogID = str(blog_id)


with open('workoutData.json') as json_data:
    jsonData = json.load(json_data)

db.child(blogID).push(jsonData)

#for i in jsonData:
#    print("Date: " + i['Title'] + " Workout -- " + i['Workout'], )
