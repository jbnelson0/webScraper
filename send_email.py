import os
import yagmail
from datetime import datetime

date = datetime.today()
yag = yagmail.SMTP(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))

#Email function
def send_email(data):
    contents = data
    yag.send('james.bnelson0@gmail.com', 'Workout for ' + str(date), contents)
