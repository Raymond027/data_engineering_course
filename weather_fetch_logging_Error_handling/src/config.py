import os
from dotenv import load_dotenv

load_dotenv()


#API KEYS
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    raise ValueError("OpenWEATHER_API_KEY is missing in .env")

# DEFAULTS
DEFAULT_CITY = os.getenv("DEFAULT_CITY_LIST", "New York")

# URL
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)

CITY_LIST=["New York", "London", "Tokyo", "InvalidCity"]

TIMEOUT = 5 # seconds
MAX_RETRIES = 3
RETRY_DELAY = 2 # seconds
LOG_FILE = "weather.log"