def summarize_weather(df):

    summary = {
        "rows": len(df),
        "min_temp": df["temperature_2m"].min(),
        "max_temp": df["temperature_2m"].max(),
        "avg_temp": df["temperature_2m"].mean()
    }

    print(summary)

    return summary