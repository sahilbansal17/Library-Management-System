from tkinter import *
from tkinter import ttk
import pymysql

class Book:
    def __init__(self, wind):
        self.wind = wind
        self.wind.title('Books')

        # every widget accepts the first argument as the root window name
    
        # LabelFrame is a container widget for complex window layouts
        frame = LabelFrame(self.wind, text='Add new record', bd=5)
        # grid method is used to organize widgets in a table like manner
        frame.grid(row=0, column=1)

        # Label is a display box where text/images can be placed
        Label(frame, text='Title:').grid(row=1, column=1)
        # Entry widget is used to accept single-line text strings from a user
        self.title = Entry(frame)
        self.title.grid(row=1, column=2)
        
        Label(frame, text='Year:').grid(row=2, column=1)
        self.year = Entry(frame)
        self.year.grid(row=2, column=2)

        # ttk module provides access to the Tk themed widget set
        ttk.Button(frame, text='Add Book').grid (row=3, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0)
        
        # use TreeView from ttk to display the table
        # height attribute gives the desired height of the widget in rows
        # columns is used to specify the string identifiers for the columns
        # the icon column with identifier '#0' is always the first column
        self.tree = ttk.Treeview(height=20, columns=(2, 3))
        self.tree.grid(row=4, column=0, columnspan=3)

        # modify the headings of the columns
        # first argument is the column id
        # text gives the column name
        # anchor is used for alignment within the column
        self.tree.heading('#0', text='Book ID', anchor=W)
        self.tree.heading(2, text='Title', anchor=W)
        self.tree.heading(3, text='Year', anchor=W)

        # modify the column sizes
        self.tree.column('#0', width=70)
        self.tree.column(2, width=200)
        self.tree.column(3, width=100)

        ttk.Button(text='Delete Book').grid (row=5, column=0)
        ttk.Button(text='Edit Book').grid(row=5, column=1)

        self.view_records()

    # run a mysql query 
    def run_query(self, query, parameters=()):
        db = pymysql.connect("localhost", "admin", "admin", "lms")
        cursor = db.cursor()
        cursor.execute(query, parameters)
        query_result = cursor.fetchall()
        return query_result

    # get the records from the table and display them
    def view_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT book_id, title, year FROM Book'
        db_rows = self.run_query(query)
        # print(db_rows)
        index = iid = 0
        for row in db_rows:
            # insert into the TreeView
            self.tree.insert('', index, iid, text=row[0], values=row[1:])
            index = iid = index + 1

if __name__ == '__main__':
    wind = Tk()
    books = Book(wind)
    wind.mainloop()
