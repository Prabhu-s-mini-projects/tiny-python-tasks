"""
App_Name: Musical Time machine
Purpose: Enter the date will create a spotify playlist with top 5 songs of that week
"""
# Dependencies
import os
import requests
from bs4 import BeautifulSoup
# from spotipy import Spotify
# from spotipy import SpotifyOAuth
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Internal modules


# CONSTANTS
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

BILL_BOARD_WEBSITE_URL = "https://www.billboard.com/charts/hot-100"
BILL_BOARD_HEADER = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Musical Time machine
    to do Enter the date will create a spotify playlist with top 5 songs of that week
    """
    # To do

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username="yourname",
        )
    )

    user_id = sp.current_user()["id"]
    print(f"{ user_id = } ")
    

    entered_date = input("Which year do you want to travel to?\n" +
                         "Enter the date in this format YYYY:MM:DD :")

    # Requests the BILLBOARD Website
    response =  requests.get(BILL_BOARD_WEBSITE_URL+f"/{entered_date}",
                             headers=BILL_BOARD_HEADER,
                             timeout=10)
    songs_from_website = response.text

    # parse the HTML content using the parser
    soup = BeautifulSoup(songs_from_website,"html.parser")

    # class_name = ("c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"+
    #               " lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125"+
    #               " u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330"+
    #               " u-max-width-230@tablet-only")
    # filtered_soup = soup.find_all("h3",id="title-of-a-story",class_=class_name)
    #
    # song_titles = [song.getText() for song in filtered_soup ]

    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    top_5_songs = song_names[:4]
    print(f"{ top_5_songs = } ")

    song_uris = []
    year = entered_date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")


    print(sp)



if __name__ == '__main__':
    main()
