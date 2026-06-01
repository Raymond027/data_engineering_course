from extract import fetch_weather
from transform import transform_weather
from validate import validate_dataframe
from load import save_csv

def run():

    raw_data = fetch_weather()

    df = transform_weather(raw_data)

    validate_dataframe(df)

    save_csv(df)

    print("ETL completed successfully")

if __name__ == "__main__":
    run()