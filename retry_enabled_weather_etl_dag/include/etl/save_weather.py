from pathlib import Path
from datetime import datetime


def save_weather_csv(df):

    output_dir = Path("/opt/airflow/data/weather")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = (
        f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    output_path = output_dir / filename

    df.to_csv(output_path, index=False)

    return str(output_path)