use music_streaming_app;

# Q1. Create a SQL query using a subquery in the WHERE clause to find all restaurants from a 'Restaurants' table whose average rating is higher than the average rating of all restaurants in the city.

select * from restaurants where rating > (select avg(rating) from restaurants);

# Q2. Write a SQL query that uses a subquery in the SELECT statement to display each user's name from a 'Users' table along with the total number of orders they have placed from an 'Orders' table, like a summary you might see in a Zomato user profile.

CREATE TABLE Users1 (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50)
);
CREATE TABLE Order3 (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES Users1(user_id)
);
INSERT INTO Users1 (user_id, user_name) VALUES
(1, 'Amit'),
(2, 'Priya'),
(3, 'Rahul'),
(4, 'Sneha'),
(5, 'Arjun'),
(6, 'Neha'),
(7, 'Rohit'),
(8, 'Pooja'),
(9, 'Karan'),
(10, 'Anjali');
INSERT INTO Order3 (order_id, user_id, order_date, amount) VALUES
(101, 1, '2026-07-01', 450.00),
(102, 1, '2026-07-05', 320.00),
(103, 2, '2026-07-03', 250.00),
(104, 3, '2026-07-04', 600.00),
(105, 1, '2026-07-08', 180.00),
(106, 4, '2026-07-09', 900.00),
(107, 5, '2026-07-10', 150.00),
(108, 5, '2026-07-12', 220.00),
(109, 6, '2026-07-13', 340.00),
(110, 3, '2026-07-15', 410.00),
(111, 7, '2026-07-16', 275.00),
(112, 8, '2026-07-17', 520.00),
(113, 9, '2026-07-18', 390.00),
(114, 10, '2026-07-19', 610.00),
(115, 2, '2026-07-20', 480.00),
(116, 4, '2026-07-21', 730.00),
(117, 4, '2026-07-22', 150.00),
(118, 6, '2026-07-23', 260.00),
(119, 8, '2026-07-24', 330.00),
(120, 10, '2026-07-25', 890.00);

SELECT u.user_name,(SELECT COUNT(*)FROM Order3 o WHERE o.user_id = u.user_id) AS total_orders FROM Users1 u;

# Q3. Given a 'Movies' table and a 'Reviews' table, write a SQL query using IN with a subquery to list all movies that have at least one review with a rating of 5 stars, as seen in BookMyShow's top-rated section.

CREATE TABLE Movies1 (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(100),
    genre VARCHAR(50)
);
CREATE TABLE Reviews1 (
    review_id INT PRIMARY KEY,
    movie_id INT,
    rating INT,
    reviewer_name VARCHAR(50),
    FOREIGN KEY (movie_id) REFERENCES Movies1(movie_id)
);

INSERT INTO Movies1 (movie_id, movie_name, genre) VALUES (1, '3 Idiots', 'Comedy'),(2, 'KGF Chapter 2', 'Action'),(3, 'Bahubali', 'Action'),(4, 'Dangal', 'Sports'),(5, 'Drishyam', 'Thriller'),(6, 'RRR', 'Action'),(7, 'Jawan', 'Action'),(8, 'Pushpa', 'Action'),(9, 'Animal', 'Drama'),(10, 'Chhichhore', 'Comedy');

INSERT INTO Reviews1 (review_id, movie_id, rating, reviewer_name) VALUES(101, 1, 5, 'Amit'),(102, 1, 4, 'Priya'),(103, 2, 5, 'Rahul'),(104, 2, 3, 'Sneha'),(105, 3, 4, 'Arjun'),(106, 4, 5, 'Neha'),(107, 5, 2, 'Rohit'),(108, 6, 5, 'Pooja'),(109, 7, 4, 'Karan'),(110, 8, 5, 'Anjali'),(111, 9, 3, 'Vikram'),(112, 10, 5, 'Meera'),(113, 3, 5, 'Sanjay'),(114, 5, 4, 'Riya'),(115, 7, 5, 'Deepak');

select * from movies1 where movie_id in (select movie_id from reviews1 where rating = 5);

# Q4. Write a nested SQL query to find the names of all sellers from a 'Sellers' table on a Flipkart-style platform who have sold products in every category listed in a 'Categories' table.<br><br><em><strong>Hint:</strong> Use nested subqueries to compare seller's categories with the complete list of categories.</em>

CREATE TABLE Sellers (
    seller_id INT PRIMARY KEY,
    seller_name VARCHAR(100)
);
CREATE TABLE Categories1 (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);
CREATE TABLE Products1 (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    seller_id INT,
    category_id INT,
    price DECIMAL(10,2),
    FOREIGN KEY (seller_id) REFERENCES Sellers(seller_id),
    FOREIGN KEY (category_id) REFERENCES Categories1(category_id)
);
INSERT INTO Sellers (seller_id, seller_name) VALUES
(1, 'TechStore'),
(2, 'MegaMart'),
(3, 'SuperDeals'),
(4, 'ElectroWorld'),
(5, 'FashionHub'),
(6, 'HomeNeeds'),
(7, 'SmartBuy'),
(8, 'DailyDeals'),
(9, 'PrimeSeller'),
(10, 'EasyShop');

INSERT INTO Categories1 (category_id, category_name) VALUES(101, 'Electronics'),(102, 'Fashion'),(103, 'Home Appliances'),(104, 'Books');

INSERT INTO Products1 (product_id, product_name, seller_id, category_id, price) VALUES(1001, 'Laptop',1, 101, 65000),(1002, 'T-Shirt',1, 102,1200),(1003, 'Microwave',1, 103, 15000),(1004, 'Programming Book',1, 104,800),(1005, 'Smartphone',2,101,30000),(1006, 'Jeans',2, 102,1800),(1007, 'Refrigerator',2, 103, 40000),(1008, 'Camera',3, 101, 45000),
(1009, 'Shoes',3, 102,  2500),
(1010, 'Washing Machine',3, 103, 28000),
(1011, 'Novel',3, 104,600),
(1012, 'Tablet',4, 101, 22000),
(1013, 'Jacket',5, 102,3500),
(1014, 'Air Conditioner',6, 103,38000),
(1015, 'Smart Watch',7, 101, 12000),
(1016, 'Data Science Book', 7, 104,950),
(1017, 'Dress',8, 102,  2000),
(1018, 'Mixer Grinder',8, 103,4500),
(1019, 'Gaming Laptop',9, 101,85000),
(1020, 'Formal Shirt',9, 102,1700),
(1021, 'Vacuum Cleaner',9, 103,11000),
(1022, 'SQL Guide',9, 104,700),
(1023, 'Python Basics',10, 104,650);

SELECT s.seller_name
FROM Sellers s
WHERE NOT EXISTS (
    SELECT *
    FROM Categories1 c
    WHERE NOT EXISTS (
        SELECT *
        FROM Products1 p
        WHERE p.seller_id = s.seller_id
          AND p.category_id = c.category_id
    )
);