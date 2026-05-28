import pandas as pd
from datetime import datetime

def transform_data(raw_data):

    rows = []

    ingestion_time = datetime.utcnow()

    for crypto_name, values in raw_data.items():

        rows.append({
            "crypto_name": crypto_name,
            "price_usd": values["usd"],
            "ingestion_time_utc": ingestion_time
        })

    df = pd.DataFrame(rows)

    return df