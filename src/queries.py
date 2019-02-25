import pymysql

# connect with the database
db = pymysql.connect("localhost", "admin", "admin", "lms")
cursor = db.cursor()

# function to prettify the output obtained by using cursor.fetchall()
def pretty_print(cursor, data=None, rowlens=0):
    d = cursor.description
    if not d:
        print("#### NO RESULTS ###")
    names = []
    lengths = []
    rules = []
    if not data:
        data = cursor.fetchall(  )
    for dd in d:    # iterate over description
        l = dd[1]
        if not l:
            l = 12            # or default arg ...
        l = max(l, len(dd[0])) # Handle long names
        names.append(dd[0])
        lengths.append(l)
    for col in range(len(lengths)):
        if rowlens:
            rls = [len(row[col]) for row in data if row[col]]
            lengths[col] = max([lengths[col]]+rls)
        rules.append("-"*lengths[col])
    format = " ".join(["%%-%ss" % l for l in lengths])
    result = [format % tuple(names)]
    result.append(format % tuple(rules))
    for row in data:
        result.append(format % row)
    print("\n".join(result))

def list_all_tables_and_attributes(database_name):
	sql_query = "select * from information_schema.columns where table_schema = \'" + database_name + "\';"
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)
	
# list_all_tables_and_attributes('lms')

def total_inventory(table_name):
	sql_query = "select count(*) from " + table_name + ";"
	cursor.execute(sql_query)
	data = cursor.fetchone()
	pretty_print(cursor, data)

# total_inventory('Book')

def available_books(book_name):
	select = "select count(*) from Book "
	condition = "where title = \"" + book_name + "\";"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def author_of_book(book_name):
	select = "select Author.* from Author, Book_and_Author, Book "
	condition = """where Book_and_Author.book_id = Book.book_id and 
					Book_and_Author.author_id = Author.author_id and
					Book.title = \"""" + book_name + "\";" 
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def issued_books_by_user(user_name):
	select = "select count(*) from Book, User "
	condition = """where Book.user_id = User.user_id and
				   User.name = \"""" + user_name + "\";"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)
	return data[0][0]

def isssue_allowed(user_name):
	num_issued = issued_books_by_user(user_name)
	# calculate the maximum no of books allowed to be issued
	select = "select max_books from Issue_Capacity, User where "
	condition = """User.user_type = Issue_Capacity.user_type and 
					User.name = \"""" + user_name + "\";"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)
	if(len(data) != 0 and len(data[0]) != 0):
		max_allowed = data[0][0]
	else:
		max_allowed = 2
	# if (num_issued < max_allowed):
	# 	print("The user is allowed to issue another book!")
	# else:
	# 	print("The user is not allowed to issue another book!")
	sql_query = "select if (" + str(num_issued) + " < " + str(max_allowed) + ", \"Allowed to issue\", \"Not allowed to issue\");"
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def books_issued_stats(start_daytime, end_daytime):
	select = "select count(*) from Borrow_Book where "
	condition = "issue_time >= \"" + start_daytime + "\" and "
	condition += "(return_time <= \"" + end_daytime + "\""
	condition += "or return_time IS NULL);"
	sql_query = select + condition
	# print(sql_query)
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def users_with_dues():
	select = "select User.user_id, name from User, Borrow_Book where "
	condition = "User.user_id = Borrow_Book.user_id and due_amount > 0;"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def new_books(start_daytime, end_daytime):
	select = "select * from Book where "
	condition = "add_time >= \"" + start_daytime + "\" and "
	condition += "add_time <= \"" + end_daytime + "\";"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def display_issued_books_all():
	select = "select Book.user_id, User.name, book_id, title from Book, User where "
	condition = "User.user_id = Book.user_id;"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)

def display_issued_books_by_user(user_name):
	select = "select Book.* from Book, User where "
	condition = "User.user_id = Book.user_id and User.name = \"" + user_name + "\";"
	sql_query = select + condition
	cursor.execute(sql_query)
	data = cursor.fetchall()
	pretty_print(cursor, data)


print("============================================================================================")
print("Query 2: Displaying total inventory of books in the LMS")
total_inventory("Book")
print("============================================================================================")

print("Query 3: Listing the no. of available books requested by a user by book name")
available_books("The race agency")
print("============================================================================================")

print("Query 4:Listing the author(s) of a given book")
author_of_book("The race agency")
print("============================================================================================")

print("Query 5: Listing the total no. of books issued for a user by user name")
issued_books_by_user("Frank Hall")
print("============================================================================================")

print("Query 6: Checking whether a user is allowed to borrow a book or not")
isssue_allowed("Frank Hall")
print("============================================================================================")

print("Query 7: Listing the no. of books issued and returned on a daily basis (for a given day/period)")
books_issued_stats("2019-01-01 00:00:00", "2020-01-01 00:00:00")
print("============================================================================================")

print("Query 8: Listing the users with book details if there are any dues")
users_with_dues()
print("============================================================================================")

print("Query 9: Listing the newly added book records for a given period")
new_books("2018-01-01 00:00:00", "2019-01-01 00:00:00")
print("============================================================================================")

print("Query 10: Displaying the user name and the books issued to them")
display_issued_books_all()
print("============================================================================================")

print("Query 10: Displaying all the books with all the details issued to a user")
display_issued_books_by_user("Natalie Harris")
print("============================================================================================")