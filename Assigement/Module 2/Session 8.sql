use music_streaming_app;

# Q1. Create a table called Orders with columns: order_id, user_id, payment_method, and amount. Insert at least 8 sample records representing different users and payment methods (like UPI, Card, Wallet, COD).

create table orders1(order_id smallint primary key auto_increment,user_id smallint, payment_method varchar(50), amt bigint);

insert into orders1 (order_id, user_id, payment_method, amt) values(101, 1001, 'UPI', 450.00),(102, 1002, 'Card', 800.00),(103, 1001, 'Wallet', 250.00),(104, 1003, 'COD', 600.00),(105, 1002, 'UPI', 350.00),(106, 1004, 'Card', 1200.00),(107, 1005, 'COD', 180.00),(108, 1003, 'UPI', 500.00);

select * from orders1;

# Q2. Write an SQL query to count how many orders were placed using each payment_method in the Orders table, similar to how Zomato shows payment breakdown in analytics.

select payment_method,count(payment_method) as total from orders1 group by payment_method;

# Q3. Write an SQL query to find the total amount spent by each user_id in the Orders table. Display user_id and their total spend.

select user_id,sum(amt) as total_amount from orders1 group by user_id;

# Q4. Write an SQL query to show only those payment methods where the average order amount is greater than 300, using GROUP BY and HAVING.<br><br><em><strong>Hint:</strong> Use AVG(amount) in your HAVING clause.</em>

select payment_method,avg(amt) as Average_Amt from orders1 group by payment_method having avg(amt) > 300;

# Q5. Explain the difference between WHERE and HAVING by giving one example query for each, using the Orders table. Your examples should show a scenario where WHERE and HAVING filter different things.

/*Difference between WHERE and HAVING
WHERE													HAVING
Filters rows before grouping.							Filters groups after grouping.
Used with individual records.							Used with aggregate functions like SUM(), COUNT(), AVG(), MAX(), MIN().
Cannot use aggregate functions directly.				Commonly used with aggregate functions.*/