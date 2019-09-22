# ID: jmc7dt
# Name: John Carpenter
# Class: CS 5010
# Homework #3
import functools
# Q1 Create a dictionary of 10 key-value pairs. Choose a domain that interests you. What might you want to look up?
# Using a set of nested dictionaries to query some NHL teams in the Eastern Conference.
dict = {
    "NHL Teams" :
        {"Conference":
                       {"Eastern" :
                            {"Division" : {
                                "Atlantic":["Boston Bruins" , "Buffalo Sabres","Detroit Red Wings","Florida Panthers","Montreal Canadians","Ottawa Senators","Tampa Bay Lightning","Toronto Maple Leafs" ]
                                   ,"Metropolitan":["North Carolina Hurricanes","Colombus Blue Jackets","New Jersey Devils","New York Islanders","Philadelphia Flyers","Pittsburgh Penguins","Washington Capitals"]

                                    },

                             }









    }


}
}
# Demonstrate retrieving at least three different values and displaying the results.
print(dict["NHL Teams"]["Conference"]["Eastern"]["Division"]["Atlantic"]) # getting the teams in the Atlantic
print(dict["NHL Teams"]["Conference"]["Eastern"]["Division"]["Metropolitan"]) # getting the teams in the Eastern
print(dict["NHL Teams"]["Conference"]["Eastern"]["Division"]["Metropolitan"][0]) # Getting the first team in the Eastern

#Q2 Getting user input

print("Please enter your first name: \n")
first = input().strip() # Taking in thge first name and striping off the whitespace
print("Please enter a number")
num_one = float(input()) # Taking in the first number
print("Please enter a second number")
num_two = float(input()) # Taking in the second number
mult = float(num_one*num_two) # Cast as a float
print("Hi , {}! Multplying {} and {} is: {}".format(first , num_one, num_two, mult))

# Q3 Guessing game
name = "Watson"
guess_start = 0  # Use as a counter
while guess_start < 3:
    guess = input().strip() # Strip off the white space
    print("Guess the name of the computer who played on Jeopardy. You have 3 tries!")
    if guess == name:
        print("That's correct! Gameover")
        break
    elif guess != name:
        guess_start += 1
        print("Try again")
print("You ran out of tries!")

# Q4
sent = "are you suggesting coconuts migrate"
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in sent:
    if letter == "a":
        a+=1
    elif letter == "e":
        e+=1
    elif letter == "i":
        i+=1
    elif letter == "o":
        o+=1
    elif letter == "u":
        u+=1
    else:
        continue
print("The number of a's are: {}".format(a))
print("The number of e's are: {}".format(e))
print("The number of i's are: {}".format(i))
print("The number of o's are: {}".format(o))
print("The number of u's are: {}".format(u))

#Q5

# Create a long sentence of words
sent = "Hello there my name is John Carpenter and I am a computer scientist and I a have dog named Otto and he is a Great Pyrenees"
# Put the words into a list
sentList = list(sent.split(" ")) # Put sentence into list split by a space since we are assuming no punctuation
# print(sentList) # Checking to make sure a list was created and each word was separated by a " "
# We want this so we can use the list comprehension loop
[print(sentList[word], len(sentList[word]) ) for word in range(len(sentList))] # Using the list comprehension to store the word and it's length in a tuple.
# As you can see each time a word in sentList is iterated through it prints the word and its length.
array = [ sentList[word]  for word in range(len(sentList))]
# Sorting the array by length
def Sorting( array_string ):
    sorted_list = sorted(array_string , key = len) # This function sorts the array from smallest to largest. Taking advantage of the already build in sorted() method
    return sorted_list

sort = Sorting(array)
# Printing out word size tuples from smallest to largest using list comprehension
print("##########PRINTING OUR WORDSIZE TUPLES FROM SMALLEST TO SHORTEST##########")
[print(sort[word], len(sort[word]) ) for word in range(len(sentList))]
# Print out only unique words
print("##########PRINTING ONLY UNIQUE VALUES##########")
unique = set(sort)
print(unique)

# Q6 In the PowerPoint slides describing "higher-order functions" (02-Python - Map Filter Reduce.pdf) there are three examples:
# one illustrating the use of map, the next one illustrating the use of filter, and the last one illustrating the use of reduce.
# Rewrite these three examples without using the map(), filter(), and functools.reduce() functions.

# Map
import numpy as np
# I am going to use numpy since it can take operations and vectorize them
num_list = [1,2,3,4,5]
print("The squares of the entries in your list are: " , np.square(num_list))
print("#####################################################################\n")
# Filter
# We use the math operator mod() or modulus to look through a list and grab the odd numbers
# This is done when X mod(2) != 0
num_list = [1,2,3,4,5]
# For this example we should only get back 1 , 3 , and 5
odd_number = []
for i in np.arange(0,len(num_list),1):
    if num_list[i] % 2 != 0:
        print("Found an odd number: " , num_list[i])
        odd_number.append(num_list[i])
    else:
        pass
print("The odd numbers in a list are: " , odd_number)
print("#####################################################################\n")
# Reduce
# Again we will use numpy to vectorize a sum for us
print("The sum of the list provided is: " , np.sum(num_list))
print("#####################################################################\n")


# Q7
# Create a base class called account
# Account should have the following attributes: accountNumber and balance, which should be correctly initialized in the constructor (_ _init_ _) method for the class.
# Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” on the next line (example with account number of 1234 and balance of 2000).

class Account: # Defining the Account class
    def __init__(self , accountNumber , balance): # defining the constructor
        self.accountNumber = accountNumber
        self.balance = balance
        self.transaction = []

    def __str__(self):
        #"Your account number is: {}\nYour balance is: {}".format(self.accountNumber, self.balance)
        return "Your account number is: {}\nYour balance is: {}".format(self.accountNumber, self.balance)


startingAccount = Account('12345' , '2000')

# Create another class called CHECKING. This class should inherit from the Account class. Therefore, the Checking class is the derived class.
# In addition to the accountNumber and balance attributes, the Checking class has a fee attribute (that is used when withdrawing money from the Checking account). Initialize all variables correctly in the constructor (_ _init_ _) method.

class Checking(Account):
    def __init__(self , accountNumber , balance , fee):
        Account.__init__(self , accountNumber , balance)
        self.fee = fee

    def __str__(self):
        baseString = Account.__str__(self)
        return "The account type is Checking.\n{}".format(  baseString )


test2 = Checking('12345' , 30000 , 3)
print(test2)








































