import requests
from data_manager import DataManager



class FlightData():

    def __init__(self, apikey):
        self.TEQUILA_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.TEQUILA_API_KEY = apikey
        self.tequila_header = {
            "Content-Type": "application/json",
            "apikey": self.TEQUILA_API_KEY,
        }
        self.from_airport = ""
        self.to_airport = ""
        self.date_from = ""
        self.date_to = ""
        self.stop_over = 0
        self.via_city = ''
        self.from_airport_code=''
        self.to_airport_code=''

    def get_city_code(self, city_name):
        tequila_location_params = {
            "term": city_name,
            "location_types": "city",
            "active_only": "true",
        }

        tequila_response = requests.get(url=self.TEQUILA_LOCATION_ENDPOINT, params=tequila_location_params,
                                        headers=self.tequila_header)

        city_code = tequila_response.json()["locations"][0]["code"]

        return city_code

    def modify_data(self, row_num, cheapest, search_data):
        self.cheapest = cheapest
        self.stop_over = 0
        if search_data[row_num]["price"] < self.cheapest:
            self.cheapest = search_data[row_num]["price"]
            self.from_airport = f'{search_data[row_num]["cityFrom"]}-{search_data[row_num]["cityCodeFrom"]}'
            self.to_airport = f'{search_data[row_num]["cityTo"]}-{search_data[row_num]["cityCodeTo"]}'
            self.date_from = search_data[row_num]["route"][0]["local_departure"].split("T")[0]
            self.date_to = search_data[row_num]["route"][-1]["local_departure"].split("T")[0]
            self.from_airport_code = search_data[row_num]["cityCodeFrom"]
            self.to_airport_code = search_data[row_num]["cityCodeTo"]
            if len(search_data[row_num]["route"]) > 2:
                self.stop_over += 1
                self.via_city = search_data[row_num]["route"][0]["cityTo"]



