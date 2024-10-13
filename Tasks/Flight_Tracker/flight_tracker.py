"""
This file will need to use the
DataManager, FlightSearch, FlightData, NotificationManager classes
to achieve the program requirements
"""

# Dependencies
import time
from datetime import datetime, timedelta
from pprint import pprint

# Internal modules
from data_manager import DataManager
from flight_data import FlightData, check_cheapest_flight
from flight_search import FlightSearch

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """Start of a program"""
    data_manager = DataManager()
    flight_search = FlightSearch()

    sheet_data = data_manager.get_all_data()
    data_manager.print_data()

    if sheet_data[0]["iataCode"] == "":

        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        pprint(sheet_data)

        data_manager.sheet_data = sheet_data
        data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(1)
    next_6_months = datetime.now() + timedelta(6*30)

    for destination in sheet_data:
        print(f"getting flight { destination['city'] = }  ")

        data = flight_search.find_cheapest_flight(
            originLocationCode ="SFO",
            destinationLocationCode= destination['iataCode'],
            departureDate= tomorrow.strftime("%Y-%m-%d"),
            returnDate=next_6_months.strftime("%Y-%m-%d") ,
            adults= '1'
        )

        cheapest_flight: FlightData = check_cheapest_flight(data)
        print(f"{destination['city']}: £{cheapest_flight.price}")
        # Slowing down requests to avoid rate limit
        time.sleep(2)




if __name__ == '__main__':
    main()
