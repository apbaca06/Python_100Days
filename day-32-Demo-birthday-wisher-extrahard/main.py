##################### Extra Hard Starting Project ######################
from pandas import *
from datetime import datetime
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
dataframe = pandas.read_csv("birthdays.csv")
date_now = datetime.now()
today_tuple = (date_now.month, date_now.day)

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in dataframe.iterrows()}


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

def pick_random_letter():
    default_letter_name = "letter_"
    default_letter_format = ".txt"
    random_number = random.randint(1, 3)
    return default_letter_name + str(random_number) + default_letter_format


def replace_name_from_letter(correct_name):
    letter_file = pick_random_letter()
    with open(f"letter_templates/{letter_file}", 'r') as file:
        content = file.read()
        replaced_content = content.replace("[NAME]", f"{correct_name}")
        return replaced_content


def send_email(content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="cindydemotest@gmail.com", password="Test@cindy")
        connection.sendmail(from_addr="cindydemotest@gmail.com", to_addrs="cindychen.co@gmail.com",
                            msg=f"Subject:Happy Birthday!!!\n\n{content}")

# 4. Send the letter generated in step 3 to that person's email address.


if today_tuple in birthday_dict:
    print('yeah')
    birthday_person = birthday_dict[today_tuple]
    name = birthday_person["name"]
    content = replace_name_from_letter(name)
    send_email(content)