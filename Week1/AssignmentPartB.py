# Name of Activity: Python Assignment 1 Part A
# Name: John Carpenter
# ID: jmc7dt
# Date: 8/31/2019
# Create a long sentence of words
import numpy as np
sent = "Hello there my name is John Carpenter and I am a computer scientist and I a have dog named Otto and he is a Great Pyrenees"
# Put the words into a list
sentList = list(sent.split(" ")) # Put sentence into list split by a space since we are assuming no punctuation
# print(sentList) # Checking to make sure a list was created and each word was separated by a " " 
# We want this so we can use the list comprehension loop
[print(sentList[word], len(sentList[word]) ) for word in range(len(sentList))] # Using the list comprehension to store the word and it's length in a tuple.
# As you can see each time a word in sentList is iterated through it prints the word and its length.
