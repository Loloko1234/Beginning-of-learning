import schedule
import time
from DatabaseCheck import check_upcoming_birthdays
from EmailSender import send_email_notification

def check_and_notify():
    print("Running check_and_notify")
    birthdays = check_upcoming_birthdays()
    print(f"Birthdays: {birthdays}")
    for name, birthdate in birthdays:
        send_email_notification(name, birthdate)

# Harmonogram - codziennie o 9:00 rano
schedule.every().day.at("09:00").do(check_and_notify)
print("Scheduled check_and_notify")

# Główna pętla, która uruchamia harmonogram
while True:
    schedule.run_pending()
    time.sleep(60)  # Sprawdza co minutę