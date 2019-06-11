from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import tkinter as tk
#from flask_mail import Mail #adds email


#  Set up blog_id to account for today
#  blog_id decreases by 1 every day after date of blog id update
#  *reset this function weekly*

# activate test environment --> .\env\Scripts\activate

date = datetime.today()
blog_id = 376757 - (date.day - 10)

url = 'https://crossfit-toybox.triib.com/blog/2019-06-'+ str(date.day) + '/'+ str(blog_id) + '/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

#workout = content.findAll('div', attrs={"class": "col-md-7"}).text

#for workout in content.findAll('div', attrs={"class": "col-md-7"}):
    #print(workout.text.encode('utf-8'))

workoutArr = []
for item in content.findAll('div', attrs={"class": "col-md-8"}):
    for workout in item.findAll('div', attrs={"class": "panel-body"}):
        if workout.find('h5') != None:
            workoutObject = {
                "Title": workout.find('h5').text.replace("\"B\"", ""),
                "Workout": workout.find('div', attrs={"class": "workout_description"}).text.replace("\u00a0", ""),
            }
            workoutArr.append(workoutObject)

#print(workoutArr)

with open('./testing/scraping_test/workoutData.json', 'w') as outfile:
    json.dump(workoutArr, outfile)


#add pop-up on desktop

#root = tk.Tk()

#canvas1 = tk.Canvas(root, width = 1500, height = 350)
#canvas1.pack()

#label1 = tk.Label(root, text= workoutArr)
#canvas1.create_window(750, 150, window=label1)

#root.mainloop()



# add email every morning

#mail = Mail()

#add to config

#    MAIL_PORT = 587
#    MAIL_USE_TLS = True
#    MAIL_USERNAME = os.environ.get('EMAIL_USER')
#    MAIL_PASSWORD =os.environ.get('EMAIL_PASS')

#Email function

#def send_reset_email(user):
#    token = user.get_reset_token()
#    msg = Message('Password Reset Request', sender='testing@demo.com', recipients=[user.email])
#    msg.body = f'''To reset your password, visit the following link:
#{url_for('users.reset_token', token=token, _external=True)}

#If you did not make this request, simply ignore this email and no changes will be made
#'''
#    mail.send(msg)
