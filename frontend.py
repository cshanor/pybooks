"""
Written by Ardit Sulce
modified by Christopher Shanor

A program that stores this book information:
Title, Author
Year Published, ISBN

User stories:
View all records
Search records
Add record
Update record
Delete record
Close application
"""

from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()

window.wm_title("Book Database")

label1 = Label(window, text = "Title")
label1.grid(row=0, column=0)

label2 = Label(window, text = "Author")
label2.grid(row=0, column=2)

label3 = Label(window, text = "Year")
label3.grid(row=1, column=0)

label4 = Label(window, text = "ISBN")
label4.grid(row=1, column=2)

title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll1 = Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = scroll1.set)
scroll1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Book", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Book", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Book", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()