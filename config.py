import os

Config_fb = {
    "apiKey": os.environ.get('FIREBASE_KEY_SCRAPER'),
    "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN_SCRAPER'),
    "databaseURL": os.environ.get('FIREBASE_DB_URL_SCRAPER'),
    "projectId": "scraping-workouts",
    "storageBucket": os.environ.get('FIREBASE_STORE_BUCKET_SCRAPER'),
    "messagingSenderId": os.environ.get('FIREBASE_MSG_SENDER_ID_SCRAPER')
}

class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
