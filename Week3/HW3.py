# ID: jmc7dt
# Name: John Carpenter
# Class: CS 5010
# Homework #3

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


# Q3
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

#Q4 