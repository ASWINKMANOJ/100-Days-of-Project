import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -17.802508
MY_LNG = -50.928860
EMAIL = "projectday32@gmail.com"
PASSWORD = "lvrfucjyiojwaylo"


def above_location():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    longitude = float(response_iss.json()["iss_position"]["longitude"])
    latitude = float(response_iss.json()["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT - 5 or MY_LNG - 5 <= longitude <= MY_LNG - 5:
        return True
    else:
        False


def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    current = datetime.now()
    current_hour = current.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if above_location() and night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs="achooaswinjr@gmail.com", from_addr=EMAIL, msg="Subject:LOOK UP\n\nThe ISS"
                                                                                        " is above you in the sky.")
