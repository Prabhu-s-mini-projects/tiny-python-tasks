"""Contains a Flight search class"""

# Dependencies
import os

from dotenv import load_dotenv

from Tasks.library.requests_services import RequestService

load_dotenv()  # take environment variables from .env

# CONSTANTS
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
END_POINT = "test.api.amadeus.com/v1"

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self._api_key = os.environ['AMADEUS_API_KEY']
        self._api_secret = os.environ['AMADEUS_API_SECRET']
        self._token = self._get_new_token()

    def _get_new_token(self) -> str:
        """ return the tokens"""
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'keyword': self._api_key,
            'client_secret': self._api_secret
        }

        request_service = RequestService(default_headers=header)

        response = request_service.post(url=TOKEN_ENDPOINT, data_params=body)

        json_response = response.json()

        token = json_response.get('access_token')

        return token

    def get_destination_code(self, city_name):
        """Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later."""

        header = {
            'Authorization': 'Bearer' + self._token
        }

        body = {
            'keyword': city_name
        }

        request_service = RequestService(default_headers=header)

        response = request_service.post(url=TOKEN_ENDPOINT, data_params=body)

        json_response = response.json()

        code = json_response.get('iataCode')

        return code
