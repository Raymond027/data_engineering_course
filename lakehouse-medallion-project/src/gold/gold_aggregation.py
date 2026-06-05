from pyspark.sql.functions import sum


def build_product_performance(
    orders,
    products
):

    sales = orders.join(
        products,
        "product_id"
    )

    return (
        sales.groupBy("product_id")
             .agg(
                 sum(
                     sales.quantity *
                     sales.price
                 ).alias("revenue")
             )
    )


def build_customer_metrics(
    orders,
    products
):

    sales = orders.join(
        products,
        "product_id"
    )

    return (
        sales.groupBy("customer_id")
             .agg(
                 sum(
                     sales.quantity *
                     sales.price
                 ).alias("total_spend")
             )
    )