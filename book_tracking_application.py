#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shruti Alavala
Intro to Python - Final Project
"""

import csv
from Book import Book
from BookShelf import BookShelf


def track_single_book(bookshelf, genre_tuple, status_tuple):
    """
    Prompts the user to input title, author, genre, status and rating of a book.
    Once all inputs are valid Book gets added to BookShelf.
    """
    
    in_title = input("Enter the title: ")
    in_author = input("Enter the author: ")
    
    #prompt user to input the genre of the book and make sure it is an 
    #accepted genre 
    while(True):
        in_genre = input(f'What is the genre? Choose one of the options: '
                         f'\n{genre_tuple}\n')
        if(in_genre in genre_tuple):
            break
        else:
            print(f'{in_genre} is not one of the choices, please try again.')
    
    #prompt user to input the status of the book and make sure it is an 
    #accepted status        
    while(True):
        in_status = input(f'What is the status? Choose one of the options: '
                          f'\n{status_tuple}\n')
        if(in_status in status_tuple):
            break
        else:
            print(f'{in_status} is not one of the choices, please try again.')
    
    #prompt user for rating only if book is "Read"
    if(in_status == "Read"):
        
        while(True):
            in_rating_str = input("What is your rating, from 1 to 5: ")
            try:  
                in_rating = float(in_rating_str)
                if in_rating not in range(1,6):
                    print(f'{in_rating} is not a whole number between 1 and 5')
                    continue
            except ValueError:
                print(f'{in_rating_str} is not an integer from 1 to 5')
            else:
                #instantiate Book with all 5 attributes
                book = Book(in_title, in_author, in_genre, in_status, in_rating)
                break     
    else:
        #instantiate Book with 4 attributes, rating will be default
        book = Book(in_title, in_author, in_genre, in_status)
    
    bookshelf.addBookToShelf(book)
    
def track_multiple_books(input_file_name, bookshelf, genre_tuple, status_tuple):
    """
    Creates multiple Books by extracting data from a CSV. If data is not valid
    then that book is skipped. Adds all valid Books to the Bookshelf. 
    """
    
    #open input file in read mode
    with open(input_file_name, mode='r', encoding="utf-8") as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')
        line_count = 0
        
        #iterate through each row in file
        for row in csv_reader:
            #skip the header
            if line_count == 0:
                line_count += 1
            else:
                
                #make sure genre is valid
                if row[2] not in genre_tuple:
                    print(f'{row[0]}\'s genre is not an accepted genre. '
                          f'It will not be added to your bookshelf.')
                    continue
                #make sure status is valid
                elif row[3] not in status_tuple:
                    print(f'{row[0]}\'s status is not an accepted status. '
                          f'It will not be added to your bookshelf.')
                    continue
               
                #if status is Read then get rating, make sure rating is valid
                if row[3] == "Read":
                    try:
                        float_rating = float(row[4])
                        if float_rating not in range(1,6):
                            print(f'{row[0]}\'s rating is not a whole number '
                                  f'between 1 and 5. It will not be added to '
                                  f'your bookshelf.')
                            continue
                    except ValueError:
                        print(f'{row[0]}\'s rating is not a number. '
                              f'It will not be added to your bookshelf.')
                        continue
                    else:
                        #instantiate Book with all 5 attributes
                        book = Book(row[0], row[1], row[2], row[3], float_rating)
                else:
                    #instantiate Book with 4 attributes, rating will be default
                    book = Book(row[0], row[1], row[2], row[3])
                    
                #add Book to BookShelf
                bookshelf.addBookToShelf(book)
                line_count += 1
                    
    #close input file after reading all the data    
    input_file.close()
        
    

if __name__ == "__main__":
    
    #valid options for genre
    genre_tuple = ("Fantasy", "Romance", "Contemporary", "Science Fiction", 
                   "Mystery", "Historical", "Non-Fiction")
    
    #valid options for status
    status_tuple = ("Want to Read", "Currently Reading", "Read")
    
    print("Welcome to your personal Book Tracking Application!")
    
    in_owner = input("What is your name? ")
    
    #instantiate BookShelf with empty book_list
    bookshelf = BookShelf(in_owner,[])
    
    #keep prompting user with tracking options
    while(True):
        print("\n")
        print("----------------------------------------------------")
        print("\n")
        #menu of tracking options
        print("Enter 1 to Track a Single Book.")
        print("Enter 2 to Track Multiple Books Via CSV")
        print("Enter 3 if Done Tracking")
        in_choice = input("What would you like to do? ")
        
        #call appropriate method based on user tracking choice
        if in_choice == "1":
            track_single_book(bookshelf, genre_tuple, status_tuple)
            continue
        
        elif in_choice == "2":
            
            print("\nFormat of data in CSV must be: ")
            print("Title, Author, Genre, Status, Rating(optional field)\n")
            input_file_name = input(
                "What is the name of the file with books to track? ")
            
            #make sure given file is accessible
            try:
                input_file = open(input_file_name, "r")
            except IOError: 
                print(f'{input_file_name} not found, please try again.')
            except Exception as e:
                print(f'Error opening {input_file_name}, please try again. {e}')
            else:
                input_file.close()
                track_multiple_books(input_file_name, bookshelf, 
                                     genre_tuple, status_tuple)
                continue
        
        elif in_choice == "3":
            print("\n")
            break
        else:
            print(f'{in_choice} is not one of the tracking choices, '
                f'please try again.')
    
    #once user is done tracking books, print out the stats
    if bookshelf._BookShelf__num_books != 0:
        print(f'Let\'s analyze {bookshelf.owner}\'s bookshelf!\n')
        
        print(f'Total Number of Books Tracked: {bookshelf._BookShelf__num_books}\n')
        
        author_list, author_count = bookshelf.most_tracked_author()
        print(f'Your most tracked author(s) are: {author_list}. You have tracked '
              f'{author_count} books by them.\n')
        
        print("Number of books by Status")
        print("-------------------------")
        for status, status_count in bookshelf.status_counts().items():
            print(f'{status:21} {status_count:>3}')
        print("\n")
        
        print("Number of books by Genre")
        print("-------------------------")
        for genre, genre_count in bookshelf.genre_counts().items():
            print(f'{genre:21} {genre_count:>3}')
        print("\n")
        
        
        print(f'Average Rating of Read Books: {bookshelf.average_rating()}')
    else:
        print(f'No books were added to {bookshelf.owner}\'s bookshelf.')
    
    

    