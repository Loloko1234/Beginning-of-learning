import smtplib
from email.mime.text import MIMEText

def send_email_notification(name, birthdate):
    # Informacje do logowania się do serwera poczty
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'Put Your Email Here'
    password = 'Put Your Password Here'

    # Tworzymy wiadomość
    message = f"Przypomnienie: {name} ma urodziny jutro ({birthdate})!"
    msg = MIMEText(message)
    msg['Subject'] = 'Przypomnienie o urodzinach'
    msg['From'] = sender_email
    msg['To'] = sender_email  # Wysyłamy do siebie samego

    # Wysyłamy email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, sender_email, msg.as_string())

# Przykład użycia
send_email_notification('Jan Kowalski', '2024-05-01')
