from pyspark.sql.functions import col


def create_silver(df):

    return (
        df.dropDuplicates(["order_id"])
        .filter(col("quantity") > 0)
        .filter(col("price") > 0)
    )