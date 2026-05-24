from sqlalchemy import text
from app.database import engine
from app.logger import setup_logger

logger = setup_logger()

def load_raw_data(df):
    try:
        df.to_sql(
            "raw_crypto",
            engine,
            if_exists="append",
            index=False
        )

        logger.info("Loaded raw data into PostgreSQL")

    except Exception as e:
        logger.error(f"Failed loading raw data: {e}")
        raise

def load_summary_data(df):
    try:
        summary = {
            "total_market_cap": df["market_cap"].sum(),
            "avg_price": df["current_price"].mean(),
            "top_coin": df.sort_values(
                by="market_cap",
                ascending=False
            )["name"].iloc[0]
        }

        from pandas import DataFrame

        summary_df = DataFrame([summary])

        summary_df.to_sql(
            "crypto_summary",
            engine,
            if_exists="append",
            index=False
        )

        logger.info("Loaded summary analytics")

    except Exception as e:
        logger.error(f"Failed loading summary data: {e}")
        raise