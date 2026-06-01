import pandas as pd
from validation_utils import check_freshness
from great_expectations.dataset import PandasDataset

from gx.expectations.weather_suite import validate_weather

def run_validation():

    df = pd.read_csv("data/raw/weather_raw.csv")

    df = PandasDataset(df)

    # Step 1: freshness gate
    check_freshness(df, "timestamp", 2)

    # Step 2: schema + business validation
    result = validate_weather(df)

    print("Validation Completed")
    return result

if __name__ == "__main__":
    run_validation()