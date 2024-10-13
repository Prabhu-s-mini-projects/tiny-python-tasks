"""Contains the Flight data class"""

# Dependencies

class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self,**kwargs):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = float(kwargs.get('price'))
        self.origin_airport =  kwargs.get('origin_airport')
        self.destination_airport =  kwargs.get('destination_airport')
        self.out_date =  kwargs.get('out_date')
        self.return_date =  kwargs.get('return_date')

    def get_price_in_st(self)-> str:
        """returns the price"""
        return str(self.price)

    def get_outbound_and_inbound(self)-> str:
        """:return dates in data format"""
        return f'{self.out_date} --> {self.return_date}'

def check_cheapest_flight(data:dict)-> FlightData:
    """
    Parses the JSON data returned from your FlightSearch.
    Add some error handling e.g., if that data is None.
    """
    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        print("No flight data")
        return FlightData(
            price=0.0,
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A")

        # Data from the first flight in the json
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(price=lowest_price, origin_airport=origin_airport,
                                 destination_airport=destination_airport, out_date=out_date,
                                 return_date=return_date)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(price=lowest_price, origin_airport=origin_airport,
                                 destination_airport=destination_airport, out_date=out_date,
                                 return_date=return_date)
            print(f"Lowest price to {destination_airport} is ${lowest_price}")

    return cheapest_flight
