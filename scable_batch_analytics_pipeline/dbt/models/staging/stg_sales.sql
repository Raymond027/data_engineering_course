select
    order_id,
    customer_id,
    category,
    quantity,
    price,
    country
from read_parquet('data/silver/*.parquet')