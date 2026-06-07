SELECT
    DATE(created_at) AS order_date,
    COUNT(*) AS total_orders,
    SUM(order_amount) AS revenue
FROM silver_orders
GROUP BY DATE(created_at);