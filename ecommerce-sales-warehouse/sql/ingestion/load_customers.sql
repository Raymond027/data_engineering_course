COPY raw.customers
FROM '/data/customers.csv'
DELIMITER ','
CSV HEADER;