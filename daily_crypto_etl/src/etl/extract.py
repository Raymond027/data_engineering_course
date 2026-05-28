from src.api.crypto_api import fetch_crypto_prices
from src.utils.config import CRYPTO_SYMBOLS

def extract_data():

    data = fetch_crypto_prices(CRYPTO_SYMBOLS)

    return data