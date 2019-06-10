from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import tkinter as tk



#  Set up blog_id to account for today
#  blog_id decreases by 1 every day after 5.11.19
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
                "Title": workout.find('h5').text,
                "Workout": workout.find('div', attrs={"class": "workout_description"}).text.replace("\xa0", ""),
            }
            workoutArr.append(workoutObject)

#print(workoutArr)

#root= tk.Tk()

#canvas1 = tk.Canvas(root, width = 1500, height = 350)
#canvas1.pack()

#label1 = tk.Label(root, text= workoutArr)
#canvas1.create_window(750, 150, window=label1)

#root.mainloop()

with open('workoutData.json', 'w') as outfile:
    json.dump(workoutArr, outfile)
