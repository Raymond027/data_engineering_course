SELECT
    p.product_name,
    SUM(oi.quantity * oi.unit_price) AS total_revenue

FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.status = "completed"
GROUP BY p.product_name
ORDER BY total_revenue DESC;