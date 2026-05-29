import requests
import pandas as pd

URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 34.05,
    "longitude": -118.24,
    "hourly": "temperature_2m"
}


def fetch_weather_data():
    response = requests.get(
        URL,
        params=PARAMS,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"]
    })

    return dfimport requests
import pandas as pd

URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 34.05,
    "longitude": -118.24,
    "hourly": "temperature_2m"
}


def fetch_weather_data():
    response = requests.get(
        URL,
        params=PARAMS,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"]
    })

    return df