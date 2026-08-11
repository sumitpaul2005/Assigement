use music_streaming_app;

# Q1. Create a SQL table called Restaurant with columns: id, name, cuisine, location, and average_rating. Insert at least 5 sample rows representing popular restaurants from Zomato.

create table restaurant17 (
    id int primary key,
    name varchar(100),
    cuisine varchar(100),
    location varchar(100),
    average_rating decimal(2,1)
);

insert into restaurant17(id, name, cuisine, location, average_rating)values
(1, 'dominos pizza', 'italian, pizza', 'ahmedabad', 4.2),
(2, 'burger king', 'fast food, burger', 'ahmedabad', 4.1),
(3, 'haldiram''s', 'north indian, sweets', 'delhi', 4.3),
(4, 'barbeque nation', 'north indian, bbq', 'mumbai', 4.5),
(5, 'the belgian waffle co.', 'desserts, waffles', 'bangalore', 4.4);

select * from restaurant17;

select * from Restaurant17 where average_rating >= 4.3 order by average_rating desc;

# Q2. Write a SQL query to generate a report showing the number of restaurants for each cuisine type from your Restaurant table, ordered by the count in descending order.<br><br><em><strong>Hint:</strong> Use GROUP BY and ORDER BY.</em>

select cuisine, count(*) as restaurant_count from restaurant17 group by cuisine order by restaurant_count desc;

# Q3. Add a new table called Review with columns: id, restaurant_id, user_name, rating, and review_date. Insert at least 10 sample reviews, linking them to restaurants using restaurant_id.

create table review17 (
    id int primary key,
    restaurant_id int,
    user_name varchar(100),
    rating decimal(2,1),
    review_date date,
    foreign key (restaurant_id) references restaurant17(id)
);

insert into review17(id, restaurant_id, user_name, rating, review_date) values
(1, 1, 'rahul', 4.5, '2026-08-01'),
(2, 2, 'priya', 4.0, '2026-08-02'),
(3, 3, 'amit', 4.5, '2026-08-03'),
(4, 4, 'neha', 5.0, '2026-08-04'),
(5, 5, 'rohan', 4.0, '2026-08-05'),
(6, 1, 'kiran', 4.0, '2026-08-06'),
(7, 2, 'pooja', 4.5, '2026-08-07'),
(8, 3, 'arjun', 3.5, '2026-08-08'),
(9, 4, 'sneha', 4.5, '2026-08-09'),
(10, 5, 'vikas', 5.0, '2026-08-10');

select * from review17;

# Q4. Write a SQL query using a JOIN to display each restaurant's name, cuisine, and its average review rating (from the Review table), ordered by highest average rating first.<br><br><em><strong>Hint:</strong> Use JOIN and GROUP BY with aggregate functions.</em>

select r.name, r.cuisine, avg(re.rating) as average_rating from restaurant17 r join review17 re on r.id = re.restaurant_id group by r.name, r.cuisine order by average_rating desc;

# Q5. Use a window function to rank restaurants by their average review rating within each cuisine type, showing the restaurant name, cuisine, average rating, and rank.<br><br><em><strong>Hint:</strong> Use the RANK() or DENSE_RANK() window function partitioned by cuisine.</em>

select re.name,re.cuisine,re.avg_rating,rank() over(partition by re.cuisine order by re.avg_rating desc) as ranks from (select r.name,r.cuisine,avg(rv.rating) as avg_rating from restaurant17 r join review17 rv on r.id=rv.restaurant_id group by r.name,r.cuisine) re;