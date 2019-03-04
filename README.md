# Library-Management-System at IIT Jammu

## Script to create database
	$ sudo chmod 777 initialize
	$ ./initialize

This will automatically perform the next two steps mentioned below.

### 1. Creating the database
	$ sudo mysql < db/sql_commands.sql

This will create the database **lms** and all the tables with constraints associated.

### 2. Generating random data
	$ pip3 install -r requirements.txt 
	$ python3 db/generate_data.py

### 3. Running the queries
	$ python3 db/queries.py

### 4. Documentation
The documentation is available in the [doc/](doc/) folder.