import os
import pyrebase
import json
from webscraper import date, blog_id


config = {
  "apiKey": os.environ.get('FIREBASE_KEY_SCRAPER'),
  "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN_SCRAPER'),
  "databaseURL": os.environ.get('FIREBASE_DB_URL_SCRAPER'),
  "projectId": os.environ.get('scraping-workouts'),
  "storageBucket": os.environ.get('FIREBASE_STORE_BUCKET_SCRAPER'),
  "messagingSenderId": os.environ.get('FIREBASE_MSG_SENDER_ID_SCRAPER'),
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

blogID = str(blog_id)


with open('./testing/scraping_test/workoutData.json') as json_data:
    jsonData = json.load(json_data)

db.child(blogID).push(jsonData)


#for i in jsonData:
#    print("Date: " + i['Title'] + " Workout -- " + i['Workout'], )
