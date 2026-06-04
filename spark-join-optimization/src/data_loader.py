def load_data(spark):
    customers = spark.read.option("header", True).csv("data/raw/customers.csv")
    orders = spark.read.option("header", True).csv("data/raw/orders.csv")
    products = spark.read.option("header", True).csv("data/raw/products.csv")
    
    return customers, orders, products