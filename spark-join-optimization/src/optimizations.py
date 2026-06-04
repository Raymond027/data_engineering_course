def baseline_join(customers, orders):
    return customers.join(orders, "customer_id")