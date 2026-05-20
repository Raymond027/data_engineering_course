import requests
from config import ( CRYPTO_URL )

def get_crypto_prices():
    crypto_response = requests.get(CRYPTO_URL)
    crypto_response.raise_for_status()
    return crypto_response.json()
   

