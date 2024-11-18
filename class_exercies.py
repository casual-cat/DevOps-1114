class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

class Library:
    def __init__(self):
        self.books = []
    
def add_book(self, book):
    self.books.append(book)
    
def list_books(self):
    for book in self.books:
        print(book)

#method to find a book by the title in the library:
def find_book(self, title):
    for book in self.books:
        if book.title == title:
            return book
    return None

library = Library()
book = library.find_book("amit is a dumbahh")
if book:
    print(f"Book found: {book}")
else:
    print("Book not found")

#purpose of 'book' class: create a book object with title, author, and copies.
#purpose of 'library' class: create a library object with a list of books.
#purpose of 'add_book' method: add a book to the library.
#purpose of 'list_books' method: list all the books in the library. When books are added then they are printed out.