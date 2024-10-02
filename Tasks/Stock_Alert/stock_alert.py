""" Main script of a program"""
# Dependencies
import datetime as dt
import requests

# Internal modules


# CONSTANTS
NEWS_API_KEY = 'TBD'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_API_KEY = 'TBD'
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'

def fetch_stock_price(symbol:str)-> dict:
    """ Using the API fetches the data """
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': STOCK_API_KEY
    }

    response = requests.get(url=STOCK_API_ENDPOINT, params=parameters, timeout=10)
    response.raise_for_status()

    print(f"{ response.url = } ")
    print(f"{ response.status_code = } ")


    return response.json() if response.status_code==200 else None

def get_news(q:str)-> dict:
    """collects the news from news API"""
    parameters = {
        'q': q,
        'apikey': NEWS_API_KEY
    }

    response = requests.get(url=NEWS_API_ENDPOINT, params=parameters, timeout=10)
    response.raise_for_status()

    print(f"{ response.url = } ")
    print(f"{ response.status_code = } ")

    return response.json() if response.status_code == 200 else None

# Methods
def main() -> None:
    """Start of a program"""

    data = fetch_stock_price("TSLA")
    print(f"{ data = } ")
    news = get_news("Tesla")
    print(f"{ news = } ")

    # ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # # When stock price increase/decreases
    # by 5% between yesterday and the day before yesterday then print("Get News").
    #
    # # Get yesterday's closing stock price.
    # Hint: You can perform list comprehensions on Python dictionaries.
    # # e.g. [new_value for (key, value) in dictionary.items()]
    # yesterday = str(dt.datetime.today().date() - dt.timedelta(1))
    # day_before_yes = str(dt.datetime.today().date() - dt.timedelta(2))
    #
    # stock_prices_history = data.get("Time Series (Daily)")
    #
    # stock_price = [price.get('4. close') for date, price in stock_prices_history.items()]
    #
    # print(f"{ stock_price = } ")
    #
    # # Get the day before yesterday's closing stock price
    # yesterday_closing_price = float(stock_price[1])
    # day_before_yesterday = float(stock_price[2])
    #
    # # Find the positive difference between 1 and 2. e.g. 40 - 20 = -20,
    # # but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    # difference = abs(yesterday_closing_price - day_before_yesterday)
    # print(f"{ difference = } ")
    #
    #
    # # Work out the percentage difference in price between
    # # closing price yesterday and closing price the day before yesterday.
    # percentage = difference * 100/ day_before_yesterday
    #
    # # If TODO4 percentage is greater than 5 then print("Get News").
    # print(f"{ percentage = } ")
    #
    # print("Get News")
    #
    #
    # ## STEP 2: https://newsapi.org/
    # # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    #
    # # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # news =  get_news("Tesla").get('articles')
    # print(f"{ news = } ")
    #
    # # Use Python slice operator to create a list that contains the first 3 articles.
    # # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    # top_3_news = news[0:2]
    # print(f"{ top_3_news = } ")

if __name__ == '__main__':
    main()
