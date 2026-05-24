import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from app.config import Config
from app.logger import setup_logger

logger = setup_logger()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_crypto_data():
    try:
        response = requests.get(
            Config.COINGECKO_URL,
            params=Config.API_PARAMS,
            timeout=10
        )

        response.raise_for_status()

        logger.info("Successfully fetched crypto data")

        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise