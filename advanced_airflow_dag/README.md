# Advanced Production Airflow DAG

## Overview

Production-style Apache Airflow project demonstrating:

- Dynamic task generation
- Task Groups
- Retry handling
- SLA monitoring
- Dependency chains
- Alerting
- DAG validation testing

---

## Architecture

Extract
↓
Bronze
↓
Silver
↓
Gold
↓
Validation
↓
Reporting

---

## Run Airflow

```bash
airflow standalone
```

Place DAG file inside:

```bash
AIRFLOW_HOME/dags
```

Run tests:

```bash
pytest tests/
```

---

## Features

- Dynamic DAG design
- Production retry strategy
- SLA monitoring
- Failure alert hooks
- Unit testing
- Modular project structure