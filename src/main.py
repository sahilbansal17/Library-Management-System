import pymysql

db = pymysql.connect("localhost", "sahilbansal", "iamalive", "lms")
cursor = db.cursor()

cursor.execute("Create database lms;")

cursor.execute("source ../db/sql_commands.sql;")