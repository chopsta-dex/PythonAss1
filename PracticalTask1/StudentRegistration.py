# Assessment 1
# Practical Task 1

# StudentRegistration.py
# This program processes the details of three students and displays their information on the screen
# Author: Lucas Beyer
# Date: 24/10/23

import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()
application_window.withdraw()

# The totalFees variable needs to be initialised
totalFees = 0.0

# Let's start with the printHeadings() function
def printHeadings():
    print("---HOLMESGLEN INSTITUTE---")
    print("ID\tNAME\t\tCOURSE\t\t\tFEE\n")

# Now let's make the function that creates a new student
# This function takes a dictionary as a parameter and fills it with values
def inputStudentDetails(dict):
    dict["id"] = simpledialog.askstring("Student Details", "What is this student's ID?", parent=application_window)
    dict["name"] = simpledialog.askstring("Student Details", "What is this student's name?", parent=application_window)
    dict["course"] = simpledialog.askstring("Student Details", "What is this student's course?", parent=application_window)
    dict["fee"] = simpledialog.askfloat("Student Details", "What is this student's fee?", parent=application_window)
    print("This student's details:")
    print(f"ID: {dict["id"]}")
    print(f"Name: {dict["name"]}")
    print(f"Course: {dict["course"]}")
    print(f"Fee: ${dict["fee"]}")

# Now lets create empty dictionaries for our three students
student1 = {"id": "", "name": "", "course": "", "fee": 0.0}
student2 = {"id": "", "name": "", "course": "", "fee": 0.0}
student3 = {"id": "", "name": "", "course": "", "fee": 0.0}

# Now we can create our students
inputStudentDetails(student1)
inputStudentDetails(student2)
inputStudentDetails(student3)

# And add our fees together
totalFees = student1["fee"] + student2["fee"] + student3["fee"]

# We can create out display fees function
def outputTotalFee():
    print("\nTotal fees: $", end="")
    print(f'{totalFees:,}')

# I will create a function to help me display each student
def showStudent(dict):
    tab = '\t'
    print(f"{dict['id']}{tab}{dict['name']}{tab}{tab}{dict['course']}{tab}{tab}${dict['fee']:,}")

# And now we can display the final output
printHeadings()
showStudent(student1)
showStudent(student2)
showStudent(student3)
outputTotalFee()