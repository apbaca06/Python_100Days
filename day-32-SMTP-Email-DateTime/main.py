import smtplib
from datetime import datetime
import random

my_email = "cindydemotest@gmail.com"
password = "Test@cindy"
to_email = "cindychen.co@gmail.com"

"""
Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com
"""

def send_email_gmail(message):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
    connection.close()


def send_email_yahoo():
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # use \n\n to separate subject and content
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Hello\n\nThis is a test email")


def format_email_content(subject, quote):
    return f"Subject:{subject}\n\n{quote}"


def check_weekday_is_tuesday():
    return datetime.now().weekday() == 1


def get_quote_of_the_day():
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        return random.choice(lines)


if check_weekday_is_tuesday():
    quote = get_quote_of_the_day()
    print(quote)
    email_content = format_email_content("Power Mail", quote)
    send_email_gmail(email_content)
