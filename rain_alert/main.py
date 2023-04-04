import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = XXXX
auth_token = os.environ.get("AUTH_TOKEN")



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": -33.868820,
    "lon": 151.209290,
    "exclude": "current, minutely, daily",
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_list = [int(weather_data["hourly"][i]["weather"][0]["id"]) for i in range(12)]
will_rain = False
#print(weather_list)

for weather in weather_list:
    if weather < 700:
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Be sure to bring an ☂️!",
        from_="93853027374",
        to="937370527"
    )
    print(message.status)




