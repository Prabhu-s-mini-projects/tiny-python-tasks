# Program Requirements

1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport
   Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city
   code (not the airport code see here).

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the
   Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your
   own number using the Twilio API.

4. The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.
   e.g.