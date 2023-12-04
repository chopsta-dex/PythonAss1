# Catalog

from Book import Book

import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()
application_window.withdraw()

catalog = []

def main_menu():
    selection = simpledialog.askinteger("Book Catalog", "-- Holmesglen Book Store --\n\n" +
                            "1. Add a book\n" +
                            "2. Sort and display books by price\n" +
                            "3. Search for a book by title\n" +
                            "4. Delete a book\n" +
                            "5. Display all books\n" +
                            "6. Exit\n\n" +
                            "Enter a menu choice:",
                            minvalue=1, maxvalue=6)

def ask_for_book():
    isbn = simpledialog.askstring("Book Catalog", "What is this book's ISBN?")
    title = simpledialog.askstring("Book Catalog", "What is the title of this book?")
    author = simpledialog.askstring("Book Catalog", "Who is the author of this book?")
    price = simpledialog.askfloat("Book Catalog", "How much does this book cost?")
    new_book = Book(isbn=isbn, title=title, author=author, price=price)
    return new_book

def startup():
    global catalog
    book1 = Book(isbn="0553296981", title="The Diary of a Young Girl", author="Frank, Anne", price=16.50)
    book2 = Book(isbn="1400082773", title="Dreams from My Father", author="Obama, Barrack", price=24.99)
    catalog.append(book1)
    catalog.append(book2)

    main_menu()

def add_book(new_book):
    global catalog
    catalog.append(new_book)

def show_catalog():
    global catalog
    if catalog == []:
        popup = tk.Tk()
        popup.title("Book Catalog")
        label = tk.Label(text="There are no books in the catalog")
        label.pack()
    else:
        catalog.sort(key=lambda x: x.price)
        popup = tk.Tk()
        popup.title("Book Catalog")
        label = tk.Label(text=catalog)
        label.pack()

startup()

show_catalog()
