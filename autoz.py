#Want to import schedule library and time library to keep track of time
# Need to include a library to read HTML form data into variables for python
import webbrowser


# Create class with parameters from the form data
class Course:
    def __init__(self, class_name, class_days, class_time, class_url):
        self.class_name = class_name
        self.class_days = class_days
        self.class_time = class_time
        self.class_url = class_url
#Class function that opens zoom link when time is triggered



#First step is to read in form data and create a "Course" for every row input in the form with the appropiate functions on submit



#Here I will put a schedule function, maybe in a loop to call the class function whenever the time is right and 
# increment to the next class time




p1 = Course("Cyber Securty", "T/H", "10:15", "lol.com")

#This is the code I will use to open the zoom link for each class
#webbrowser.open_new('https://byui.zoom.us/j/2592059656')  # Go to example.com
