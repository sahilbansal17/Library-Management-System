import pymysql
from faker import Faker 
import factory 
import random 

db = pymysql.connect("localhost", "sahilbansal", "iamalive", "lms")
cursor = db.cursor()
# cursor.execute("SELECT * FROM User")
# data = cursor.fetchall()
# print(data)

fake = Faker()

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

books = []
num_books = 100
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

users = []
num_users = 100
user_types = ['Student', 'Faculty', 'Staff', 'Guest']

for i in range(num_users):
	id = i + 1
	name = fake.name()
	username = fake.user_name()
	password = fake.password()
	email = fake.ascii_email()
	pages = fake.pyint()
	user_type = random.randint(0, 3)
	user_type = user_types[user_type]
	users.append({
		'id':id, 
		'name': name, 
		'username': username, 
		'password': password, 
		'email': email, 
		'user_type': user_type
	})
	add_into_table('User', users[i])

periodicals = []
num_periodicals = 100
for i in range(num_periodicals):
	id = i + 1
	title = fake.sentence(nb_words=3, variable_nb_words=False)
	title = title[:-1] # remove the dot at the last of the sentence
	year = int(fake.year())
	isbn = fake.isbn10()
	volume = random.randint(0, 10)
	# user_id = 
	add_time = fake.date() + ' ' + fake.time()
	# issue_time = 
	# publisher_id = 
	periodicals.append({
		'id':id, 
		'title': title, 
		'year': year,
		'volume': volume, 
		'isbn': isbn, 
		'user_id': 'NULL',  
		'publisher_id': 'NULL',
		'add_time': add_time, 
		'issue_time': 'NULL'
	})
	add_into_table('Periodical', periodicals[i])

authors = []
num_authors = 100
for i in range(num_authors):
	id = i + 1
	name = fake.name()
	authors.append({
		'id': id,
		'name': name
	})
	add_into_table('Author', authors[i])

publishers = []
num_publishers = 100
for i in range(num_publishers):
	id = i + 1
	name = fake.company()
	publishers.append({
		'id': id,
		'name': name
	})
	add_into_table('Publisher', publishers[i])

papers = []
num_papers = 100
for i in range(num_papers):
	id = i + 1
	name = fake.sentence()
	name = name[:-1]
	# periodical_id = 
	papers.append({
		'id': id,
		'name': name,
		'periodical_id': 'NULL'
	})
	add_into_table('Paper', papers[i])
# ---------------------------

tags = []
num_tags = 100
for i in range(num_tags):
	id = i + 1
	value = fake.catch_phrase() 
	tags.append({
		'id': id,
		'value': value
	})
	add_into_table('Tag', tags[i])

messages = []
num_messages = 100
for i in range(num_messages):
	id = i + 1
	text = fake.paragraph()
	user_id = random.randint(1, num_users)
	datetime = fake.date() + ' ' + fake.time()
	messages.append({
		'id': id,
		'text': text,
		'user_id': user_id,
		'datetime': datetime 
	})
	add_into_table('Message', messages[i])

book_and_authors = []
num_book_and_authors = 100

for i in range(num_book_and_authors):
	book_id = random.randint(1, num_books)
	author_id = random.randint(1, num_authors)
	book_and_authors.append({
		'book_id': book_id,
		'user_id': user_id 
	})
	add_into_table('Book_and_Author', book_and_authors[i])
# -----------------------

book_and_tags = []
num_book_and_tags = 100

for i in range(num_book_and_tags):
	book_id = random.randint(1, num_books)
	tag_id = random.randint(1, num_tags)
	book_and_tags.append({
		'book_id': book_id,
		'tag_id': tag_id 
	})
	add_into_table('Book_and_Tag', book_and_tags[i])

paper_and_authors = []
num_paper_and_authors = 100

for i in range(num_paper_and_authors):
	paper_id = random.randint(1, num_papers)
	author_id = random.randint(1, num_authors)
	paper_and_authors.append({
		'paper_id': paper_id,
		'author_id': author_id 
	})
	add_into_table('Paper_and_Author', paper_and_authors[i])

periodical_and_tags = []
num_periodical_and_tags = 100

for i in range(num_periodical_and_tags):
	periodical_id = random.randint(1, num_periodicals)
	tag_id = random.randint(1, num_tags)
	periodical_and_tags.append({
		'periodical_id': periodical_id,
		'tag_id': tag_id 
	})
	add_into_table('Periodical_and_Tag', periodical_and_tags[i])
