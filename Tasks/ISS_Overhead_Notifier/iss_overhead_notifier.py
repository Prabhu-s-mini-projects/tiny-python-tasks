""" Main script of overhead Notifier"""

from datetime import datetime
import smtplib
import requests

MY_LAT = 55.9571 # Your latitude
MY_LONG = -5.4949 # Your longitude

MY_EMAIL = "tdummy206@gmail.com"
PASSWORD = "ArqnFsktowTQHZ5"

def is_iss_overhead()-> bool:
    """ Check whether it over my location"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG-5 <= iss_longitude<= MY_LONG+5 and MY_LAT-5<= iss_latitude <= MY_LAT+5:
        return True
    return False

def is_night()-> bool:
    """Check whether is a nighttime or day time"""

    # Getting current time
    time_now = datetime.now()

    # Sunrise and Sunset time
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"{sunrise = }")
    print(f"{sunset = }")

    if sunrise <= time_now.hour <= sunset:
        return  True
    return False

def send_notification()-> None:
    """ Sends email alert"""

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=" Passing right above your head"
        )
    print("SEND the NOTIFICATION")

def main()-> None:
    """starting point of program"""

    send_notification()

    if not is_iss_overhead() and is_night():
        send_notification()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

if __name__ == '__main__':
    main()


