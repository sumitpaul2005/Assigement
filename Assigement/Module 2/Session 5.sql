use music_streaming_app;

# Q1. Create a table called Restaurants with columns: id, name, cuisine, rating, and city. Insert at least 5 sample records representing real or fictional restaurants you might find on Zomato.

create table restaurants(id smallint primary key auto_increment, name varchar(50), cuisine varchar(50), rating smallint, city varchar(50));

insert into Restaurants (id, name, cuisine, rating, city) values
(1, 'Swagat', 'North Indian', 4.6, 'Ahmedabad'),
(2, 'Pizza Hub', 'Italian', 4.2, 'Surat'),
(3, 'Dragon Wok', 'Chinese', 4.4, 'Ahmedabad'),
(4, 'Swadisht', 'South Indian', 3.9, 'Vadodara'),
(5, 'Cafe Aroma', 'Cafe', 3.7, 'Surat'),
(6, 'Royal Spice', 'Chinese', 4.8, 'Rajkot'),
(7, 'Italian Delight', 'Italian', 3.5, 'Ahmedabad'),
(8, 'Tandoori Nights', 'North Indian', 4.1, 'Surat'),
(9, 'Bombay Bites', 'Fast Food', 3.8, 'Mumbai'),
(10, 'Swaad Ghar', 'Gujarati', 4.5, 'Ahmedabad'),
(11, 'Urban Kitchen', 'Continental', 4.0, 'Pune'),
(12, 'Madras Cafe', 'South Indian', 4.3, 'Chennai'),
(13, 'China Express', 'Chinese', 3.6, 'Delhi'),
(14, 'La Pizzeria', 'Italian', 4.7, 'Bengaluru'),
(15, 'Green Leaf', 'Vegetarian', 4.2, 'Jaipur');

# Q2. Write a SQL query to find all restaurants in the Restaurants table that have a rating greater than 4.0 and are located in either 'Ahmedabad' or 'Surat'.

select * from restaurants where rating > 4.0 and city = "Ahmedabad" or city = "Surat";

# Q3. Using the LIKE operator, write a query to select all restaurants whose names start with 'Swa' (for example, 'Swagat', 'Swadisht') from the Restaurants table.<br><br><em><strong>Hint:</strong> Use LIKE 'Swa%'.</em>

select * from restaurants where name like "Swa%";

# Q4. Write a SQL query using the BETWEEN keyword to find all restaurants in the Restaurants table with a rating between 3.5 and 4.5 (inclusive).

select * from restaurants where rating between 3.5 and 4.5;

# Q5. Write a query to find all restaurants whose cuisine is either 'Chinese', 'Italian', or 'South Indian' using the IN operator.

select * from restaurants where cuisine in('Chinese','Italian','South Indian');