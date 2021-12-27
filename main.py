import os
from dotenv import load_dotenv, find_dotenv
import requests
from datetime import datetime

load_dotenv(find_dotenv())

today = datetime.now()


# constants
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%X")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTHORIZATION = os.environ.get("SHEETY_AUTHERIZATION")

exercise_params = {
    "query": input("Tell me which exercises you did: ")
}


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise_post_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
exercise_post_text = exercise_post_response.json()

for exercise_num in exercise_post_text["exercises"]:
    sheety_params = {
        "tabellenblatt1": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise_num["name"].title(),
            "duration": exercise_num["duration_min"],
            "calories": exercise_num["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": SHEETY_AUTHORIZATION,
    }

    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    print(sheety_post_response.json())


