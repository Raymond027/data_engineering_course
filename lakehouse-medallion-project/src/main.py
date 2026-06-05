from src.utils.spark_session import get_spark
from src.utils.constants import *

from src.bronze.bronze_ingestion import load_to_bronze
from src.silver.silver_transformation import *

from src.gold.gold_aggregation import *

spark = get_spark()

# -----------------------------------
# Bronze
# -----------------------------------

load_to_bronze(
    spark,
    f"{RAW_PATH}/customers.csv",
    f"{BRONZE_PATH}/customers"
)

load_to_bronze(
    spark,
    f"{RAW_PATH}/products.csv",
    f"{BRONZE_PATH}/products"
)

load_to_bronze(
    spark,
    f"{RAW_PATH}/orders.csv",
    f"{BRONZE_PATH}/orders"
)

# -----------------------------------
# Read Bronze
# -----------------------------------

customers = (
    spark.read
    .format("delta")
    .load(f"{BRONZE_PATH}/customers")
)

products = (
    spark.read
    .format("delta")
    .load(f"{BRONZE_PATH}/products")
)

orders = (
    spark.read
    .format("delta")
    .load(f"{BRONZE_PATH}/orders")
)

# -----------------------------------
# Silver
# -----------------------------------

silver_customers = clean_customers(customers)

silver_products = clean_products(products)

silver_orders = clean_orders(orders)

(
    silver_customers.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_PATH}/customers")
)

(
    silver_products.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_PATH}/products")
)

(
    silver_orders.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_PATH}/orders")
)

# -----------------------------------
# Gold
# -----------------------------------

product_performance = (
    build_product_performance(
        silver_orders,
        silver_products
    )
)

customer_metrics = (
    build_customer_metrics(
        silver_orders,
        silver_products
    )
)

(
    product_performance.write
    .format("parquet")
    .mode("overwrite")
    .save(
        f"{GOLD_PATH}/product_performance"
    )
)

(
    customer_metrics.write
    .format("parquet")
    .mode("overwrite")
    .save(
        f"{GOLD_PATH}/customer_metrics"
    )
)

print("Pipeline Completed Successfully")