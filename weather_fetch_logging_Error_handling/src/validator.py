def validate_weather_response(data: dict) -> bool:
    """
    Ensures API response has required fields.
    Prevents downstream crashes.
    """
    try:
        return (
            "main" in data
            and "temp" in data["main"]
            and "weather" in data
            and len(data["weather"]) > 0
        )
    except Exception:
        return False