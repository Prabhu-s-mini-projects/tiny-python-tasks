# Dependencies
import requests

# Constants
ENDPOINT = "http://api.open-notify.org/iss-now.json"
def main()-> None:
    response = requests.get(url=ENDPOINT)
    response.raise_for_status()

    data = response.json()
    iss_position = data['iss_position']

    print(data)

    # if response.status_code == 404:
    #     raise Exception("Request not Found")
    # elif response.status_code == 403:
    #     raise Exception("You don't have a permission to get the data")


if __name__ == "__main__":
    main()
