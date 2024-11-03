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
        print(f"{ movie_title.get("href") = } ")
        

    # movie_upvotes = soup.find_all("span", class_="score")
    #
    # for movie_upvote in movie_upvotes:
    #     print(f"{ int(movie_upvote.getText().split()[0]) = } ")


A_website_url = "https://www.empireonline.com/movies/features/best-movies-2/"

response =  requests.get(A_website_url)

soup = BeautifulSoup(response.text,"html.parser")

movie_titles =[movie_title.getText()
               for movie_title in soup.find_all("h3",
                                                class_="listicleItem_listicle-item__title__BfenH"
                                                )
               ]
movie_titles.reverse()

with open("movies.txt","w",encoding="utf-8") as file:
    for movie_title in movie_titles:
        file.write(f"{movie_title}\n")

if __name__ == '__main__':
    main()
