"""Contains the data manager class"""

# Dependencies
import os
from pprint import pprint

# Internal Modules
from Tasks.library.requests_services import RequestService

# CONSTANTS
GOOGLE_SHEET_API = os.environ['GOOGLE_SHEET_API']
GOOGLE_SHEET_HEADER = {
    'Authorization': os.environ['GOOGLE_SHEET_TOKEN']
}



class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        # Creates an API helper
        self.google_sheets_api = RequestService(default_headers=GOOGLE_SHEET_HEADER)
        self.sheet_data = None

    def get_all_data(self) -> dict:
        """ Get all the entered row from a Google sheet"""

        response = self.google_sheets_api.get(url=GOOGLE_SHEET_API)

        self.sheet_data = response.json().get('prices')

        return self.sheet_data

    def print_data(self) -> None:
        """uses pprint to print the data"""
        pprint(self.sheet_data)

    def update_destination_codes(self) -> None:
        """Based on the Row Id it will update the data into a row """

        prices = self.sheet_data

        for price in prices:
            new_data = {
                "price": {
                    "iataCode": price.get('iataCode')
                }
            }

            # API combined with Row_id
            new_url = GOOGLE_SHEET_API + '/' + str(price.get('id'))

            response = self.google_sheets_api.put(url=new_url, data_params=new_data)
            print(response.status_code)
