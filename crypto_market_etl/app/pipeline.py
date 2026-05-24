from app.extract import fetch_crypto_data
from app.transform import clean_crypto_data
from app.load import load_raw_data, load_summary_data
from app.logger import setup_logger

logger = setup_logger()

def run_pipeline():
    try:
        logger.info("Starting ETL pipeline")

        raw_data = fetch_crypto_data()

        clean_df = clean_crypto_data(raw_data)

        load_raw_data(clean_df)

        load_summary_data(clean_df)

        logger.info("ETL pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise