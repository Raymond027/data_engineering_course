from etl.utils.database import engine

def load_crypto(df):

    df.to_sql(
        "crypto_prices",
        engine,
        if_exists="append",
        index=False
    )