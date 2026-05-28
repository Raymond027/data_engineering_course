import requests
from src.utils.logger import get_logger

logger = get_logger(__name__)

def fetch_crypto_prices(symbols: list):

    ids = ",".join(symbols)

    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={ids}&vs_currencies=usd"
    )

    logger.info(f"Calling API: {url}")

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()