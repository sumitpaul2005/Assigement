use music_streaming_app;

# Q1. Create two tables: Influencers (id, name) and Collaborations (id, influencer1_id, influencer2_id, collab_date). Write a SQL FULL JOIN query to list all influencers and show their collaboration partner names if any, including influencers with no collaborations.

create table influencers (
    id int primary key,
    name varchar(50)
);

create table collaborations (
    id int primary key,
    influencer1_id int,
    influencer2_id int,
    collab_date date
);

insert into influencers values
(1, 'aman'),
(2, 'riya'),
(3, 'karan'),
(4, 'neha'),
(5, 'rahul');

insert into collaborations values
(101, 1, 2, '2026-01-10'),
(102, 2, 3, '2026-02-15'),
(103, 1, 4, '2026-03-20');

select i.name as influencer, p.name as collaboration_partner,c.collab_date from influencers i join collaborations c on i.id = c.influencer1_id join influencers p on c.influencer2_id = p.id;

# Q2. Using a SELF JOIN, write a query on a table called Playlists (id, user_id, playlist_name, parent_playlist_id) to display each playlist alongside its parent playlist name, similar to how Spotify shows nested playlists.<br><br><em><strong>Hint:</strong> Join Playlists with itself on parent_playlist_id = id.</em>

create table playlists (
    id int primary key,
    user_id int,
    playlist_name varchar(50),
    parent_playlist_id int
);

insert into playlists values
(1, 101, 'my music', null),
(2, 101, 'workout', 1),
(3, 101, 'gym songs', 2),
(4, 102, 'travel', null),
(5, 102, 'road trip', 4);

select p.playlist_name as playlist, parent.playlist_name as parent_playlist from playlists p left join playlists parent on p.parent_playlist_id = parent.id;

# Q3. Given three tables: Users (id, username), Orders (id, user_id, order_date), and Payments (id, order_id, amount), write a SQL query using multiple JOINs to display each username, their order date, and payment amount, showing all users even if they have no orders or payments.

create table users (
    id int primary key,
    username varchar(50)
);

create table orders2 (
    id int primary key,
    user_id int,
    order_date date,
    foreign key (user_id) references users(id)
);

create table payments (
    id int primary key,
    order_id int,
    amount decimal(10,2),
    foreign key (order_id) references orders2(id)
);

insert into users values
(101, 'rahul'),
(102, 'priya'),
(103, 'aman'),
(104, 'neha'),
(105, 'karan'); 

insert into orders2 values
(1001, 101, '2026-07-01'),
(1002, 102, '2026-07-02'),
(1003, 101, '2026-07-05'),
(1004, 104, '2026-07-06');

insert into payments values
(201, 1001, 850.00),
(202, 1002, 1200.00),
(203, 1004, 650.00);

select u.username, o.order_date, p.amount from users u left join orders2 o on u.id = o.user_id left join payments p on o.id = p.order_id;

# Q4. You notice that your JOIN query between Zomato's Restaurants and Reviews tables is returning duplicate rows for some restaurants. Modify your query to eliminate duplicates and explain in one line why the duplicates were happening.<br><br><em><strong>Hint:</strong> Use DISTINCT or GROUP BY and consider the relationship between restaurants and reviews.</em>

create table restaurant (
    id int primary key,
    restaurant_name varchar(50),
    city varchar(50)
);

insert into restaurant values
(1, 'spice hub', 'ahmedabad'),
(2, 'pizza world', 'surat'),
(3, 'royal biryani', 'vadodara'),
(4, 'green cafe', 'rajkot');

create table reviews (
    id int primary key,
    restaurant_id int,
    customer_name varchar(50),
    rating int,
    review_text varchar(100),
    foreign key (restaurant_id) references restaurant(id)
);
insert into reviews values
(101, 1, 'rahul', 5, 'excellent food'),
(102, 1, 'priya', 4, 'good service'),
(103, 2, 'aman', 5, 'best pizza'),
(104, 2, 'neha', 4, 'nice ambience'),
(105, 2, 'karan', 3, 'average taste'),
(106, 3, 'riya', 5, 'amazing biryani');

select distinct
    r.restaurant_name,
    r.city
from restaurant r
inner join reviews rev
on r.id = rev.restaurant_id;

# Q5. Write two different JOIN queries on a Products and Categories table (like Flipkart) to list all products with their category names, but use different join conditions in each. Briefly explain which join condition is more efficient and why.

create table products (
    product_id int primary key,
    product_name varchar(50),
    category_id int
);

create table categories (
    category_id int primary key,
    category_name varchar(50)
);

insert into categories values
(1, 'mobiles'),
(2, 'laptops'),
(3, 'electronics'),
(4, 'fashion'),
(5, 'books');

insert into products values
(101, 'iphone 15', 1),
(102, 'samsung galaxy s25', 1),
(103, 'dell inspiron', 2),
(104, 'sony headphones', 3),
(105, 'nike shoes', 4),
(106, 'atomic habits', 5);

select
    p.product_name,
    c.category_name
from products p
inner join categories c
on p.category_id = c.category_id;

select
    products.product_name,
    categories.category_name
from products
inner join categories
on products.category_id = categories.category_id;