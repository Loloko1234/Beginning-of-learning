import sqlite3

def add_birthday(name, birthdate):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    c.execute('INSERT INTO birthdays (name, birthdate) VALUES (?, ?)', (name, birthdate))
    
    conn.commit()
    conn.close()

# Przykład użycia
add_birthday("Nowaczkiewicz", "2024-23-09")