SELECT
    o.order_date,
    SUM(oi.quantity * oi.unit_price) AS daily_revenue

FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = "completed"
GROUP BY o.order_date
ORDER BY o.order_date DESC;