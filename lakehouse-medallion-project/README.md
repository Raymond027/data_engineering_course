# Lakehouse Medallion Architecture

A production-style Data Engineering project implementing the Medallion Architecture.

## Architecture

Raw CSV
    ↓
Bronze Layer (Delta)
    ↓
Silver Layer (Delta)
    ↓
Gold Layer (Parquet)
    ↓
Analytics

## Technologies

- PySpark
- Delta Lake
- Parquet
- Data Quality Checks
- Medallion Architecture

## Run

python src/main.py