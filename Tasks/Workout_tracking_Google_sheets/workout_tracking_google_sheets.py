""" AI + Tracking the worksheet """

import datetime as dt
# Dependencies
import os

# Internal modules
from Tasks.library.requests_services import RequestService

# CONSTANTS
API_KEY = os.environ['API_KEY']
APP_ID = os.environ['APP_ID']

NUTRITION_X_HEADER = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
GOOGLE_SHEET_HEADER = {
    'Authorization': os.environ['GOOGLE_SHEET_TOKEN']
}
AGE = 32
WEIGHT = 90
HEIGHT = 186

NUTRITION_X_ENDPOINT = 'https://trackapi.nutritionix.com'
NUTRIENTS_ENDPOINT = f"{NUTRITION_X_ENDPOINT}/v2/natural/nutrients"
INSTANT_ENDPOINT = f"{NUTRITION_X_ENDPOINT}/v2/search/instant"
SEARCH_ENDPOINT = f"{NUTRITION_X_ENDPOINT}/v2/search/item"
EXERCISE_ENDPOINT = f"{NUTRITION_X_ENDPOINT}/v2/natural/exercise"

GOOGLE_SHEET_API = os.environ['MY_WORKOUT_SHEET_API']


# Methods-------------------------------------------------------------------
def get_exercise_json() -> dict:
    """will get the user input and convert it into dict"""

    # Get the user data in the form of sentences
    user_query = input("Tell me what you did today: ")

    # Params
    query_params = {
        'query': user_query,
        'weight_kg': WEIGHT,
        'height_cm': HEIGHT,
        'age': AGE
    }

    # Creates a Request API helper
    nutrition_x_api = RequestService(default_headers=NUTRITION_X_HEADER)

    response_data = nutrition_x_api.post(data_params=query_params, url=EXERCISE_ENDPOINT)
    print(f"{ response_data = } ")

    # Returns JSON payload of the response data
    return response_data.json()


def add_a_row_google_sheets(data: dict) -> None:
    """ Will update the dictionary data in the spreadsheet"""
    # Creates an API helper
    google_sheets_api = RequestService(default_headers=GOOGLE_SHEET_HEADER)

    # creates a row
    for exercises_row in data['exercises']:
        row_data = {
            'sheet1': {
                'date': dt.datetime.today().strftime('%d/%m/%Y'),
                'time': dt.datetime.now().strftime('%H:%M:%S'),
                'exercise': exercises_row.get('name').title(),
                'duration': exercises_row.get('duration_min'),
                'calories': exercises_row.get('nf_calories')
            }
        }

        # Post the data to sheet
        response_data = google_sheets_api.post(url=GOOGLE_SHEET_API, data_params=row_data)
        print(f"{ response_data.text = } ")


def main() -> None:
    """Start of a program"""

    today = dt.datetime.today()
    print(f"{ today = } ")

    data = get_exercise_json()

    add_a_row_google_sheets(data)

    print("End of the program")


if __name__ == '__main__':
    main()
