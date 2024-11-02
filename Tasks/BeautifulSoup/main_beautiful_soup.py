"""
App_Name: BeautifulSoup_module
Purpose: contains an example of how to use the beautiful soup api
"""
import requests
# Dependencies
from bs4 import BeautifulSoup

# Internal modules

# CONSTANTS
WEBSITE_URL = "https://appbrewery.github.io/news.ycombinator.com/"


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : BeautifulSoup_module
    to do contains an example of how to use the beautiful soup api
    """
    # To do
    with open('website.html', 'r', encoding='utf-8') as file:
        html_data = file.read()

    print(html_data)

    soup = BeautifulSoup(html_data, 'html.parser')
    print(soup.prettify())
    print(soup.title.string)
    print(soup.find_all(name='a'))

    response = requests.get(WEBSITE_URL, timeout=10)
    y_combinator = response.text

    soup = BeautifulSoup(y_combinator, "html.parser")
    print(soup)
    print(soup.title.string)

    movie_titles = soup.find_all("a", class_="storylink")
    for movie_title in movie_titles:
        print(movie_title.getText())


if __name__ == '__main__':
    main()
