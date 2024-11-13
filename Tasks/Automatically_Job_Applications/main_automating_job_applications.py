"""
App_Name: Automatically Job applications
Purpose: will apply for jobs in LinkedIn automatically
"""
# Dependencies
import os
import time

# Add the os and dotenv modules
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load environment variables from .env file
load_dotenv()
# Internal modules

# CONSTANTS
LINKEDIN_URL = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account"


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Automatically Job applications
    to do will apply for jobs in LinkedIn automatically
    """
    # Configure Webdriver to the website open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome()
    driver.get(url=LINKEDIN_URL)
    time.sleep(1)  # Gives time to load the page

    username = driver.find_element(By.ID, "username")
    username.send_keys(os.environ["EMAIL_ADDRESS"])

    password = driver.find_element(By.ID, "password")
    password.send_keys(os.environ["LINKEDIN_PASSWORD"])

    sign_in_button = driver.find_element(
        By.CSS_SELECTOR,
        "#organic-div > form > div.login__form_action_container > button"
    )
    sign_in_button.click()

    time.sleep(2)  # Gives time to load all the login pages

    jobs_tab_xpath = driver.find_element(
        By.XPATH, '// *[ @ id = "global-nav"] / div / nav / ul / li[3] / a'
    )
    jobs_tab_xpath.click()

    job_search = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
    job_search.send_keys("Python Developer")

    job_location = driver.find_element(By.ID, "jobs-search-box-location-id-ember249")

    # Clear the field in case there's any placeholder or previous input
    job_location.clear()

    # Send the desired location (Milpitas, CA)
    job_location.send_keys("Milpitas, CA")

    # Optionally, send a key to simulate pressing "Enter" after input
    job_location.send_keys(Keys.RETURN)

    listed_jobs = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container > li")

    for job in listed_jobs:
        title = job.find_element(By.CSS_SELECTOR, "strong").text
        company = job.find_element(
            By.CSS_SELECTOR, ".job-card-container__primary-description"
        ).text
        location = job.find_element(
            By.CSS_SELECTOR, ".job-card-container__metadata-item > span"
        ).text

        print(f"{company}looking for  {title} in {location} ")

    driver.quit()


if __name__ == '__main__':
    main()
