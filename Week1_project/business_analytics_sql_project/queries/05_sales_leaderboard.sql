SELECT 
    sr.rep_name,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM sales_reps sr
JOIN orders o ON sr.sales_rep_id = o.sales_rep_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status = "completed"
GROUP BY sr.rep_name
ORDER BY total_revenue DESC;
