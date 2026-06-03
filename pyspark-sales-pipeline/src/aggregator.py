from pyspark.sql.functions import (
    sum,
    avg,
    count,
    round
)


def sales_summary(df):

    return (
        df.groupBy("year", "month")
        .agg(
            round(sum("sales_amount"), 2)
            .alias("total_sales"),

            round(avg("sales_amount"), 2)
            .alias("avg_sales"),

            count("*")
            .alias("transactions")
        )
    )


def product_summary(df):

    return (
        df.groupBy("product")
        .agg(
            round(sum("sales_amount"), 2)
            .alias("revenue")
        )
    )


def region_summary(df):

    return (
        df.groupBy("region")
        .agg(
            round(sum("sales_amount"), 2)
            .alias("revenue")
        )
    )