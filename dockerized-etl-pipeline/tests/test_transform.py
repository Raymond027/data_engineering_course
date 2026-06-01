from app.transform import transform_weather

def test_transform():

    sample = {
        "current_weather": {
            "temperature": 25,
            "windspeed": 5,
            "winddirection": 90,
            "time": "2026"
        }
    }

    df = transform_weather(sample)

    assert len(df) == 1