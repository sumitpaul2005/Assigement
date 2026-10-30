use music_streaming_app;

# Q1. Write an SQL query to display the total number of songs uploaded by each artist from a table 'songs' (columns: song_id, artist_name, title) and show only those artists who have uploaded more than 3 songs.

create table songs18 (song_id int, artist_name varchar(50), title varchar(100));

insert into songs18 values
(1, 'arijit singh', 'tum hi ho'),
(2, 'arijit singh', 'agar tum saath ho'),
(3, 'arijit singh', 'channa mereya'),
(4, 'arijit singh', 'khairiyat'),
(5, 'arijit singh', 'kesariya'),
(6, 'atif aslam', 'tera hone laga hoon'),
(7, 'atif aslam', 'jeena jeena'),
(8, 'atif aslam', 'dil diyan gallan'),
(9, 'atif aslam', 'tajdar-e-haram'),
(10, 'shreya ghoshal', 'sun raha hai'),
(11, 'shreya ghoshal', 'manwa lage'),
(12, 'shreya ghoshal', 'deewani mastani'),
(13, 'shreya ghoshal', 'teri ore'),
(14, 'armaan malik', 'bol do na zara'),
(15, 'armaan malik', 'main hoon hero tera');

select artist_name, count(artist_name) as total
from songs18
group by artist_name
having count(artist_name) > 3;

# Q2. Given two tables, 'orders' (order_id, user_id, amount) and 'users' (user_id, username), write a SQL JOIN query to display each username along with their total order amount.

create table users18 (user_id int primary key auto_increment, username varchar(50));

insert into users18 values
(1, 'rahul'),
(2, 'priya'),
(3, 'amit'),
(4, 'neha'),
(5, 'rohit');

create table orders18 (order_id int primary key auto_increment, user_id int, amount decimal(10,2),foreign key (user_id) references users18(user_id));
drop table users18;
insert into orders18 values
(101, 1, 500.00),
(102, 1, 750.00),
(103, 2, 1200.00),
(104, 2, 300.00),
(105, 3, 900.00),
(106, 3, 450.00),
(107, 3, 650.00),
(108, 4, 800.00),
(109, 5, 250.00),
(110, 5, 550.00);

select u.username,sum(o.amount) as total_amount from users18 u join orders18 o on u.user_id = o.user_id group by u.username;

# Q3. Write a SQL subquery to find the names of all restaurants from a 'restaurants' table (id, name, rating) whose rating is higher than the average rating of all restaurants.

create table restaurants18 (
    id int primary key auto_increment,
    name varchar(100),
    rating decimal(3,1)
);

insert into restaurants18 (name, rating) values
('dominos', 4.5),
('pizza hut', 4.0),
('mcdonalds', 3.8),
('subway', 4.2),
('burger king', 3.5),
('zomato kitchen', 4.7),
('barbeque nation', 4.6),
('biryani blues', 4.1),
('cafe coffee day', 3.9),
('wow momo', 4.3);

select * from restaurants18 where rating > (select avg(rating) from restaurants18);

# Q4. Using a 'transactions' table (id, user_id, amount, transaction_date), write a SQL query with a window function to display each user's transaction amount and their running total (cumulative sum) ordered by transaction_date.

create table transactions (
    id int primary key auto_increment,
    user_id int,
    amount decimal(10,2),
    transaction_date date
);

insert into transactions (user_id, amount, transaction_date) values
(1, 500.00, '2026-08-01'),
(1, 300.00, '2026-08-03'),
(1, 700.00, '2026-08-05'),
(2, 1000.00, '2026-08-02'),
(2, 450.00, '2026-08-04'),
(2, 800.00, '2026-08-06'),
(3, 250.00, '2026-08-01'),
(3, 600.00, '2026-08-03'),
(3, 400.00, '2026-08-07');

select user_id, transaction_date, amount,
       sum(amount) over (
           partition by user_id
           order by transaction_date
       ) as running_total
from transactions;

# Q5. List two optimizations you would apply to speed up a query that filters Flipkart products by category and price, and briefly explain how each helps.<br><br><em><strong>Hint:</strong> Think about indexes and query structure.</em>

create table products18 (
    id int primary key auto_increment,
    product_name varchar(100),
    category varchar(50),
    price decimal(10,2)
);

insert into products18 (product_name, category, price) values
('iphone 15', 'electronics', 65000),
('samsung galaxy s24', 'electronics', 72000),
('boat headphones', 'electronics', 2500),
('hp laptop', 'computers', 55000),
('dell laptop', 'computers', 48000),
('nike shoes', 'fashion', 5000),
('adidas shoes', 'fashion', 4500),
('wildcraft backpack', 'bags', 2200),
('puma t-shirt', 'fashion', 1800),
('logitech mouse', 'electronics', 1200);

create index idx_category_price on products18(category, price);

select product_name, price
from products18
where category = 'electronics'
and price < 50000;