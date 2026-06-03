from pyspark.sql.functions import col


def validate_sales(df):

    df = df.filter(col("sale_id").isNotNull())

    df = df.filter(col("quantity") > 0)

    df = df.filter(col("price") > 0)

    return df