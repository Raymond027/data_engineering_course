from extract import extract_crypto
from transform import transform_crypto
from load import load_crypto

from utils.logger import logger

def run():

    logger.info("ETL started")

    data = extract_crypto()

    df = transform_crypto(data)

    load_crypto(df)

    logger.info("ETL completed")

if __name__ == "__main__":
    run()