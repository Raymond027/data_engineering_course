from airflow import DAG
from airflow.decorators import task
from airflow.sensors.time_sensor import TimeSensor
from datetime import datetime, timedelta

from include.etl.fetch_weather import fetch_weather_data
from include.etl.validate_weather import validate_weather_data
from include.etl.save_weather import save_weather_csv
from include.etl.summarize_weather import summarize_weather


default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,

    # Retry configuration
    "retries": 3,
    "retry_delay": timedelta(minutes=1),

    # Optional production settings
    "email_on_failure": False,
    "email_on_retry": False
}


with DAG(
    dag_id="retry_enabled_weather_etl",
    start_date=datetime(2026, 5, 28),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["weather", "etl", "retries"]
) as dag:

    # Step 1 — Sensor Task
    wait_for_api_window = TimeSensor(
        task_id="wait_for_api_window",
        target_time=datetime.strptime("06:00", "%H:%M").time()
    )

    @task
    def fetch_task():

        df = fetch_weather_data()

        return df.to_json()

    @task
    def validate_task(weather_json):

        import pandas as pd

        df = pd.read_json(weather_json)

        validate_weather_data(df)

        return weather_json

    @task
    def save_task(weather_json):

        import pandas as pd

        df = pd.read_json(weather_json)

        path = save_weather_csv(df)

        return path

    @task
    def summary_task(weather_json):

        import pandas as pd

        df = pd.read_json(weather_json)

        summarize_weather(df)

    weather_data = fetch_task()

    validated_data = validate_task(weather_data)

    saved_file = save_task(validated_data)

    summary = summary_task(validated_data)

    (
        wait_for_api_window
        >> weather_data
        >> validated_data
        >> [saved_file, summary]
    )