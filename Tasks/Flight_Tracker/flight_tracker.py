"""
This file will need to use the
DataManager, FlightSearch, FlightData, NotificationManager classes
to achieve the program requirements
"""

# Dependencies

# Internal modules
from data_manager import DataManager
from flight_data import FlightData

# CONSTANTS

# Methods-------------------------------------------------------------------

def main() -> None:
    """Start of a program"""
    data_manager = DataManager()
    flight_data = FlightData()

    sheet_data = data_manager.get_all_data()
    data_manager.print_data()

    if sheet_data[0]["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.sheet_data = sheet_data
        data_manager.update_destination_codes()

    

if __name__ == '__main__':
    main()
