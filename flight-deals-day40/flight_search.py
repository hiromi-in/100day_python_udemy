import requests

class FlightSearch:

    def __init__(self, apikey):
        self.TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.TEQUILA_API_KEY = apikey
        self.tequila_header = {
            "Content-Type": "application/json",
            "apikey": self.TEQUILA_API_KEY,
        }

        self.flight_type = "round"
        self.adults = 2
        self.infants = 2
        self.only_working_days = False
        self.only_weekends = False
        self.partner_market = "us"
        self.max_stopovers = 2
        self.max_sector_stopovers = 1
        self.vehicle_type = "aircraft"
        self.stop_overs = 0
        self.via_city = ""

    def search_flight(self, fly_from, fly_to, date_from, date_to, return_from, return_to):

        tequila_flight_search_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "flight_type": self.flight_type,
            "adults": self.adults,
            "infants": self.infants,
            "only_working_days": self.only_working_days,
            "only_weekends": self.only_weekends,
            "partner_market": self.partner_market,
            "max_stopovers": self.max_stopovers,
            "max_sector_stopovers": self.max_sector_stopovers,
            "vehicle_type": self.vehicle_type,
        }

        response = requests.get(url=self.TEQUILA_SEARCH_ENDPOINT, headers=self.tequila_header,
                                params=tequila_flight_search_params)

        response.raise_for_status()

        return response.json()


