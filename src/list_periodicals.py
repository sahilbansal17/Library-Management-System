try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pymysql
import sys

import list_books_support

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = ListPeriodical(root)
    list_books_support.init(root, top)
    root.mainloop()

w = None

def create_ListPeriodical(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = ListPeriodical(w)
    list_books_support.init(w, top, *args, **kwargs)
    destroy_ListPeriodical()
    return (w, top)

def destroy_ListPeriodical():
    global w
    w.destroy()
    w = None

class ListPeriodical:
    def __init__(self, top=None):
        top.title('Periodicals')

        # use TreeView from ttk to display the table
        # height attribute gives the desired height of the widget in rows
        # columns is used to specify the string identifiers for the columns
        # the icon column with identifier '#0' is always the first column
        columns = (2, 3, 4, 5, 6, 7, 8, 9)
        self.tree = ttk.Treeview(height=33, columns=columns)
        self.tree.grid(row=4, column=0, columnspan=9)

        headings = ['Title', 'Year', 'Volume', 'ISBN', 'User ID', 'Publisher ID', 'Add Time', 'Issue Time']
        col_sizes = [200, 70, 70, 120, 70, 100, 170, 200]
        head_count = 2
        for title, size in zip(headings, col_sizes):
            # modify the headings of the columns
            # first argument is the column id
            # text gives the column name
            # anchor is used for alignment within the column
            self.tree.heading(head_count, text=title, anchor=tk.W)
            # modify the column sizes
            self.tree.column(head_count, width=size)
            head_count = head_count + 1

        self.tree.heading('#0', text='Periodical ID', anchor=tk.W)
        self.tree.column('#0', width=100)

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
        query = 'SELECT * FROM Periodical'
        db_rows = self.run_query(query)
        # print(db_rows)
        index = iid = 0
        for row in db_rows:
            # insert into the TreeView
            self.tree.insert('', index, iid, text=row[0], values=row[1:])
            index = iid = index + 1

if __name__ == '__main__':
    vp_start_gui()
