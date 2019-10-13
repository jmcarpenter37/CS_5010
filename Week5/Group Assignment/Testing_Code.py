#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Testing another Group's Code

Omkar Kharkar (ogk3u)
Celeste Lemrow (ctl7t)
Maria Arango-Mesa (mca8y)
John Carpenter (jmc7dt)
Gavin Wiehl (gtw4vx)

"""
import unittest

from Mod_5_debugging_unit_test import BookLoverD 

class BookLoverTest(unittest.TestCase):
    
    """
    Initializes several objects for use in testing the unit tests
    """
    def __init__(self, *args, **kwargs):
        super(BookLoverTest, self).__init__(*args, **kwargs)
        self.bob1 = BookLoverD("Bob", "bob@gmail.com", "Fiction")
        self.bob2 = BookLoverD("Bob", "bob@gmail.com", "Fiction", 2)
        self.mary = BookLoverD("Mary", "Mary@gmail.com", "Horror", 2, [("The Catcher in the Rye", 3.5), ("The Grapes of Wrath", 4)])
        self.katy = BookLoverD("Katy", "Katy@gmail.com", "Horror", 2, [("IT", 3), ("The Mist", 2.85)])

    """
    Two cases are tested for addbook. 
    Case 1 - the book is not present, in which case, it should match the last element of list
    Case 2 - the book is present, in which case, the book should not be added

    """         
    def test_addBook_NotPresent(self):
        book = "The Great Gatsby"
        rating = 3.75
        self.mary.addBook(book, rating)
        self.assertEqual((book, rating), self.mary.bookLst[-1])   
    
    def test_addBook_Present(self):
        bookname = "The Grapes of Wrath"
        test_list = [x[0] for x in self.mary.bookLst]
        val = self.assertTrue(bookname in test_list)
        val2 = self.mary.addBook("The Grapes of Wrath", 3.5)
        self.assertNotEqual(val, val2)        
   
    """
    Two cases are tested for numBooksRead:
    
    Case 1 - If the books read is greater than 0, return the value'
    Case 2 - If the books is equal to 0 or missing, return 0.    

    """     
        
    def test_numBooksRead_gt_0(self):
        val = self.bob2.numBooks
        self.assertEqual(val, self.bob2.numBooks)
    
    def test_numBooksRead_eq_0(self):
        val = self.bob1.numBooks
        self.assertEqual(0, val)
    
    """
    Two cases are tested for hasRead:
       
        Case 1 - If the book has been read, then return true
        Case 2 - If the book has not been read, then return false     
   """
    
    def test_hasRead_Present(self):
        val = "The Grapes of Wrath"
        self.assertTrue(self.mary.hasRead(val))
    
    def test_hasRead_NotPresent(self):
        val = "The Adventures of Tom Sawyer"
        self.assertFalse(self.mary.hasRead(val))       
    
    """
    Two cases are tested for favorite Books:
        
    Case 1 - If there are no books greater than or equal to 3, then return an empty list 
    Case 2 - If there are books greater than 3, then return the list sorted by the second
    element of the tuple, so that the highest rated books are at the top of the list.
        
    """
        
    def test_favBooks_rating_lt_3(self):
        self.assertEqual([], self.katy.favBooks())
                
    def test_favBooks_rating_ge_3(self):
        fav_book_list = [("The Grapes of Wrath", 4), ("The Catcher in the Rye", 3.5)]
        self.assertEqual(fav_book_list, self.mary.favBooks())
        
            
if __name__ == '__main__':
    unittest.main() 
