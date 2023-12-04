# Pratical Task 3
# Let's get going

class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        my_book = ""
        my_book += f"ISBN: {self.isbn}\n"
        my_book += f"Title: {self.title}\n"
        my_book += f"Author: {self.author}\n"
        my_book += f"Price: ${self.price:.2f}\n"
        my_book += "\n"
        return my_book