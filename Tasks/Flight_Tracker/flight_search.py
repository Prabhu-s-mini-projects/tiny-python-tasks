"""Contains a Flight search class"""

# Dependencies
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

# CONSTANTS
API = os.environ['TBD']

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        print("cTodod")

    def get_destination_code(self, city_name):
        """Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later."""
        code = "TESTING"
        return code
