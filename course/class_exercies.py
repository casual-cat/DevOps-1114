# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
    
# def __str__(self):
#     return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

# class Library:
#     def __init__(self):
#         self.books = []
    
# def add_book(self, book):
#     self.books.append(book)
    
# def list_books(self):
#     for book in self.books:
#         print(book)

# #method to find a book by the title in the library:
# def find_book(self, title):
#     for book in self.books:
#         if book.title == title:
#             return book
#     return None

# library = Library()
# book = library.find_book("amit is a dumbahh")
# if book:
#     print(f"Book found: {book}")
# else:
#     print("Book not found")

# #purpose of 'book' class: create a book object with title, author, and copies.
# #purpose of 'library' class: create a library object with a list of books.
# #purpose of 'add_book' method: add a book to the library.
# #purpose of 'list_books' method: list all the books in the library. When books are added then they are printed out.

# class cars:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def display_info(self):
#         return f"cars maker: {self.make}, model: {self.model}, created on: {self.year}."
    
#     def update_year(self, new_year):
#         self.year = new_year
    
#     def update_model(self, new_model):
#         self.model = new_model
    
# car1 = cars("mazda", "2", "2016")
# print(car1.display_info())
# car2 = cars("mazda", "3", "2017")
# print(car2.display_info())

class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        return f"Item name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"
    
class Shop:
    def __init__(self):
        self.inventory = []
        
    def add_new_item(self, new_item):
        self.inventory.append(new_item)
    
    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                break
            
    def update_item(self, item_name, new_quantity):
        for item in self.inventory:
            if item.name == item_name:
                item.quantity = new_quantity
                break 
        
item1 = Inventory("Bamba", "3 shekels", "25")
item2 = Inventory("chips", "4 shekels", "53")
print(item1.display_info())

shop = Shop()
shop.add_new_item(item1)
shop.update_item("Bamba", "30")
print(item1.display_info())

        
        

        

        