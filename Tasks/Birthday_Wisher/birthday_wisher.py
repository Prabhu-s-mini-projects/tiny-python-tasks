""" Script that  changes the name of sample letter and sends an email """
# Dependencies
import datetime as dt
#import smtplib
import random
import pandas as pd

# Internal Modules

# CONSTANTS
BIRTHDAY_DB_PATH = "birthdays.csv"

def check_birthdays()-> str:
    """
    Check if today matches a birthday in the birthdays.csv
        HINT 1: Only the month and day matter.
        HINT 2: You could create a dictionary from birthdays.csv that looks like this:
        birthdays_dict = {
            (month, day): data_row
        }
    """
    # Reads the data from csv file
    birthday_db = pd.read_csv(BIRTHDAY_DB_PATH)

    # Get today's date
    today = dt.datetime.today()

    today_year = today.year
    today_month = today.month
    today_day =today.day

    if today_year in list(birthday_db["year"]):
        all_birthdays_in_year = birthday_db[birthday_db.year == today_year]
        print(all_birthdays_in_year)

        if today_month in list(birthday_db["month"]):
            all_birthdays_in_month = birthday_db[birthday_db.month == today_month]
            print(all_birthdays_in_month)

            if today_day in list(birthday_db["day"]):
                all_birthdays_in_day = birthday_db[birthday_db.day == today_day]
                print(all_birthdays_in_day)

                for index ,row in all_birthdays_in_day.iterrows():
                    selected_letter = "letter_" + str(random.randint(1,3))
                    selected_letter_path = f"letter_templates/{selected_letter}.txt"

                    with open(selected_letter_path, encoding="utf-8") as letter_file:
                        letter = letter_file.read()
                        letter = letter.replace("[NAME]", str(row.name))

                        #my_email = "dummy@gmail.com"

                        print(all_birthdays_in_day.to_records())
                        print(row.email)
                        print(row.name)
                        print(index)
                        print(letter)

                    # with smtplib.SMTP("Smtp.gmail.com") as connection:
                    #     connection.starttls()
                    #     connection.login(user=my_email,password="abcdef")
                    #     connection.sendmail(
                    #         from_addr=my_email,
                    #         to_addrs=row.email,
                    #         msg=letter
                    #     )

                    print(letter)

    return " "

check_birthdays()
