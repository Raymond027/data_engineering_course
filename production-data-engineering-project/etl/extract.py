import requests
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(5)
)
def extract_crypto():

    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()