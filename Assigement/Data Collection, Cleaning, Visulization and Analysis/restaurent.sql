create database ass;
use ass;

CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    cuisine VARCHAR(50),
    rating DECIMAL(2,1)
);

INSERT INTO restaurants (restaurant_id, name, city, cuisine, rating) VALUES
(1, 'Spice Hub', 'Mumbai', 'Indian', 4.5),
(2, 'Pizza Town', 'Delhi', 'Italian', 4.2),
(3, 'Sushi House', 'Bengaluru', 'Japanese', 4.8),
(4, 'Burger King', 'Pune', 'Fast Food', 4.1),
(5, 'Cafe Mocha', 'Chennai', 'Cafe', 4.3),
(6, 'Royal Biryani', 'Hyderabad', 'Biryani', 4.7),
(7, 'Dragon Wok', 'Kolkata', 'Chinese', 4.0),
(8, 'Taco Fiesta', 'Ahmedabad', 'Mexican', 4.4),
(9, 'Green Bowl', 'Jaipur', 'Healthy', 4.6),
(10, 'Ocean Delight', 'Goa', 'Seafood', 4.5);