#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Module 5 - Live Session Assignment

Omkar Kharkar (ogk3u)
Celeste Lemrow (ctl7t)
Maria Arango-Mesa (mca8y)
John Carpenter (jmc7dt)
Gavin Wiehl (gtw4vx)

"""

# Part 1 - Writing the Code

class BookLover:
    """
    Initializes the constructor
    """
    def __init__(self, name, email, favGenre, numBooks=None, bookLst=None):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        if numBooks is None:
            self.numBooks = 0
        else:
            self.numBooks = numBooks
        if bookLst is None:
            self.bookLst = []
        else:
            self.bookLst = bookLst
        return

    """
    Prints the string message, using the person's name and ratings.
    
    """
    def __str__(self):
        print("The person's name is " + str(self.name))
        print("The list of books read and ratings, respectively, are: ")
        for x in self.bookLst:
            print(str(x[0]) + " : " + str(x[1]))
        return
    
    """ 
    Adds a book to bookLst; if the book already exists, then don't
    add the book. 
     
    """    
    def addBook(self, bookName, rating):
        bookname_list = [z[0] for z in self.bookLst]
        if bookName in bookname_list:
            print("Already read!")
            return False
        else:
            self.bookLst.append((bookName, rating))
        return True
    
    """
    Checks if a book has been read already. If it has, returns a boolean
    value of True. Otherwise, it returns false.
    
    """
    
    def hasRead(self, bookName):
        bookname_list = [z[0] for z in self.bookLst]
        if bookName in bookname_list:
            print("Already read!")
            return True
        else:
            return False
        
    """
    Checks the number of books that have been read by a person.

    """    
    def numBooksRead(self):
        return self.numBooks
    
    """
    Checks the favorite books for a person. This is defined as having a 
    rating greater than 3 or else, returns an empty list.
    
    """
    def favBooks(self):
        rating_list = [z for z in self.bookLst if z[1] > 3]
        if not rating_list:
            print("There are no favorite books yet. Check back later.")
            return []
        else:
            return sorted(rating_list, key = lambda z: z[1], reverse=True)
        
        





























