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

class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Book Database")

        label1 = Label(window, text = "Title")
        label1.grid(row=0, column=0)

        label2 = Label(window, text = "Author")
        label2.grid(row=0, column=2)

        label3 = Label(window, text = "Year")
        label3.grid(row=1, column=0)

        label4 = Label(window, text = "ISBN")
        label4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.entry1 = Entry(window, textvariable = self.title_text)
        self.entry1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.entry2 = Entry(window, textvariable = self.author_text)
        self.entry2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.entry3 = Entry(window, textvariable = self.year_text)
        self.entry3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.entry4 = Entry(window, textvariable = self.isbn_text)
        self.entry4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        scroll1 = Scrollbar(window)
        scroll1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand = scroll1.set)
        scroll1.configure(command = self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add Book", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update Book", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete Book", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.entry1.delete(0, END)
            self.entry1.insert(END, self.selected_tuple[1])
            self.entry2.delete(0, END)
            self.entry2.insert(END, self.selected_tuple[2])
            self.entry3.delete(0, END)
            self.entry3.insert(END, self.selected_tuple[3])
            self.entry4.delete(0, END)
            self.entry4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

window = Tk()
Window(window)
window.mainloop()