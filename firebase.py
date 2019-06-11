import pyrebase
from config import Config_fb

firebase = pyrebase.initialize_app(Config_fb)
db = firebase.database()

def add_workout(blogID, jsonData):
    db.child(blogID).push(jsonData)
