"""
App_Name: Selenium_example
Purpose: contains example for the selenium
"""
# Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By


# Internal modules

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Selenium_example
    to do contains example for the selenium
    """

    # Configure Webdriver to the website open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome()
    driver.get(url="https://www.amazon.com")

    driver.get(url="https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/" \
                   "dp/B00FLYWNYQ/ref=sr_1_1?crid=3F4GJXJCSBQQZ&dib=eyJ2IjoiMSJ9.y4LLAMvRXyF" \
                   "-GJBFF44YpgoQFm3qlOqvoway1SDbaoWDPyWnF_gZbDUmfjzaG2mJiBUnAHLFMmgcQz3xJU5r9_" \
                   "u__VUJFaoM7NkyoHuWc0ZITN_FZKfeSYcoBdpjx10hye7WiqZf1Y7cOOm2nGxnFV3D96JGWtwacFN" \
                   "NjjKVdDo8wWBv4hHH7FRyiMNlH6U8im9amKv7z9m3Sm1F1gQovs6apyw-bADwooAb1ezPZ3M" \
                   ".dmoZ3vVGH3WfwpX7ygcoCgkwt8w37E-rH2DPEceb2Ms&dib_tag=se&keywords=instant+pot" \
                   "&qid=1731255383&sprefix=in%2Caps%2C194&sr=8-1")

    price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    print(f"{ price_dollar = } & {price_cents = } ")

    driver.get(url="https://python.org")
    search_bar = driver.find_element(By.NAME, "q")
    print(search_bar)

    button = driver.find_element(By.ID, "submit")
    print(f"{ button.size = } ")
    # button.click()

    # dates =  driver.find_elements(
    #     By.XPATH,
    #     '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time/text()')

    dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

    event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

    final_dict = {}

    for index, (date, event_name) in enumerate(zip(dates, event_names)):
        new_dict = {
            index: {
                date.text: event_name.text
            }
        }
        final_dict.update(new_dict)

    print(f"{ final_dict = } ")

    # driver.close() # To close a particular Tab.
    driver.quit()  # Will quit the entire browser.


if __name__ == '__main__':
    main()
