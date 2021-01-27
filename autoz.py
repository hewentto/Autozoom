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
    # class function to open the web link for the zoom class
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
    # created two lists for future use to help automate the job/event creating
    # these lists contain all the start times and all the days
    # will need to find a way to make this a 2 day array that has each day once
    #with the correct times to start classes in those days
    StartTimes.append(instance.class_time)
    Days.append(instance.class_days)

#%%
#creating 2d list itterate and combine into a 2d array that has one day with its certain times
DaysTimes = [Days,StartTimes]




#%%
#Since I could not find a way to get this done in a for loop, seperate my classes
# into jobs manually

def working():
    print("Working...")


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

# this prints out "working..." help give feedback that the script is still on
schedule.every(5).minutes.do(working)

# This will open my personal zoom link for an example for the video
# schedule.every(5).seconds.do(job)



# this is the while loop that will continue checking the time for execute the jobs
# this can be modified also, and will be on the next itteration to help make this program
# functional as a background task.
while True:
    schedule.run_pending()
    time.sleep(60)


#This is the code I will use to open the zoom link for each class
#webbrowser.open_new('https://byui.zoom.us/j/2592059656')  # Go to example.com

# %%
