SELECT
    customer_id,
    TRIM(full_name) AS full_name,
    LOWER(email) AS email,
    country,
    city
FROM raw.customers
WHERE customer_id IS NOT NULL;