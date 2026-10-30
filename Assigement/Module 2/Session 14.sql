use music_streaming_app;

# Q1. Create a table called Orders with columns: order_id, user_id, order_date, and total_amount. Insert at least 7 sample rows representing different users and dates, similar to how food orders appear in Zomato or Swiggy.

create table orders14 (
    order_id int primary key,
    user_id int,
    order_date date,
    total_amount decimal(10,2)
);
insert into orders14 (order_id, user_id, order_date, total_amount)
values
(1, 101, '2026-08-01', 450.00),
(2, 102, '2026-08-01', 320.50),
(3, 101, '2026-08-02', 275.00),
(4, 103, '2026-08-03', 650.75),
(5, 104, '2026-08-04', 199.00),
(6, 102, '2026-08-05', 525.50),
(7, 105, '2026-08-06', 380.00);

select * from orders14;

# Q2. Write a SQL query using the LAG() function to show each user's order_id, order_date, and the total_amount of their previous order (if any), ordered by user and date.<br><br><em><strong>Hint:</strong> Use PARTITION BY user_id and ORDER BY order_date in your window function.</em>

select *, lag(total_amount) over (partition by user_id order by order_date) as Pervious_order_amt from orders14 order by user_id, order_date;

# Q3. Using the same Orders table, write a SQL query with the LEAD() function to display each order_id, order_date, and the next order's total_amount for the same user.

select *, lead(total_amount) over (partition by user_id order by order_date) as Next_Order from orders14 order by user_id, order_date;

# Q4. Write a SQL query to calculate the running total of total_amount for each user, showing order_id, order_date, total_amount, and a column running_total that accumulates the sum as you move through each user's orders.<br><br><em><strong>Hint:</strong> Use SUM(total_amount) OVER (PARTITION BY user_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW).</em>

select *,sum(total_amount) over (partition by user_id order by order_date rows between unbounded preceding and current row) as running_total from orders14 order by user_id , order_date;

# Q5. Write a SQL query to calculate a 3-order moving average of total_amount for each user, showing order_id, order_date, total_amount, and moving_avg columns.<br><br><em><strong>Constraint:</strong> Use SUM() OVER() with ROWS BETWEEN 2 PRECEDING AND CURRENT ROW to compute the moving average.</em>

select *,sum(total_amount) over (partition by user_id order by order_date rows between 2 preceding and current row)/count(*) over (partition by user_id order by order_date rows between 2 preceding and current row) as moving_avg from orders14 order by user_id, order_date;
