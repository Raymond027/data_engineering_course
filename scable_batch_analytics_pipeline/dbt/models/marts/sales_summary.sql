select
    category,
    sum(quantity * price) as revenue,
    count(*) as orders
from {{ ref('stg_sales') }}
group by category