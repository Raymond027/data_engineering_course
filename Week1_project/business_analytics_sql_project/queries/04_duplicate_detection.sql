SELECT 
    c.email,
    COUNT(*) AS duplicated_email_count
FROM customers c
GROUP BY c.email
HAVING duplicated_email_count > 1;


-- detect duplicate orders
SELECT
    o.customer_id,
    COUNT(*) AS duplicated_orders
FROM orders o
GROUP BY o.customer_id, o.order_date
HAVING duplicated_orders > 1;