import pandas as pd

def transform_weather():
    df = pd.read_csv("data/raw/weather_raw.csv")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df.to_csv("data/raw/weather_raw.csv", index=False)

if __name__ == "__main__":
    transform_weather()