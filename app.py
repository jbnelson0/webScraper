import pyrebase
import json
from webscraper import date, blog_id

config = {
  "apiKey": "#########################",
  "authDomain": "############################",
  "databaseURL": "##########################",
  "projectId": "#######################",
  "storageBucket": "###################",
  "messagingSenderId": "##############",


}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

blogID = str(blog_id)


with open('workoutData.json') as json_data:
    jsonData = json.load(json_data)

db.child(blogID).push(jsonData)

#for i in jsonData:
#    print("Date: " + i['Title'] + " Workout -- " + i['Workout'], )
