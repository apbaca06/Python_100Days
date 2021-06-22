import requests
from datetime import datetime
import smtplib

"""
1XX: Hold None
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up

https://httpstatuses.com/
"""

MY_LAT = 25.032969
MY_LONG = 121.565414

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    print(longitude, latitude)

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG-5 <= longitude <= MY_LONG +5:
        print(True)
        return True
    else:
        return False


    # if response.status_code == 404:
    #     raise Exception("That resource doesn't exist.")
    # elif response.status_code == 401:
    #     raise Exception("You are not authorized to access this data.")


parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

def get_hour(date_time):
    return int(date_time.split("T")[1].split(":")[0])

def is_night():
    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    data = response.json()
    print(data)
    sunrise_hour = get_hour(data["results"]["sunrise"])
    sunset_hour = get_hour(data["results"]["sunset"])
    print(sunset_hour, sunrise_hour)
    now_hour = datetime.now().hour
    print(now_hour)

    if sunset_hour <= now_hour or now_hour <= sunrise_hour:
        return  True
    else:
        return False


if is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("cindychen.co@gmail.com", "ichrock0826")
    connection.sendmail(from_addr="cindychen.co@gmail.com",
                        to_addrs="cindychen.co@gmail.com",
                        msg="Subject: Test")