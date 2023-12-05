# Catalog

from Book import Book

from functools import partial

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

catalog = []
exit_all = False
selection = None

def main_menu():
    global selection
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

def add_book(new_book):
    global catalog
    catalog.append(new_book)
    popup = tk.Tk()
    popup_text = "Book successfully added"
    label = tk.Label(text=popup_text)

    def close_popup():
        popup.destroy()

    close_button = tk.Button(popup, text="Okay", command=close_popup)

    label.pack()
    close_button.pack()
    popup.mainloop()

def show_catalog():
    global catalog
    popup = tk.Tk()

    def close_popup():
        popup.destroy()

    close_button = tk.Button(popup, text="Okay", command=close_popup)

    if catalog == []:
        popup.title("Book Catalog")
        label = tk.Label(text="There are no books in the catalog")
        label.pack()
        close_button.pack()
        popup.mainloop()
    else:
        catalog.sort(key=lambda x: x.price)
        popup_text = ""
        for item in catalog:
            popup_text += item.display()

        popup.title("Book Catalog")
        label = tk.Label(text=popup_text)
        label.pack()
        close_button.pack()
    popup.mainloop()

def search():
    global catalog
    search_value = simpledialog.askstring("Book Catalog", "What book are you looking for?\n\nEnter your search term(s) here:")
    popup_title = "Search results:"
    popup_text = ""
    for item in catalog:
        if search_value in item.title:
            popup_text += item.display()
    if popup_text == "":
        popup_title = "No books found."
    
    popup = tk.Tk()
    label = tk.Label(text=popup_text)
    title = tk.Label(text=popup_title)
    def close_popup():
        popup.destroy()
    close_button = tk.Button(popup, text="Okay", command=close_popup)
    title.pack()
    label.pack()
    close_button.pack()
    popup.mainloop()


def delete_book():
    global catalog
    found = False

    del_isbn = simpledialog.askstring("Book Catalog", "Enter the ISBN of the book you would like to delete:")

    for item in catalog:
        if del_isbn == item.isbn:
            found = True
            book_string = item.display()
            book_string += "Are you sure you want to delete this book?"
            answer = messagebox.askyesno("Book Catalog", book_string)
            if answer:
                catalog.remove(item)
                messagebox.showinfo("Book Catalog", "Book has been deleted")
            else:
                messagebox.showinfo("Book Catalog", "Book has not been deleted")
            
            break
    if not found:
        messagebox.showinfo("Book Catalog", "No such book was found")

def display_all():
    global catalog
    if catalog == []:
        messagebox.showinfo
    else:
        popup = tk.Tk()
        popup_text = ""
        for item in catalog:
            popup_text += item.display()

        popup.title("Book Catalog")
        label = tk.Label(text=popup_text)
        label.pack()
        close_button = tk.Button(popup, text="Okay", command=popup.destroy)
        close_button.pack()
        popup.mainloop()

def exit_program():
    global exit_all
    exit_all = True


# Here is the program
startup()
while not exit_all:
    main_menu()
    if selection == 1:
        add_book(ask_for_book())
        continue
    elif selection == 2:
        show_catalog()
        continue
    elif selection == 3:
        search()
        continue
    elif selection == 4:
        delete_book()
        continue
    elif selection == 5:
        display_all()
        continue
    elif selection == 6:
        exit_program()

messagebox.showinfo("Book Catalog", "The program will now exit")