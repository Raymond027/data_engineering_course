from pyspark.sql.functions import (
    sum,
    count,
    col
)


def create_gold(df):

    return (
        df.groupBy("category")
        .agg(
            sum(
                col("quantity") * col("price")
            ).alias("revenue"),

            count("*").alias("orders")
        )
    )