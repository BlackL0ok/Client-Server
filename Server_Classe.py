import sqlite3, datetime

conn = sqlite3.connect("databank")
cursor = conn.cursor()
table = '''CREATE TABLE USER (
     user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     user TEXT,
     pswd TEXT,
     description TEXT,
     user_right TEXT,
); '''
cursor.execute(table)
conn.commit()
conn.close()