import pandas as pd


def transform_data(df: pd.DataFrame):

    return df[
        [
            "id",
            "symbol",
            "current_price",
            "market_cap"
        ]
    ]