from pyspark.sql.functions import col


def validate(df):

    assert df.count() > 0

    assert (
        df.filter(
            col("order_id").isNull()
        ).count() == 0
    )

    assert (
        df.filter(
            col("customer_id").isNull()
        ).count() == 0
    )

    return True