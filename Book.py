#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shruti Alavala
Intro to Python - Final Project
"""

class Book:
    """Book class"""
    
    def __init__(self, title, author, genre, status, rating=0):
        """Instantiate Book object with 5 attributes"""
        
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.rating = rating
    
    def __repr__(self):
        """Representation of Book object"""
        return (f'{self.title} written by {self.author} is a {self.genre} '
                f'book categorized as {self.status} with a rating of '
                f'{self.rating}.\n')
    
if __name__ ==  "__main__":
    
    #testing instantiation of book objects
    b1 = Book("Empire of Storms", "Sarah J. Maas", "Fantasy", "Read", 5)
    print(b1)
    assert b1.title == "Empire of Storms", "Title should be Empire of Storms"
    assert b1.author == "Sarah J. Maas", "Author should be Sarah J. Maas"
    assert b1.genre == "Fantasy", "Genre should be Fantasy"
    assert b1.status == "Read", "Status should be Read"
    assert b1.rating == 5, "Rating should be 5"
    
    b2 = Book("Malibu Rising", "Taylor Jenkins Reid", "Contemporary", 
              "Want to Read")
    print(b2)
    assert b2.title == "Malibu Rising", "Title should be Malibu Rising"
    assert b2.author == "Taylor Jenkins Reid", ("Author should be "
                                                "Taylor Jenkins Reid")
    assert b2.genre == "Contemporary", "Genre should be Contemporary"
    assert b2.status == "Want to Read", "Status should be Want to Read"
    assert b2.rating == 0, "Rating should be 0"
    
    
    


