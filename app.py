import pyrebase
import json

config = {
  "apiKey": "AIzaSyB4YbNMkY-1CjnjOLwuS1O30mwS1z3eaKU",
  "authDomain": "scraping-workouts.firebaseapp.com",
  "databaseURL": "https://scraping-workouts.firebaseio.com",
  "projectId": "scraping-workouts",
  "storageBucket": "scraping-workouts.appspot.com",
  "messagingSenderId": "48784455086",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()




with open('workoutData.json') as json_data:
    jsonData = json.load(json_data)

db.child("names").push(jsonData)

#for i in jsonData:
#    print("Date: " + i['Title'] + " Workout -- " + i['Workout'], )
