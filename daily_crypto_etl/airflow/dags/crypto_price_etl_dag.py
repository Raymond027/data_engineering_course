from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import save_to_csv
from src.summary.reporting import generate_summary
from src.utils.config import OUTPUT_DIR

default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="daily_crypto_price_etl",
    default_args=default_args,
    description="Daily crypto ETL pipeline",
    schedule="@daily",
    start_date=datetime(2026, 5, 1),
    catchup=False,
    tags=["crypto", "etl", "daily"]
) as dag:

    def extract_task(ti):

        raw_data = extract_data()

        ti.xcom_push(key="raw_crypto_data", value=raw_data)

    def transform_task(ti):

        raw_data = ti.xcom_pull(
            key="raw_crypto_data",
            task_ids="extract_crypto_prices"
        )

        df = transform_data(raw_data)

        ti.xcom_push(
            key="transformed_data",
            value=df.to_json()
        )

    def load_task(ti):

        import pandas as pd

        json_data = ti.xcom_pull(
            key="transformed_data",
            task_ids="transform_crypto_prices"
        )

        df = pd.read_json(json_data)

        path = save_to_csv(df, OUTPUT_DIR)

        ti.xcom_push(key="output_path", value=path)

    def summary_task(ti):

        import pandas as pd

        json_data = ti.xcom_pull(
            key="transformed_data",
            task_ids="transform_crypto_prices"
        )

        df = pd.read_json(json_data)

        summary = generate_summary(df)

        print(summary)

    extract_operator = PythonOperator(
        task_id="extract_crypto_prices",
        python_callable=extract_task
    )

    transform_operator = PythonOperator(
        task_id="transform_crypto_prices",
        python_callable=transform_task
    )

    load_operator = PythonOperator(
        task_id="load_crypto_prices_csv",
        python_callable=load_task
    )

    summary_operator = PythonOperator(
        task_id="print_summary",
        python_callable=summary_task
    )

    extract_operator >> transform_operator >> load_operator >> summary_operator