"""This program gives alert if there is rain in the next 12 hrs"""

# Dependencies
# import datetime as dt
import requests

# Internal modules

# CONSTANTS
WEATHER_API_ID = "f1f17c8b0b522f73a27d24873aea3da9"

MY_LAT = 36.731650
MY_LOG = -119.785860

WEATHER_PARAMS = {
    "lat":MY_LAT,
    "lon":MY_LOG,
    "cnt": 4, # for 12 hrs
    "appid":WEATHER_API_ID
}

WEATHER_API_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

def will_rain(weather_data:dict)-> bool:
    """
     check weather id >701 for all datas from response

    :param weather_data:
    :return: bool
    """

    # To do
    status_list = [True for weather_datum in weather_data.get('list')
                   if weather_datum.get('weather')[0].get('id') < 700]

    return bool(status_list)

# Methods
def main()-> None:
    """Start of a program"""

    # Make a request to Forcast API and get response
    response = requests.get(url=WEATHER_API_END_POINT,params=WEATHER_PARAMS)
    response.raise_for_status()

    # Print the HTTP status code
    print(response.status_code)

    # Gets the weather data from response
    weather_data = response.json()
    print(weather_data)

    if will_rain(weather_data=weather_data):
        print("Bring Umbrella")
    else:
        print("Enjoy your day")

if __name__ == '__main__':
    main()
