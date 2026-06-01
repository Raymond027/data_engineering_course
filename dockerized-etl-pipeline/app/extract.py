import requests
from config import API_URL, LATITUDE, LONGITUDE

def fetch_weather():

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current_weather": True
    }

    response = requests.get(API_URL, params=params)

    response.raise_for_status()

    return response.json()