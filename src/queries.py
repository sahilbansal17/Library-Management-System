import pymysql

db = pymysql.connect("localhost", "sahilbansal", "iamalive", "lms")
cursor = db.cursor()

def list_all_tables_and_attributes(database_name):
	sql_query = "select * from information_schema.columns where table_schema = \'" + database_name + "\';"
	cursor.execute(sql_query)
	data = cursor.fetchall()
	print(data)
	
# list_all_tables_and_attributes('lms')

def total_inventory(table_name):
	sql_query = "select count(*) from " + table_name + ";"
	cursor.execute(sql_query)
	data = cursor.fetchone()
	print(data)

# total_inventory('Book')

# def available_books():


def author_of_book(book_name):
	select = "select Author.author_id, name from Author, Book_and_Author, Book "
	condition = """where Book_and_Author.book_id = Book.book_id and 
					Book_and_Author.author_id = Author.author_id and
					Book.title = \"""" + book_name + "\";" 
	sql_query = select + condition
	print(sql_query)

author_of_book("Begin education choose")

# def num_of_books_issued(user_name):
	