select
    customer_id,
    count(*) as total_orders,
    sum(quantity * price) as lifetime_value
from {{ ref('stg_sales') }}
group by customer_id