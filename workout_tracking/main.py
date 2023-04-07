import requests, os
from datetime import datetime

#--------exercise---------------------------#

EX_APP_ID = os.environ.get('APP_ID')
EX_APP_KEY = os.environ.get('APP_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : EX_APP_ID,
    "x-app-key" : EX_APP_KEY,
    "Content-Type" : "application/json",
}

exercise_input = input("What exercise did you do and how long?")

exercise_params = {
    "query" : exercise_input,
    "gender" : "female",
    "weight_kg" : 55,
    "height_cm" : 165,
    "age" : 35,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
exercise_response = response.json()


exercises = exercise_response["exercises"][0]
exercise_name = exercises["name"].title()
exercise_duration = exercises["duration_min"]
exercise_calories = exercises["nf_calories"]

#---------------------sheety-------------------#
sheety_endpoint = os.environ.get('SHEET_ENDPOINT')
sheety_header = {
    "Authorization" : os.environ.get('TOKEN'),
    "Content-Type" : "application/json"
}

today = datetime.today().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

sheety_input = {'workout': {
    'date': today,
    'time': time_now,
    'exercise': exercise_name,
    'duration': exercise_duration,
    'calories': exercise_calories,
}
}

sheety_add_row = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_input)
