def validate_weather_data(df):

    if df.empty:
        raise ValueError("Weather dataframe is empty")

    required_columns = [
        "time",
        "temperature_2m"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return True