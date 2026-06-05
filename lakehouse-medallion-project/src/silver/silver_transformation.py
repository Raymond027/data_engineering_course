from pyspark.sql.functions import lower

def clean_customers(df):

    return (
        df.dropDuplicates(["customer_id"])
          .dropna()
          .withColumn(
              "email",
              lower("email")
          )
    )


def clean_products(df):

    return (
        df.dropDuplicates(["product_id"])
          .dropna()
    )


def clean_orders(df):

    return (
        df.dropDuplicates(["order_id"])
          .dropna()
    )