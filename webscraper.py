from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import tkinter as tk
from send_email import send_email
from firebase import add_workout


#  Set up blog_id to account for today
#  blog_id decreases by 1 every day after date of blog id update
#  *reset this function weekly*

# activate test environment --> .\env\Scripts\activate

date = datetime.today()
blog_id = 390943 - (date.day - 8)

url = 'https://crossfit-toybox.triib.com/blog/2019-07-'+ str(date.day) + '/'+ str(blog_id) + '/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

#workout = content.findAll('div', attrs={"class": "col-md-7"}).text

#for workout in content.findAll('div', attrs={"class": "col-md-7"}):
    #print(workout.text.encode('utf-8'))

workoutArr = []
for item in content.findAll('div', attrs={"class": "col-md-8"}):
    for workout in item.findAll('div', attrs={"class": "panel-body"}):
        workoutObj = workout.find('div', attrs={"class": "workout_description"}).text.replace("\u00a0", "")
        workoutArr.append(workoutObj)

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


#send Email
send_email(workoutArr)
add_workout(blog_id, workoutArr)
