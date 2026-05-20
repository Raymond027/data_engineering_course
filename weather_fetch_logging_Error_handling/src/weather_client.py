import requests
import time
from config import OPENWEATHER_URL,OPENWEATHER_API_KEY, MAX_RETRIES, TIMEOUT, RETRY_DELAY
from logger import get_logger
from validator import validate_weather_response

logger = get_logger()

class WeatherClient:

    def fetch_weather(self, city: str):
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        attempt = 0

        while attempt < MAX_RETRIES:
            try:
                logger.info(f"Attempt {attempt + 1} for city: {city}")

                response = requests.get(
                    OPENWEATHER_URL,
                    params=params,
                    timeout=TIMEOUT
                )

                response.raise_for_status()
                data = response.json()

                # Validate structure
                if not validate_weather_response(data):
                    logger.warning(f"Incomplete data received for {city}")
                    return None

                logger.info(f"Success fetching data for {city}")
                return self._parse(data, city)

            except requests.exceptions.Timeout:
                logger.warning(f"Timeout error for {city}")

            except requests.exceptions.ConnectionError:
                logger.warning(f"Connection error for {city}")

            except requests.exceptions.HTTPError as e:
                logger.warning(f"HTTP error for {city}: {str(e)}")
                break  # don't retry for 4xx/5xx API errors

            except ValueError:
                logger.warning(f"Invalid JSON response for {city}")

            except Exception as e:
                logger.error(f"Unexpected error for {city}: {str(e)}")
                break

            attempt += 1
            time.sleep(RETRY_DELAY)

        logger.error(f"Failed to fetch weather for {city} after retries")
        return None

    def _parse(self, data: dict, city: str):
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }