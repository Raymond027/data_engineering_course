import yaml

from src.logger import get_logger
from src.spark_session import create_spark_session

from src.extractor import extract_sales
from src.validator import validate_sales
from src.transformer import transform_sales

from src.aggregator import (
    sales_summary,
    product_summary,
    region_summary
)

from src.loader import save_parquet


def load_config():

    with open("config/config.yaml") as file:
        return yaml.safe_load(file)


def main():

    config = load_config()

    logger = get_logger()

    spark = create_spark_session(
        config["app_name"]
    )

    logger.info("Pipeline Started")

    sales_df = extract_sales(
        spark,
        config["input_path"]
    )

    sales_df = validate_sales(sales_df)

    sales_df = transform_sales(sales_df)

    monthly_df = sales_summary(sales_df)

    product_df = product_summary(sales_df)

    region_df = region_summary(sales_df)

    save_parquet(
        monthly_df,
        config["output"]["sales_summary"]
    )

    save_parquet(
        product_df,
        config["output"]["product_summary"]
    )

    save_parquet(
        region_df,
        config["output"]["region_summary"]
    )

    logger.info("Pipeline Completed")

    spark.stop()


if __name__ == "__main__":
    main()