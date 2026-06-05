# Lakehouse Medallion Architecture

## Bronze Layer

Stores raw source data exactly as received.

Format:
- Delta

Tables:
- customers
- products
- orders

---

## Silver Layer

Stores validated and cleaned data.

Transformations:
- Deduplication
- Null Handling
- Standardization

Format:
- Delta

---

## Gold Layer

Business-ready analytics tables.

Tables:
- customer_metrics
- product_performance

Format:
- Parquet