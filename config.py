import os

Config_fb = {
    "apiKey": "AIzaSyB4YbNMkY-1CjnjOLwuS1O30mwS1z3eaKU",
    "authDomain": "scraping-workouts.firebaseapp.com",
    "databaseURL": "https://scraping-workouts.firebaseio.com",
    "projectId": "scraping-workouts",
    "storageBucket": "scraping-workouts.appspot.com",
    "messagingSenderId": "48784455086"
}

class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
