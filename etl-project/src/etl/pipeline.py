from etl.extract import extract_crypto_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():

    raw_df = extract_crypto_data()

    transformed_df = transform_data(raw_df)

    load_data(transformed_df)


if __name__ == "__main__":
    run_pipeline()