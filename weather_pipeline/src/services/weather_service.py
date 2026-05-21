import requests
from datetime import datetime

from src.config.settings import OPENWEATHER_API_KEY
from src.utils.logger import logger


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str) -> dict | None:
    """
    Fetch weather data for a city from OpenWeatherMap API.
    """

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        logger.info(f"Fetching weather data for {city}")

        response = requests.get(BASE_URL, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "timestamp": datetime.utcnow()
        }

        logger.info(f"Successfully fetched data for {city}")

        return weather_info

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed for {city}: {e}")
        return None