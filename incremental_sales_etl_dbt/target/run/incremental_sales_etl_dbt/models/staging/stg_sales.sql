
      
  
    

  create  table "sales_warehouse"."analytics_staging"."stg_sales__dbt_tmp"
  
  
    as
  
  (
    

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


  );
  
  