from pyspark.sql.functions import col

def clean_data(customers, orders, products):
    customers = customers.dropna(subset=["customer_id"])
    orders = orders.dropna(subset=["order_id"])
    products = products.dropna(subset=["product_id"])
    
    return customers, orders, products