import requests
import pandas as pd

def extract_weather():
    data = [
        {"city": "NYC", "temperature": 22, "humidity": 55, "timestamp": "2026-06-01T10:00:00Z", "source": "api"},
        {"city": "LA", "temperature": 28, "humidity": 40, "timestamp": "2026-06-01T10:00:00Z", "source": "api"}
    ]

    df = pd.DataFrame(data)
    df.to_csv("data/raw/weather_raw.csv", index=False)

if __name__ == "__main__":
    extract_weather()