import pandas as pd
from app.logger import setup_logger

logger = setup_logger()

def clean_crypto_data(data):
    df = pd.DataFrame(data)

    required_columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df = df[required_columns]

    df = df.dropna()

    df = df[df["current_price"] > 0]

    df = df.rename(columns={
        "id": "coin_id"
    })

    logger.info(f"Cleaned dataset contains {len(df)} rows")

    return df