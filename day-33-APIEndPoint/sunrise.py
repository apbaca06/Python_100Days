import requests
from datetime import datetime

MY_LAT = 25.032969
MY_LONG = 121.565414

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

def get_hour(date_time):
    return int(date_time.split("T")[1].split(":")[0])

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()

data = response.json()
print(data)
iss_latitude = data["results"]["iss_position"]
sunrise_hour = get_hour(data["results"]["sunrise"])
sunset_hour = get_hour(data["results"]["sunset"])
now_hour = datetime.now().hour

if sunset_hour <= now_hour:

print(datetime.now())

