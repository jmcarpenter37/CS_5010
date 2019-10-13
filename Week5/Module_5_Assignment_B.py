#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Name: John Carpenter
# ID: jmc7dt
# Assignment: Module 5 - Live Session Assignment (with Bugs)
# Group: Omkar Kharkaro
Celeste Lemrow ctl7t
John Carpenter jmc7dt
Gavin Wiehl gtw4vx
Maria Arango mca8y

"""

class BookLover:
    
    def __init__(self, name, email, favGenre, numBooks=None, bookLst=None):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        if numBooks is None:
            numBooks = 0
        else:
            self.numBooks = numBooks
        if bookLst is None:
            bookLst = []
        else:
            bookLst = bookLst
        return

         
    def __str__(self):
        print("The person's name is " + str(self.name))
        print("The list of books read and ratings, respectively, are: ")
        for x in self.bookLst:
            print(str(x[0]) + " : " + str(x[1]))
        return
    
    def addBook(self, bookName, rating):
        bookname_list = [z[0] for z in self.bookLst]
        if bookName in bookname_list:
            print("Already read!")
            return False
        else:
            self.bookLst.append(tuple(bookName, rating))
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
            return sorted(rating_list, key = lambda z: z[1], reverse=True)
        
        





























