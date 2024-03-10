# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk

# Dosyadan kitapları yükleyen fonksiyon
def load_books():
    try:
        with open("books.txt", "r") as file:
            for book in file:
                listbox.insert(tk.END, book.strip())
    except FileNotFoundError:
        pass  # Dosya yoksa, herhangi bir şey yapmaya gerek yok

# Kitapları dosyaya kaydeden fonksiyon
def save_books():
    with open("books.txt", "w") as file:
        books = listbox.get(0, tk.END)
        for book in books:
            file.write(book + "\n")

# Functions
def add_book():
    book = entry.get()
    if book:
        listbox.insert(tk.END, book)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Book name cannot be empty!")

def remove_book():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a book to remove!")

def show_books():
    books = "\n".join(listbox.get(0, tk.END))
    messagebox.showinfo("Books List", books if books else "No books added yet.")

# Main window
root = tk.Tk()
root.title("Book Manager")
root.geometry("600x450")
root.resizable(False, False)

# Program kapatıldığında kitapları kaydet
root.protocol("WM_DELETE_WINDOW", lambda: (save_books(), root.destroy()))

# Frames
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# Widget
entry_label = tk.Label(top_frame, text="Book Name:", font=("Arial", 12))
entry_label.pack(side=tk.LEFT, padx=5)
entry = tk.Entry(top_frame, font=("Arial", 12), width=20)
entry.pack(side=tk.LEFT, padx=5)

# Buttons
add_button = tk.Button(bottom_frame, text="Add Book", command=add_book, font=("Arial", 10), width=10)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(bottom_frame, text="Remove Book", command=remove_book, font=("Arial", 10), width=10)
remove_button.pack(side=tk.LEFT, padx=5)

show_button = tk.Button(bottom_frame, text="Show Books", command=show_books, font=("Arial", 10), width=10)
show_button.pack(side=tk.LEFT, padx=5)

# Listbox and Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(list_frame, width=50, height=6, font=("Arial", 12), yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Başlangıçta kitapları yükle
load_books()

# Start GUI
root.mainloop()
