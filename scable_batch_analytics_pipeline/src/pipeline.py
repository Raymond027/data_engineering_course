from src.utils.spark_session import create_spark_session
from src.ingestion.bronze_loader import load_bronze
from src.transformations.silver_transform import create_silver
from src.transformations.gold_transform import create_gold
from src.validation.validator import validate


def run():

    spark = create_spark_session()

    bronze = load_bronze(
        spark,
        "data/raw/ecommerce_sales.csv"
    )

    validate(bronze)

    bronze.write.mode(
        "append"
    ).partitionBy(
        "order_date"
    ).parquet(
        "data/bronze"
    )

    silver = create_silver(bronze)

    silver.write.mode(
        "overwrite"
    ).partitionBy(
        "order_date"
    ).parquet(
        "data/silver"
    )

    gold = create_gold(silver)

    gold.write.mode(
        "overwrite"
    ).parquet(
        "data/gold"
    )

    spark.stop()


if __name__ == "__main__":
    run()