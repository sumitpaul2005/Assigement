use music_streaming_app;

# 1. Create a table called Orders with columns: order_id, user_name, total_amount, and order_date. Insert 5 sample rows with different users and order amounts, including at least one NULL value for total_amount.

create table Orders (orderId smallint primary key auto_increment,user_name varchar(50), total_amt bigint, order_date date);

INSERT INTO Orders (user_name, total_amt, order_date)
VALUES
('Amit', 1200.50, '2026-07-01'),
('Amit', 850.00, '2026-07-02'),
('Priya', 650.75, '2026-07-03'),
('Priya', 999.99, '2026-07-04'),
('Rahul', NULL, '2026-07-05'),
('Rahul', 1500.00, '2026-07-06'),
('Sneha', 450.25, '2026-07-07'),
('Sneha', NULL, '2026-07-08'),
('Vikram', 1750.80, '2026-07-09'),
('Amit', Null, '2026-07-10');

select * from Orders;

# 2. Write a SQL query to count how many orders were placed by each user in the Orders table, displaying user_name and the number of orders as order_count.

select user_name,count(user_name) as Order_Count from Orders group by user_name; 

# 3. Write a SQL query to calculate the average total_amount of all orders in the Orders table, making sure to ignore any NULL values.

select avg(total_amt) as Average from Orders where total_amt is not Null;

# 4. Suppose you are building a Flipkart-style dashboard: Write a SQL query to find the highest and lowest order amounts (MAX and MIN) from the Orders table, and display both values in a single result row.

select max(total_amt) as Maximum , min(total_amt) as Minimum from Orders;

# 5. Write a SQL query to calculate the total sales (SUM of total_amount) for all orders, but only include orders where total_amount is not NULL.<br><br><em><strong>Hint:</strong> Use a WHERE clause to filter out NULL values before applying the SUM function.</em>

select SUM(total_amt) AS total_sales FROM Orders WHERE total_amt IS NOT NULL;