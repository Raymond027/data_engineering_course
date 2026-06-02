from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    etl = BashOperator(
        task_id="run_etl",
        bash_command="python etl/pipeline.py"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="dbt test"
    )

    etl >> dbt_run >> dbt_test