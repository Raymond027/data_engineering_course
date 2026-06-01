import pandas as pd

def transform_weather(data):

    weather = data["current_weather"]

    df = pd.DataFrame([{
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "winddirection": weather["winddirection"],
        "time": weather["time"]
    }])

    return df