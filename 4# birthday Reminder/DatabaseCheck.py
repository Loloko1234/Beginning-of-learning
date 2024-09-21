import sqlite3
from datetime import datetime, timedelta

def check_upcoming_birthdays():
    print("check_upcoming_birthdays called")  # Dodajemy print tutaj
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    # Calculate the date for tomorrow
    tomorrow = datetime.now() + timedelta(days=1)
    print(f"Checking birthdays for: {tomorrow.strftime('%Y-%m-%d')}")  # Dodajemy print tutaj

    # Fetch people who have birthdays tomorrow
    c.execute('SELECT name, birthdate FROM birthdays WHERE strftime("%m-%d", birthdate) = ?', (tomorrow.strftime('%m-%d'),))
    birthdays = c.fetchall()
    
    conn.close()
    print(f"Found birthdays: {birthdays}")  # Dodajemy print tutaj
    return birthdays

if __name__ == "__main__":
    birthdays = check_upcoming_birthdays()
    print(f"Birthdays: {birthdays}")
