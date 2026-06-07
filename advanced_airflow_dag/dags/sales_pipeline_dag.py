from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from monitoring.alerts import task_failure_alert

TABLES = [
    "customers",
    "orders",
    "products"
]

default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
    "on_failure_callback": task_failure_alert
}


def extract(table):
    print(f"Extracting data from {table}")


def bronze_load(table):
    print(f"Loading {table} into Bronze layer")


def silver_transform(table):
    print(f"Transforming {table} into Silver layer")


def gold_aggregate(table):
    print(f"Creating Gold aggregates for {table}")


def validate():
    print("Running data quality validation")


def reporting():
    print("Generating business reports")


with DAG(
    dag_id="advanced_production_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule="0 2 * * *",
    catchup=False,
    tags=["production", "etl"]
) as dag:

    with TaskGroup(group_id="extract_group") as extract_group:
        for table in TABLES:
            PythonOperator(
                task_id=f"extract_{table}",
                python_callable=extract,
                op_kwargs={"table": table},
                sla=timedelta(minutes=30)
            )

    with TaskGroup(group_id="bronze_group") as bronze_group:
        for table in TABLES:
            PythonOperator(
                task_id=f"bronze_{table}",
                python_callable=bronze_load,
                op_kwargs={"table": table}
            )

    with TaskGroup(group_id="silver_group") as silver_group:
        for table in TABLES:
            PythonOperator(
                task_id=f"silver_{table}",
                python_callable=silver_transform,
                op_kwargs={"table": table}
            )

    with TaskGroup(group_id="gold_group") as gold_group:
        for table in TABLES:
            PythonOperator(
                task_id=f"gold_{table}",
                python_callable=gold_aggregate,
                op_kwargs={"table": table}
            )

    validation_task = PythonOperator(
        task_id="data_validation",
        python_callable=validate
    )

    reporting_task = PythonOperator(
        task_id="business_reporting",
        python_callable=reporting
    )

    (
        extract_group
        >> bronze_group
        >> silver_group
        >> gold_group
        >> validation_task
        >> reporting_task
    )