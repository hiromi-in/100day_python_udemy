import requests

class DataManager:

    def __init__(self, sheet_token, sheet_endpoint):
        self.SHEETY_TOKEN = sheet_token
        self.SHEETY_GET_ENDPOINT = sheet_endpoint

        self.sheety_headers = {
            "Authorization": self.SHEETY_TOKEN,
            "Content-Type": "application/json",
        }
        self.all_data = requests.get(url=self.SHEETY_GET_ENDPOINT, headers=self.sheety_headers)
        self.all_data.raise_for_status()
        self.all_data = self.all_data.json()["prices"]


    def get_city_name(self, row_num):
         return self.all_data[row_num-1]["city"]

    def add_city_code(self, city_name, row_num, city_code):
        row_id = self.all_data[row_num-1]["id"]

        sheety_add = {
            'price': {
                'city': city_name,
                'iataCode': city_code,
                'lowestPrice': self.all_data[row_num-1]['lowestPrice'],
                'id': row_id,
            }
        }

        response = requests.put(
            url=f"{self.SHEETY_GET_ENDPOINT}/{row_id}", json=sheety_add,
            headers=self.sheety_headers)
        response.raise_for_status()