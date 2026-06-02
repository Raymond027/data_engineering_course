import pandas as pd
from datetime import datetime

def transform_crypto(data):

    df = pd.DataFrame(data)

    cols = [
        "id",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume"
    ]

    df = df[cols]

    df["ingestion_timestamp"] = datetime.utcnow()

    return df