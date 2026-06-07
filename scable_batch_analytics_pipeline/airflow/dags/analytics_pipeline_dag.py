from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime


with DAG(
    dag_id="scalable_batch_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    spark_job = BashOperator(
        task_id="run_spark_pipeline",
        bash_command="python src/pipeline.py"
    )

    dbt_run = BashOperator(
        task_id="run_dbt",
        bash_command="cd dbt && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd dbt && dbt test"
    )

    spark_job >> dbt_run >> dbt_test