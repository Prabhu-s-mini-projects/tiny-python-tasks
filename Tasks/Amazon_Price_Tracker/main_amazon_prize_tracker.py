"""
App_Name: Amazon_price_tracker
Purpose: tracks the items in the amazon if is below the mentioned price sends mail
"""
# Dependencies
import os
import smtplib

import requests
from bs4 import BeautifulSoup
# Add the os and dotenv modules
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Internal modules

# CONSTANTS
WEBSITE_URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Amazon_price_tracker
    to do tracks the items in the amazon if is below the mentioned price sends mail
    """
    # To do

    response = requests.get(WEBSITE_URL,timeout=10)
    website = response.text

    soup  = BeautifulSoup(website,"html.parser")
    price_in_tag = soup.find("span",class_="a-price-whole")
    price = float(price_in_tag.getText())
    price_decimal_in_tag = soup.find("span", class_="a-price-fraction")
    price += float(price_decimal_in_tag.getText())/100
    print(f"{ price = } ")

    # ====================== Use environment variables ===========================

    if price < TARGET_PRICE:
        message = f"{TARGET_PRICE = } but the actual{price = }"

        # Sends Email
        with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
            connection.starttls()
            result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
            print(result)
            connection.sendmail(
                from_addr=os.environ["EMAIL_ADDRESS"],
                to_addrs=os.environ["EMAIL_ADDRESS"],
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{WEBSITE_URL}".encode("utf-8")
            )






if __name__ == '__main__':
    main()
