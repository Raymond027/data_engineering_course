SELECT
    order_id,
    customer_id,
    order_date::DATE AS order_date,
    order_status
FROM raw.orders
WHERE order_status = 'COMPLETED';