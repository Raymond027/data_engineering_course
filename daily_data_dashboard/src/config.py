import os
from dotenv import load_dotenv

load_dotenv()

#API KEYS
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    raise ValueError("OpenWEATHER_API_KEY is missing in .env")

# DEFAULTS
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Las Vegas")

# URL
GITHUB_API_URL = "https://api.github.com/users/Raymond227"

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)

CRYPTO_URL = (
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
)

