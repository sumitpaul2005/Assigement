use music_streaming_app;

# Q1. Create a CTE using the WITH clause to select all products with a rating above 4.5 from a 'Products' table, similar to how Flipkart or Myntra might highlight top-rated items.

CREATE TABLE Product (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    rating DECIMAL(2,1)
);

INSERT INTO Product VALUES
(101, 'Nike Running Shoes', 'Footwear', 4999.00, 4.8),
(102, 'Samsung Galaxy M16', 'Mobile', 15999.00, 4.6),
(103, 'Boat Headphones', 'Electronics', 1999.00, 4.3),
(104, 'Levis Jeans', 'Clothing', 2499.00, 4.7),
(105, 'Puma T-Shirt', 'Clothing', 999.00, 4.2);

with TopRatedProduct as (select * from Product where rating > 4.5) select * from TopRatedProduct;

# Q2. Rewrite a query that finds all restaurants in 'Ahmedabad' with delivery charges under 50 from a 'Restaurants' table, first using a subquery and then using a CTE. Compare both queries for readability.<br><br><em><strong>Hint:</strong> Focus on making the CTE version cleaner and easier to understand.</em>

create table restaurant2 (
    restaurant_id int,
    restaurant_name varchar(100),
    city varchar(50),
    delivery_charge decimal(5,2),
    rating decimal(2,1)
);

insert into restaurant2 values
(1, 'pizza hut', 'ahmedabad', 40.00, 4.5),
(2, 'domino''s', 'ahmedabad', 60.00, 4.3),
(3, 'kfc', 'ahmedabad', 45.00, 4.6),
(4, 'mcdonald''s', 'surat', 35.00, 4.4),
(5, 'burger king', 'ahmedabad', 30.00, 4.2);

select * from (select * from restaurant2 where delivery_charge < 50) as AhmedabadRestaurent where city = 'Ahmedabad';

with AhmedabadRestaurent as (select * from restaurant2 where delivery_charge < 50) select * from AhmedabadRestaurent where city = 'Ahmedabad';

# Q3. Using two CTEs in a single query, find the top 3 most-followed users and the top 3 most-liked posts from a 'Users' and 'Posts' table (think Instagram-style data). Output both lists in the same result set.

create table usersIns (
    user_id int,
    user_name varchar(50),
    followers int
);

create table postsIns (
    post_id int,
    user_id int,
    post_title varchar(100),
    likes int
);
insert into usersIns values
(1, 'rahul', 2500),
(2, 'priya', 4800),
(3, 'amit', 3200),
(4, 'neha', 5500),
(5, 'karan', 4100);

insert into postsIns values
(101, 1, 'travel vlog', 950),
(102, 2, 'food reel', 1800),
(103, 3, 'fitness tips', 1200),
(104, 4, 'nature photography', 2200),
(105, 5, 'tech review', 1600);

with top_users as (
    select
        user_id,
        user_name,
        followers
    from usersIns
    order by followers desc
    limit 3
),
top_posts as (
    select
        post_id,
        post_title,
        likes
    from postsIns
    order by likes desc
    limit 3
)
select 'top user' as type, user_name as name, followers as value
from top_users union all select 'top post' as type, post_title as name, likes as value from top_posts;

# Q4. Write a recursive CTE that generates a list of dates for the next 7 days starting from today, similar to how BookMyShow shows available dates for movie bookings.<br><br><em><strong>Hint:</strong> Use a base case for today and recursion to add one day at a time.</em>

with recursive next_7_days as (select current_date() as Booking_date, 1 as day_no union all select date_add(booking_date, interval 1 day) , day_no + 1 from next_7_days where day_no < 7) select booking_date from next_7_days;

# Q5. Given a messy SQL query that finds all users with more than 1000 followers from a 'Users' table, refactor it to use a CTE for better clarity and maintainability.

create table users2 (
    user_id int primary key auto_increment,
    user_name varchar(50),
    followers int,
    city varchar(50)
);

insert into users2 values
(1, 'rahul', 800, 'ahmedabad'),
(2, 'priya', 2500, 'mumbai'),
(3, 'amit', 1200, 'delhi'),
(4, 'neha', 5000, 'pune'),
(5, 'karan', 950, 'surat'),
(6, 'anita', 1800, 'jaipur'),
(7, 'rohit', 3000, 'kolkata');

with Messy as (select * from users2) select * from Messy where followers > 1000;