"""
App_Name: Interaction_wiki
Purpose: Will contains few more examples for the selenium usage
"""

# Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By


# Internal modules

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Interaction_wiki
    to do Will contains few more examples for the selenium usage
    """
    # To do
    driver = webdriver.Chrome()
    driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

    count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
    print(f"{ count = } ")

    driver.get(url="http://secure-retreat-92358.herokuapp.com")

    f_name = driver.find_element(By.NAME, "fName")
    l_name = driver.find_element(By.NAME, "lName")
    email_address = driver.find_element(By.NAME, "email")

    button = driver.find_element(By.TAG_NAME, "button")
    f_name.send_keys("P")
    l_name.send_keys("S")
    email_address.send_keys("heeeeee@gmail.com")
    button.click()

    driver.quit()


if __name__ == '__main__':
    main()
