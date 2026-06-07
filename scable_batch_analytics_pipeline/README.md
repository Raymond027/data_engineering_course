# Scalable Batch Analytics Pipeline

## Architecture

Bronze → Silver → Gold

## Technologies

- PySpark
- Delta Lake
- Airflow
- dbt
- Parquet
- Pytest

## Features

- Incremental Processing
- Partitioned Storage
- Data Validation
- Logging
- Airflow Orchestration
- dbt Modeling
- Medallion Architecture

## Execution

python src/pipeline.py

dbt run

dbt test

airflow scheduler

airflow webserver

## Testing

pytest tests/