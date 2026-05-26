WITH sales AS (

    SELECT *
    FROM "sales_warehouse"."analytics_staging"."stg_sales"

),

aggregated AS (

    SELECT
        order_date,
        product_id,

        COUNT(order_id) AS total_orders,
        SUM(quantity) AS total_quantity,
        SUM(total_amount) AS total_revenue,
        AVG(total_amount) AS avg_order_value

    FROM sales
    GROUP BY 1, 2

)

SELECT *
FROM aggregated