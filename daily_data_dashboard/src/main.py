import requests
from src.config import (
    OPENWEATHER_API_KEY,
    GITHUB_API_URL,
    OPENWEATHER_URL,
    CRYPTO_URL,
    DEFAULT_CITY,
)

# GITHUB API

github_response = requests.get(GITHUB_API_URL)

print(github_response)

if github_response.status_code == 200:
    github_data = github_response.json()
    print("GitHub User:")
    print(github_data["login"])
    print(github_data["public_repos"])
else:
    print("Request Failed", github_response.status_code)

# CRYPTO API
crypto_response = requests.get(CRYPTO_URL)

if crypto_response.status_code  == 200:
    crypto_data = crypto_response.json()
    print(crypto_data)


# WEATHER API
params = {
    "q": DEFAULT_CITY,
    "appid": OPENWEATHER_API_KEY,
    "units": "metric"
}
weather_response = requests.get(OPENWEATHER_URL, params)

if weather_response.status_code  == 200:
    weather_data = weather_response.json()
    print(weather_data["main"]["temp"])

 