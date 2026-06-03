from pyspark.sql.functions import (
    col,
    to_date,
    year,
    month
)


def transform_sales(df):

    df = (
        df.withColumn(
            "sale_date",
            to_date(col("sale_date"))
        )
    )

    df = (
        df.withColumn(
            "sales_amount",
            col("quantity") * col("price")
        )
    )

    df = (
        df.withColumn(
            "year",
            year("sale_date")
        )
    )

    df = (
        df.withColumn(
            "month",
            month("sale_date")
        )
    )

    return df