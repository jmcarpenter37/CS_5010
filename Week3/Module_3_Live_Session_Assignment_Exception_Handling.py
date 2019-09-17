
"""
Name of Activity: Module 3 Live Session Assignment: Exception Handling
Name: John Carpenter
Computing ID: jmc7dt

Partner: John Carpenter
Partner Computing ID: John Carpenter
"""
"""
#1 Because the FileNotFoundError is a subclass of an IOError and the IOError exception statement
was called before the FileNotFoundError the IOError exception statement caught the file name error rather than
FileNotFoundError
"""
"""
#2
"""

try:
    name = input("Enter the name of a file: ")
    file = open(name, 'r')  # try to open this file for reading
    num = int(input("Enter a number: ")) #  Entering John throws a ValueError
    num2 = input("Enter a number to add to num: ")# Entering 2 (without casting as an int first) throws TypeError
    sum_output = num + num2
    print(str(sum_output))
    numer = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: ")) # Entering 0 throws ZeroDivisionError
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
except FileNotFoundError:   # specifically for file errors [BEFORE IOError!]
   print("** FileNotFoundError >> Cannot open file! **")
   name = input("Enter the name of a file to open: ") # w2filegrades.txt
except TypeError:
    print("** TypeError >> Cannot add two variables of different types! **")
    num2 = int(input("Enter a number to add to num: "))
    sum_output = num + num2
    print(str(sum_output))
except ValueError:
    print("** ValueError >> Cannot enter non-int type! **")
    num = input("Enter a number: ")
except IOError:  # for general IO errors
    print("** You caught a general IOError! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')
except ZeroDivisionError:  # for divide by zero error
    print("** Cannot divide by zero! **")
    denom = int(input("Enter a non-zero denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
except ArithmeticError: # for general Arithmetic errors
    print("** You caught a general Arithmetic Error! **")
    denom = int(input("Enter a non-zero denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
except Exception:
    print("** You caught a general Exception! **")
finally:
    print("I'm in finally!")
    file.close()   # do this no matter what else is happening in the program
    
#/Users/nathanengland/Public/UVA DSI/CS 5010/Module 2/newton.py
