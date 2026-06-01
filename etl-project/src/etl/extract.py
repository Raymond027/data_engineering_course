import requests
import pandas as pd


def extract_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return pd.DataFrame(response.json())