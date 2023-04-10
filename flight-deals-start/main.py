#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from twilio.rest import Client

TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')

SHEETY_TOKEN = os.environ.get('SHEET_TOKEN')
SHEETY_GET_ENDPOINT = os.environ.get('SHEET_ENDPOINT')

account_sid = os.environ.get('TWILLIO_SID')
auth_token = os.environ.get('TWILLIO_TOKEN')

tequila_header = {
    "Content-Type" : "application/json",
    "apikey": TEQUILA_API_KEY,
}

sheety_headers = {
    "Authorization" : SHEETY_TOKEN,
    "Content-Type": "application/json",
}

#------------Get IATA Code------------------------#

city_cost_dict = {}
get_row_num = requests.get(url=SHEETY_GET_ENDPOINT, headers=sheety_headers)
get_row_num = get_row_num.json()

for i in range(len(get_row_num["prices"])):
    row_id = get_row_num["prices"][i-1]["id"]

    tequila_location_params = {
        "term": get_row_num["prices"][i-1]["city"],
        "location_types": "city",
        "active_only": "true",
    }

    tequila_response = requests.get(url=TEQUILA_LOCATION_ENDPOINT, params=tequila_location_params, headers=tequila_header)
    city_code = tequila_response.json()["locations"][0]["code"]

    sheety_add = {
        'price' : {
            'city': get_row_num["prices"][i-1]["city"],
            'iataCode': city_code,
            'lowestPrice': get_row_num["prices"][i-1]['lowestPrice'],
            'id': get_row_num["prices"][i-1]["id"],
        }
    }

    city_cost_dict[city_code] = get_row_num["prices"][i - 1]['lowestPrice']

    response = requests.put(url=f"https://api.sheety.co/939d5b2d5afe69747a7b20323f2fd8ed/flightDeals/prices/{row_id}", json=sheety_add, headers=sheety_headers)

#----------------Search flights---------------#

today = datetime.now().strftime("%d/%m/%Y")
today_plus_five_days = (datetime.today() + relativedelta(days=+5)).strftime("%d/%m/%Y")
six_months_ahead = (datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
six_months_plus_five_days = (datetime.today() + relativedelta(months=+6, days=+5)).strftime("%d/%m/%Y")

for city in city_cost_dict:

    tequila_flight_search_params = {
        "fly_from": "LCY",
        "fly_to": city,
        "date_from": today,
        "date_to": six_months_ahead,
        "return_from": today_plus_five_days,
        "return_to": six_months_plus_five_days,
        "flight_type": "round",
        "adults": 2,
        "infants": 2,
        "only_working_days": False,
        "only_weekends": False,
        "partner_market": "us",
        "max_stopovers": 2,
        "max_sector_stopovers": 2,
        "vehicle_type": "aircraft",
        "limit" : 5
    }

    response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, headers=tequila_header, params=tequila_flight_search_params)
    data = response.json()
    cheapest = city_cost_dict[city]
    from_airport = ""
    to_airport = ""
    date_from = ""
    date_to = ""
    cheaper_flight = False
    for i in range(len(data["data"])):
        if data["data"][i-1]["price"] < cheapest:
           cheapest = data["data"][i-1]["price"]
           from_airport = f'{data["data"][i-1]["cityFrom"]}-{data["data"][i-1]["cityCodeFrom"]}'
           to_airport = f'{data["data"][i-1]["cityTo"]}-{data["data"][i-1]["cityCodeTo"]}'
           date_from = data["data"][i-1]["route"][0]["local_departure"].split("T")[0]
           date_to = data["data"][i-1]["route"][-1]["local_departure"].split("T")[0]
           cheaper_flight = True
    if cheaper_flight == True:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Low price alert! Only ${cheapest} to fly from {from_airport} to {to_airport}, from {date_from} to {date_to}.",
            from_=os.environ.get('FROM_NUMBER'),
            to=os.environ.get('TO_NUMBER')
        )
        print(message.sid)

