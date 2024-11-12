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

    driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

    big_cookie = driver.find_element(By.ID, "cookie")

    five_min = time() + 60 * 5
    timeout = time() + 5
    while True:

        big_cookie.click()

        if time() > timeout:
            # To do
            cookies_count = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            print(cookies_count)

            products = driver.find_elements(By.CSS_SELECTOR, "#store b")

            affordable_upgrades = {}
            for product in products:
                if "-" in product.text:
                    cost = int(product.text.split("-")[1].replace(",", ""))
                    item = {
                        cost: product
                    }
                    if cookies_count > cost:
                        affordable_upgrades.update(item)

            if affordable_upgrades:
                print(affordable_upgrades)
                high_affordable_upgrade = max(affordable_upgrades.keys())
                product = affordable_upgrades[high_affordable_upgrade]
                print(product.text)

                product.click()

            # Reset time
            timeout = time() + 5

        # After 5 minutes, stop the bot and check the cookies per second count.
        if time() > five_min:
            cookies_per_second = driver.find_element(By.ID, "cps").text
            print(f"{ cookies_per_second = } ")
            break

    driver.quit()


if __name__ == '__main__':
    main()
