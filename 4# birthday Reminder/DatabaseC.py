import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE birthdays(id INTEGER PRIMARY KEY, name TEXT, birthdate DATE)''')
conn.commit()
conn.close()