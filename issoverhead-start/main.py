import requests, smtplib, time
from datetime import datetime

MY_LAT = 34.385204
MY_LONG = 132.455292

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
range_lat =  MY_LAT-5.0 < iss_latitude < MY_LAT + 5.0
range_long =  MY_LONG - 5.0 < iss_longitude < MY_LONG + 5.0

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

time_hour = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def send_email():
    if range_lat and range_long and (time_hour >= sunset or time_hour <= sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            MY_EMAIL = "XXXX"
            PASSWORD = "XXXX"

            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look up!\n\nThe Space Station is near you!")
    else:
        pass


while True:
    send_email()
    time.sleep(60)


