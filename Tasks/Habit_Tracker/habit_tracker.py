""" Main script Using HTTPS post to update habit tracker data to server"""

import datetime as dt
# Dependencies
import os

import requests

# Internal modules


# CONSTANTS
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ['USERNAME']
HEADERS = {
    'X-USER-TOKEN': os.environ['TOKEN']
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "completedgraphv0"

POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"


# Methods-------------------------------------------------------------------

def send_post_requests(json: dict, url: str, headers: dict = None) -> dict:
    """ Sends the post-request to the respective url """

    # Sends post-request
    response = requests.post(url=url, json=json, headers=headers, timeout=10)
    print(f"{ response.status_code = } ")
    print(f"{ response.text = } ")

    # To indicate and capture the HTTP ERROR Codes
    response.raise_for_status()

    # returns the response json
    return response.json()


def pixela_sign_up(user_name: str = USERNAME, token: str = HEADERS.get('X-USER-TOKEN')) -> dict:
    """
    To register and create a new account in pixela

    To update params, refer this page: https://docs.pixe.la/entry/post-user
    """

    # Setting the params
    params = {
        'token': token,
        'username': user_name,
        'agreeTermsOfService': "yes",
        'notMinor': 'yes'
    }

    return send_post_requests(json=params, url=PIXELA_ENDPOINT)


def create_graph(**kwargs: str) -> dict:
    """
    Creates a separate ID for graph:
    Refer : https://docs.pixe.la/entry/post-graph
    """

    # creates a params
    config = {
        'id': kwargs.get('graph_id'),
        'name': kwargs.get('name'),
        'unit': kwargs.get('unit'),
        'type': kwargs.get('type'),
        'color': kwargs.get('color'),
        'timezone': 'America/Los_Angeles',  # kwargs.get('timezone'),
    }

    return send_post_requests(json=config, url=GRAPH_ENDPOINT, headers=HEADERS)


def setting_up_account(graph_name: str, graph_id: str = GRAPH_ID) -> None:
    """
    1. Register an account
    2. Create a graph

    :param graph_id: Unique id for the graph
    :param graph_name: name of the graph
    :return: None
    """

    # Register an account
    result = pixela_sign_up()
    print(f"{ result = } ")

    # Creates an account
    status = create_graph(name=graph_name, graph_id=graph_id,
                          unit='tasks', type='int', color='shibafu')
    print(f"{ status = } ")


def post_data(date: str, quantity: int) -> dict:
    """ Post data """

    data = {
        'date': date,
        'quantity': str(quantity),
    }

    return send_post_requests(json=data, url=POST_ENDPOINT, headers=HEADERS)


def send_put_requests(json: dict, url: str, headers: dict = None) -> dict:
    """ Sends the put-request to the respective url """

    # Sends post-request
    response = requests.put(url=url, json=json, headers=headers, timeout=10)
    print(f"{ response.status_code = } ")
    print(f"{ response.text = } ")

    # To indicate and capture the HTTP ERROR Codes
    response.raise_for_status()

    # returns the response json
    return response.json()


def update_a_post(date: str, quantity: int) -> dict:
    """To make a correction"""
    data = {
        'quantity': str(quantity),
    }

    return send_put_requests(json=data, url=POST_ENDPOINT + f'/{date}', headers=HEADERS)
    
def main() -> None:
    """Start of a program"""

    # Commenting below code as Since user can sign up only once
    # setting_up_account(graph_name="Successful Task")

    today_s_date = dt.datetime.today()
    date = today_s_date.strftime('%Y%m%d')
    result = post_data(date=date, quantity=1)
    print(f"{ date =  }  {result}")

    result = update_a_post(date=date, quantity=67)
    print(f"{ date =  }  {result}")

    for number in range(7, 10):
        date = dt.datetime(year=2024, month=7, day=number)
        date = date.strftime('%Y%m%d')
        result = post_data(date=date, quantity=30 + number)
        print(f"{ date =  }  {result}")



    print("Habit Tracker")


if __name__ == '__main__':
    main()
