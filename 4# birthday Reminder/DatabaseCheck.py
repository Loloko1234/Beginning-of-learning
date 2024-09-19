import sqlite3
from datetime import datetime, timedelta

def check_upcoming_birthdays():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    # Calculate the date for tomorrow
    tomorrow = datetime.now() + timedelta(days=1)

    # Fetch people who have birthdays tomorrow
    c.execute('SELECT name, birthdate FROM birthdays WHERE strftime("%m-%d", birthdate) = ?', (tomorrow.strftime('%m-%d'),))
    birthdays = c.fetchall()
    
    conn.close()
    return birthdays

# Example usage:
upcoming_birthdays = check_upcoming_birthdays()
for name, birthdate in upcoming_birthdays:
    print(f"{name} has a birthday on {birthdate}")