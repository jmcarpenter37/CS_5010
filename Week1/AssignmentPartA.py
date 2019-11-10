# Name of Activity: Python Assignment 1 Part A
# Name: John Carpenter
# ID: jmc7dt
# Date: 8/29/2019
import sys
import os
# sys.stdout = open("TestFile.txt" , 'a')
# Prompt user for: First Name, Last Name, Age
counter = 0 # Using the counter so once the fourth entry is complete the dictionary will be written to a .txt file
dict = {} # Initialize an empty dictionary to add Key : Value pairs to it.
while counter <= 3:
    print("Please enter your first name or type 'stop' to cancel the program: ")
    first = input()
    first = first.strip() # Stripping the leading and trailing whitespace
    print("Please enter your last name: ")
    last = input()
    last = last.strip() # Stripping the leading and trailing whitespace
    print("Please enter your age: ")
    age = input()
    age = int(age.strip()) # Stripping the leading and trailing whitespace and casting age as an int
    # Concatenate the First name and Last name into a single string so it looks like "Last-First"
    concat = last + "-" + first
    # print("Dict pre: {}".format(dict)) Used to make sure the dictionary was updating
    dict[concat] = age
    # print("Dict post: {}".format(dict)) Used to make sure the dictionary was updating
    counter +=1

# Write the dictionary to a .txt file
with open('myOutput.txt' , 'w') as f:
    print(dict , file = f)

