#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Module 5 - Live Session Assignment

Created on Wed Sep 25 19:06:10 2019

"""

# Part 1 - Writing the Code

class BookLover:
    
    def __init__(self, name, email, favGenre, numBooks=0, bookLst=[]):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = 0
        self.bookLst = [] # list of tuples
        return
     
# Can someone check if the optional fields above are marked correctly ?
    
    def __str__(self):
        print("The person's name is " + str(self.name))
        print("The list of books read and ratings, respectively, are: ")
        for x in self.bookList:
            print(x[0] + " : " + x[1])
        return
    
    def addBook(self, bookName, rating):
        bookname_list = [z[0] for z in self.bookLst]
        if bookName in bookname_list:
            print("Already read!")
            return False
        else:
            self.bookList.append(tuple(bookName, rating))
        return True
    
    def hasRead(self, bookName):
        bookname_list = [z[0] for z in self.bookLst]
        if bookName in bookname_list:
            print("Already read!")
            return True
        else:
            return False
        
    def numBooksRead(self):
        return self.numBooks
    
    def favBooks(self):
        rating_list = [z for z in self.bookLst if z[1] > 3]
        if not rating_list:
            print("There are no favorite books yet. Check back later.")
            return []
        else:
            return sorted(rating_list, key = lambda z: z[1])
        
        
# Part 2 - Writing the Unit Tests
def test_addBook(self):
    bookname = "The Grapes of Wrath"
    val = self.assertIn(bookname, [x[0] for x in self.mary.bookLst])
    self.assertEqual(val, self.mary.addBook("The Grapes of Wrath", 3.5))

import unittest
test_list = [("The Catcher in the Rye", 3.5), ("The Grapes of Wrath", 4)]

print(title_list)


mary = BookLover("Mary", "Mary@gmail.com", "Horror", 2, [("The Catcher in the Rye", 3.5), ("The Grapes of Wrath", 4)])

bookname = "The Grapes of Wrath"
test_list = [x[0] for x in mary.bookLst]
test_list
val = unittest.TestCase.assertIn(bookname, test_list)
print(val)
# TypeError: assertIn() missing 1 required positional argument: 'container'
































