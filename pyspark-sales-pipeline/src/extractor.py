from src.schemas import sales_schema


def extract_sales(spark, file_path):

    return (
        spark.read
        .option("header", True)
        .schema(sales_schema)
        .csv(file_path)
    )