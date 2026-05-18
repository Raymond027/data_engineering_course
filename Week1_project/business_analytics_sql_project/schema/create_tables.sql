CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(150),
    signup_date DATE,
    country VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    sales_rep_id INT,
    status VARCHAR(30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price NUMERIC(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE sales_reps (
    sales_rep_id INT PRIMARY KEY,
    rep_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE spotify_tracks (
    track_id VARCHAR(50),
    track_name VARCHAR(200),
    artist_name VARCHAR(150),
    album_name VARCHAR(150),
    release_date DATE,
    popularity INT,
    duration_ms INT,
    explicit BOOLEAN
);


INSERT INTO customers VALUES
    (1, 'John Smith', 'john@example.com', '2026-01-05', 'USA'),
    (2, 'Sarah Lee', 'sarah@example.com', '2026-01-10', 'USA'),
    (3, 'Michael Brown', 'michael@example.com', '2026-02-01', 'Canada'),
    (4, 'Emma Wilson', 'emma@example.com', '2026-02-12', 'UK'),
    (5, 'David Ky', 'david@example.com', '2026-03-03', 'USA');

INSERT INTO products VALUES
    (101, 'Laptop', 'Electronics', 1200.00),
    (102, 'Headphones', 'Electronics', 150.00),
    (103, 'Office Chair', 'Furniture', 300.00),
    (104, 'Desk', 'Furniture', 450.00),
    (105, 'Coffee Mug', 'Kitchen', 20.00);


INSERT INTO sales_reps VALUES
    (1, 'Alice Johnson', 'West'),
    (2, 'Robert Miller', 'East'),
    (3, 'Nancy Davis', 'Central');

INSERT INTO orders VALUES
    (1001, 1, '2026-03-01', 1, 'completed'),
    (1002, 2, '2026-03-01', 2, 'completed'),
    (1003, 1, '2026-03-05', 1, 'completed'),
    (1004, 3, '2026-03-10', 3, 'completed'),
    (1005, 4, '2026-03-11', 2, 'cancelled'),
    (1006, 2, '2026-04-01', 2, 'completed'),
    (1007, 5, '2026-04-02', 1, 'completed'),
    (1008, 1, '2026-04-05', 3, 'completed');


INSERT INTO order_items VALUES
    (1, 1001, 101, 1, 1200.00),
    (2, 1001, 102, 2, 150.00),
    (3, 1002, 103, 1, 300.00),
    (4, 1003, 105, 5, 20.00),
    (5, 1004, 104, 1, 450.00),
    (6, 1006, 101, 1, 1200.00),
    (7, 1007, 102, 3, 150.00),
    (8, 1008, 105, 10, 20.00);