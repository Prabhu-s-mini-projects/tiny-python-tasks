"""
App_Name: Automates the Cookie clicker game
Purpose: using selenium automates the cookie clicker
"""
from time import time

# Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By


# Internal modules

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Automates the Cookie clicker game
    to do using selenium automates the cookie clicker
    """
    # To do
    # Configure Webdriver to the website open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url="https://orteil.dashnet.org/cookieclicker/")

    # lang_select = driver.find_element(By.ID,"langSelect-EN")
    # lang_select.click()

    big_cookie = driver.find_element(By.ID, "bigCookie")

    five_min = time() + 60 * 5
    timeout = time() + 5
    while True:

        big_cookie.click()

        if time() > timeout:
            # To do
            cookies_count = driver.find_element(By.ID, "cookies").text
            print(cookies_count)

            store = driver.find_element(By.ID, "store")
            print(store)

            # Reset time
            timeout = time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time() > five_min:
            cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond").text
            print(f"{ cookies_per_second = } ")
            break

    driver.quit()


if __name__ == '__main__':
    main()
