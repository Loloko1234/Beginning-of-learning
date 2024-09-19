import schedule
import time

def check_and_notify():
    birthdays = check_upcoming_birthdays()
    for name, birthdate in birthdays:
        send_email_notification(name, birthdate)

# Harmonogram - codziennie o 9:00
schedule.every().day.at("09:00").do(check_and_notify)

# Główna pętla, która uruchamia harmonogram
while True:
    schedule.run_pending()
    time.sleep(60)  # Sprawdza co minutę
