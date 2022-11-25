# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:42:22 2022

@author: elect
"""

class Book:
    def __init__(self, strBookName, strBookAuthor, intBookPrice, intDatePublished):
        self.__strBookName = strBookName;
        self.__strBookAuthor = strBookAuthor;
        self.__intBookPrice = intBookPrice;
        self.__intDatePublished = intDatePublished
        self.addBook()
    
    def addBook(self):
        print("--BOOK INFO BEGIN--")
        print("Name:            " + self.__strBookName)
        print("Author(s):       " + self.__strBookAuthor)
        print("Price:           $" + str(self.__intBookPrice))
        print("First Published: " + str(self.__intDatePublished))
        print("---BOOK INFO END---")
        print("Book Added.")

bookHarryPotterBook1 = Book("Harry Potter and the Philosopher's Stone", "JK Rowling", 10, 1997)
bookHarryPotterBook2 = Book("Harry Potter and the Chamber of Secrets", "JK Rowling", 10, 1998)
bookHarryPotterBook3 = Book("Harry Potter and the Prisoner of Azkaban", "JK Rowling", 10, 1999)
bookHarryPotterBook4 = Book("Harry Potter and the Goblet of Fire", "JK Rowling", 10, 2000)
bookHarryPotterBook5 = Book("Harry Potter and the Order of the Phoenix", "JK Rowling", 10, 2003)
bookHarryPotterBook6 = Book("Harry Potter and the Half-Blood Prince", "JK Rowling", 10, 2005)
bookHarryPotterBook7 = Book("Harry Potter and the Deathly Hallows", "JK Rowling", 10, 2007)
bookHarryPotterBook8 = Book("Harry Potter and the Cursed Child", "Jack Thorne, JK Rowling", 10, 2016)