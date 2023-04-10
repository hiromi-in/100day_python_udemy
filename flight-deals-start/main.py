#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
import os

account_sid = os.environ.get('TWILLIO_SID')
auth_token = os.environ.get('TWILLIO_TOKEN')
MESSAGE_FROM = os.environ.get('FROM_NUMBER')
MESSAGE_TO = os.environ.get('TO_NUMBER')
SHEETY_TOKEN = os.environ.get('SHEET_TOKEN')
SHEETY_GET_ENDPOINT = os.environ.get('SHEET_ENDPOINT')
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')

data_manager = DataManager(sheet_token=SHEETY_TOKEN, sheet_endpoint=SHEETY_GET_ENDPOINT)
flight_data = FlightData(apikey=TEQUILA_API_KEY)
flight_search = FlightSearch(apikey=TEQUILA_API_KEY)

original_fly_from = "LCY"

for i in range(len(data_manager.all_data)):
    city_name = data_manager.get_city_name(row_num=i)
    if data_manager.all_data[i-1]["iataCode"] == '':
        city_code = flight_data.get_city_code(city_name=city_name)
        data_manager.add_city_code(city_name=city_name, row_num=i, city_code=city_code)

today = datetime.now().strftime("%d/%m/%Y")
today_plus_five_days = (datetime.today() + relativedelta(days=+5)).strftime("%d/%m/%Y")
six_months_ahead = (datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
six_months_plus_five_days = (datetime.today() + relativedelta(months=+6, days=+5)).strftime("%d/%m/%Y")

city_cost_list={}
for i in range(len(data_manager.all_data)):
    city_cost_list[data_manager.all_data[i-1]["iataCode"]] = data_manager.all_data[i-1]["lowestPrice"]

for city in city_cost_list:
    search_data = flight_search.search_flight(fly_from=original_fly_from,fly_to=city, date_from=today, date_to=six_months_ahead,
                                       return_from=today_plus_five_days, return_to=six_months_plus_five_days)["data"]
    cheaper_flight = False
    cheapest = city_cost_list[city]

    for i in range(len(search_data)):
       flight_data.modify_data(row_num=i-1, search_data=search_data, cheapest=cheapest)
       cheaper_flight = True

    if cheaper_flight == True:
        notification = NotificationManager(sid=account_sid, token=auth_token, message_to=MESSAGE_TO, message_from=MESSAGE_FROM)
        notification.send_message(cheapest=flight_data.cheapest, from_airport=flight_data.from_airport,
                                  to_airport=flight_data.to_airport, date_from=flight_data.date_from,
                                  date_to=flight_data.date_to)

