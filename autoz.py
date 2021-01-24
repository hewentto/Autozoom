#Want to import schedule library and time library to keep track of time
# Need to include a library to read HTML form data into variables for python
#%%
import webbrowser
import pandas as pd
import schedule
import time

#%%
# Create class with parameters from the form data
StartTimes = []
Days = []
class Course:
    def __init__(self, class_name, class_days, class_time, class_url):
        self.class_name = class_name
        self.class_days = class_days
        self.class_time = class_time
        self.class_url = class_url
    def StartClass(self):
        webbrowser.open_new(self.class_url)
#Class function that opens zoom link when time is triggered


#%%
#First step is to read in form data and create a "Course" for every row input in the form with the appropiate functions on submit
df = pd.read_excel("schedule.xlsx")

#read in data frame to list, then create a list of those class instances
classes = df.values.tolist()
classes_instances = []
for c in classes:
    classes_instances.append(Course(*c))

for instance in classes_instances:
    StartTimes.append(instance.class_time)
    Days.append(instance.class_days)

#%%
#creating 2d list itterate and combine into a 2d array that has one day with its certain times
DaysTimes = [Days,StartTimes]




#%%
#Here I will put a schedule function, maybe in a loop to call the class function whenever the time is right and 
# increment to the next class time
def job():
    webbrowser.open_new('https://byui.zoom.us/j/2592059656')


def job0():
    classes_instances[0].StartClass()

def job1():
    classes_instances[1].StartClass()

def job2():
    classes_instances[2].StartClass()

def job3():
    classes_instances[3].StartClass()

def job4():
    classes_instances[4].StartClass()

schedule.every().monday.at(str(classes_instances[2].class_time)).do(job2)
schedule.every().wednesday.at(str(classes_instances[2].class_time)).do(job2)
schedule.every().friday.at(str(classes_instances[2].class_time)).do(job2)

schedule.every().tuesday.at(str(classes_instances[0].class_time)).do(job0)
schedule.every().tuesday.at(str(classes_instances[1].class_time)).do(job1)
schedule.every().tuesday.at(str(classes_instances[3].class_time)).do(job3)
schedule.every().tuesday.at(str(classes_instances[4].class_time)).do(job4)

schedule.every().thursday.at(str(classes_instances[0].class_time)).do(job0)
schedule.every().thursday.at(str(classes_instances[1].class_time)).do(job1)
schedule.every().thursday.at(str(classes_instances[3].class_time)).do(job3)
schedule.every().thursday.at(str(classes_instances[4].class_time)).do(job4)

schedule.every(5).seconds.do(job)




while True:
    schedule.run_pending()
    time.sleep(1)


#This is the code I will use to open the zoom link for each class
#webbrowser.open_new('https://byui.zoom.us/j/2592059656')  # Go to example.com

# %%
