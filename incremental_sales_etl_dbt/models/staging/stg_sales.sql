{{
    config(
        materialized='incremental',
        unique_key='order_id',
        on_schema_change='sync_all_columns'
    )
}}

WITH source_data AS (

    SELECT
        order_id,
        order_date,
        customer_id,
        product_id,
        quantity,
        price,
        quantity * price AS total_amount,
        created_at

    FROM raw.sales_raw

)

SELECT *
FROM source_data

{% if is_incremental() %}

WHERE created_at >
(
    SELECT COALESCE(MAX(created_at), '1900-01-01')
    FROM {{ this }}
)

{% endif %}