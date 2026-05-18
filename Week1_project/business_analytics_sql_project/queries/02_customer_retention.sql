SELECT
    c.customer_name,
    COUNT(DISTINCT DATE_FORMAT(o.order_date, "%Y-%M")) AS active_months

FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY active_months DESC;
