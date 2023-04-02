import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
draft = response.json()

question_data = draft["results"]