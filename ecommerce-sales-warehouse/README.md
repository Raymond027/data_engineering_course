# E-Commerce Sales Warehouse

## Overview
Analytics warehouse for ecommerce sales reporting.

## Architecture
Raw → Staging → Warehouse → Marts

## Tech Stack
- PostgreSQL
- dbt
- Airflow
- Docker

## Setup Instructions
1. docker compose up
2. dbt deps
3. dbt seed
4. dbt run
5. dbt test

## Data Model
- fact_sales
- dim_customer
- dim_product
- dim_date

## Key Metrics
- Revenue
- AOV
- CLV
- Regional Sales