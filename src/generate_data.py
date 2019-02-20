import pymysql
from faker import Faker 
import factory 

db = pymysql.connect("localhost", "sahilbansal", "iamalive", "lms")
cursor = db.cursor()
# cursor.execute("SELECT * FROM User")
# data = cursor.fetchall()
# print(data)

fake = Faker()
books = []
num_books = 100

def add_into_table(table_name, row):
	# table_name is the table name, row is the dictionary containing key and value mappings
	sql_query = "INSERT INTO " + table_name + " Values("
	for key in row.keys():
		if (row[key] == 'NULL'):
			sql_query += row[key]
		elif (type(row[key]) == str):
			sql_query += '\''
			sql_query += row[key]
			sql_query += '\''
		else:	
			sql_query += str(row[key])
		sql_query += ','
	sql_query = sql_query[:-1]
	sql_query += ');'
	# print(sql_query);
	try:
   		# Execute the SQL command
	   	cursor.execute(sql_query)
	   	# Commit your changes in the database
	   	db.commit()
	except:
   		# Rollback in case there is any error
   		db.rollback()

for i in range(num_books):
	id = i + 1
	title = fake.sentence(nb_words=3, variable_nb_words=False)
	title = title[:-1] # remove the dot at the last of the sentence
	year = int(fake.year())
	isbn = fake.isbn10()
	pages = fake.pyint()
	# user_id = 
	add_time = fake.date() + ' ' + fake.time()
	# issue_time = 
	# publisher_id = 
	books.append({
		'id':id, 
		'title': title, 
		'year': year, 
		'isbn': isbn, 
		'pages': pages, 
		'user_id': 'NULL', 
		'add_time': add_time, 
		'publisher_id': 'NULL', 
		'issue_time': 'NULL'
	})
	add_into_table('Book', books[i])
