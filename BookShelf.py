#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shruti Alavala
Intro to Python - Final Project
"""

from Book import Book

class BookShelf:
    """BookShelf class"""
    
    def __init__(self, owner, book_list):
        """Instantiate a BookShelf object"""
        self.__num_books = 0
        self.owner = owner
        self.book_list = list(book_list)
        
    def __repr__(self):
        """Representation of BookShelf object"""
        return (f'{self.owner}\'s bookshelf has a total of {self.__num_books} '
                f'books. These books are:\n{self.book_list}.')
    
    def addBookToShelf(self, other_book):
        """Public method to add a Book to the BookShelf"""
        
        #add Book to book_list attribute
        self.book_list.append(other_book)
        #increment private attribute for number of books in the BookShelf
        self.__num_books += 1
    
    def __author_counts(self):
        """
        Private method to return a dictionary where the key is an author and
        the value is the number of tracked books by that author.
        """
        
        author_dict = dict()
        
        for book in self.book_list:
            #if author is already a key, add 1 to existing count
            if book.author in author_dict.keys():
                author_dict[book.author] += 1
            #otherwise add author as a key and set count as 1
            else:
                author_dict[book.author] = 1
        
        return author_dict
            
    def most_tracked_author(self):
        """
        Public method that returns the author(s) that have the most tracked 
        books in the Bookshelf.
        """
        
        #sort the dictionary by value descending (highest first) and store 
        #key-value pairs in list of tuples 
        sorted_list = sorted(
            self.__author_counts().items(), key=lambda x: x[1], reverse=True)
        
        #highest count is at index 0 of sorted list and index 1 of the tuple
        highest_count = sorted_list[0][1]
        
        most_tracked_author_list = []
        
        #find all authors with the highest count and store these letters in 
        #separate list
        for i in range(len(sorted_list)):
            if sorted_list[0][1] == sorted_list[i][1]:
                most_tracked_author_list.append(sorted_list[i][0])
        
        return most_tracked_author_list, highest_count
        
    def genre_counts(self):
        """
        Public method that returns a dictionary where the key is a genre and
        the value is the number of tracked books in that genre.
        """
        
        genre_dict = dict()
        
        for book in self.book_list:
            #if genre is already a key, add 1 to existing count
            if book.genre in genre_dict.keys():
                genre_dict[book.genre] += 1
            #otherwise add genre as a key and set count as 1
            else:
                genre_dict[book.genre] = 1
        
        return genre_dict
    
    def status_counts(self):
        """
        Public method that returns a dictionary where the key is a status and
        the value is the number of tracked books in that status.
        """
        
        status_dict = dict()
        
        for book in self.book_list:
            #if status is already a key, add 1 to existing count
            if book.status in status_dict.keys():
                status_dict[book.status] += 1
            #otherwise add status as a key and set count as 1
            else:
                status_dict[book.status] = 1
        
        return status_dict
        
    def average_rating(self):
        """
        Public method that returns the average rating of books with status 
        of Read.
        """
        
        #initialize variables
        total_rating = 0
        count = 0
        
        for book in self.book_list:
            if book.status == "Read" and book.rating != 0:
                total_rating += book.rating
                count += 1
        
        #calculate the average, make sure not dividing by 0 in case of 
        #empty list
        try:
            avg = round(total_rating/count, 2)
        except ZeroDivisionError:
            return "Not Applicable"
        else: 
            return avg
    

if __name__ == "__main__":

    #instantiating Bookshelf object
    shelf1 = BookShelf("Shruti",[])
    assert shelf1.owner == "Shruti", "Owner should be Shruti"
    assert len(shelf1.book_list) == 0, \
        "Default number of books on the bookshelf is 0"

    #creating Book test data
    book1 = Book("Empire of Storms", "Sarah J. Maas", "Fantasy", "Read", 4)
    book2 = Book("Kingdom of Ash", "Sarah J. Maas", "Fantasy", "Read", 5)
    book3 = Book("Malibu Rising", "Taylor Jenkins Reid", "Contemporary", 
              "Currently Reading")
    book4 = Book("After I Do", "Taylor Jenkins Reid", "Contemporary", 
              "Want to Read")
    book5 = Book("Becoming", "Michelle Obama", "Non-Fiction", "Read", 5)
    
    #adding the test Books to the BookShelf object
    shelf1.addBookToShelf(book1)
    shelf1.addBookToShelf(book2)
    shelf1.addBookToShelf(book3)
    shelf1.addBookToShelf(book4)
    shelf1.addBookToShelf(book5)
    
    #check that all 5 books were added to the book_list
    assert len(shelf1.book_list) == 5, \
        "Number of books on bookshelf should be 5"    

    
    #testing most_tracked_author()
    author_list, count = shelf1.most_tracked_author()
    assert count == 2, \
        f'Highest number of books tracked by author should be 2, not {count}'
    assert len(author_list) == 2, \
        (f'Should be 2 authors in the most tracked authors list, ' 
         f'not {len(author_list)}')
    assert author_list == ['Sarah J. Maas', 'Taylor Jenkins Reid'], \
        (f'Most tracked authors should be Sarah J. Maas and '
         f'Taylor Jenkins Reid, not {author_list}')
    
    #testing counts by genre
    genre_dict = shelf1.genre_counts()
    assert genre_dict["Fantasy"] == 2, \
        f'Number of Fantasy books should be 2, not {genre_dict["Fantasy"]}'
    
    assert genre_dict["Contemporary"] == 2, \
        (f'Number of Contemporary books should be 2, '
         f'not {genre_dict["Contemporary"]}')
    
    assert genre_dict["Non-Fiction"] == 1, \
        (f'Number of Non-Fiction books should be 1, '
        f'not {genre_dict["Non-Fiction"]}')
    
    #testing counts by status
    status_dict = shelf1.status_counts()
    assert status_dict["Read"] == 3, \
        f'Number of Read books should be 3, not {status_dict["Read"]}'
    
    assert status_dict["Currently Reading"] == 1, \
        (f'Number of Currently Reading books should be 1, '
        f'not {status_dict["Currently Reading"]}')
    
    assert status_dict["Want to Read"] == 1, \
        (f'Number of Want to Read books should be 1, '
        f'not {status_dict["Want to Read"]}')
    
    #testing average_rating()
    assert shelf1.average_rating() == 4.67, \
        (f'Average rating of read books should be 4.67, '
        f'not {shelf1.average_rating()}')
    
    #testing if ZeroDivisionError is caught in average_rating()
    shelf2 = BookShelf("Sujay",[])
    shelf2.addBookToShelf(book4) #does not have a rating
    assert shelf2.average_rating() == "Not Applicable", \
        f'Should result in Not Applicable, not {shelf2.average_rating()}'
    