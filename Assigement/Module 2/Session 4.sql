use music_streaming_app;

# 1.Create a table named MusicPlaylist with columns: id, song_name, artist, genre, and duration. Insert at least 5 records representing songs from your favorite Spotify playlist, then write a SELECT statement to retrieve all columns for all songs.

CREATE TABLE MusicPlaylist (id INT PRIMARY KEY auto_increment,song_name VARCHAR(100),artist VARCHAR(100),genre VARCHAR(50),duration TIME);

INSERT INTO MusicPlaylist (id, song_name, artist, genre, duration)VALUES(1, 'Kesariya', 'Arijit Singh', 'Bollywood', '00:04:28'),(2, 'Believer', 'Imagine Dragons', 'Rock', '00:03:24'),(3, 'Perfect', 'Ed Sheeran', 'Pop', '00:04:23'),
(4, 'Blinding Lights', 'The Weeknd', 'Pop', '00:03:20'),
(5, 'Levitating', 'Dua Lipa', 'Pop', '00:03:23');

select * from MusicPlaylist;

# 2. Write a SQL query to display only the song_name and artist columns from the MusicPlaylist table, showing just the first 3 records using the LIMIT keyword.

select song_name,artist from MusicPlaylist limit 3;

# 3. Suppose you have a table named FoodOrders with columns: id, restaurant, food_item, and order_date. Write a SQL query to list all unique restaurant names where you have placed orders, using the DISTINCT keyword.

create table FoodOrders (id smallint primary key auto_increment, restaurant varchar(50), food_item varchar(50), order_date date);

INSERT INTO FoodOrders (restaurant, food_item, order_date)
VALUES('Domino''s Pizza', 'Veg Pizza', '2026-07-10'),('McDonald''s', 'McAloo Tikki Burger', '2026-07-12'),('KFC', 'Chicken Bucket', '2026-07-15'),('Burger King', 'Whopper', '2026-07-18'),('Subway', 'Veggie Delight Sandwich', '2026-07-20');

select* from FoodOrders;

select distinct restaurant from FoodOrders;

# 4. Write a SQL query on the FoodOrders table to select food_item as 'Dish' and order_date as 'Date Ordered', displaying only these two columns with the column aliases in the output.

select food_item as 'Dish',order_date as 'Date Order' from FoodOrders;

# 5. You tried running this query: SELECT DISTINCT food_item, restaurant FROM FoodOrders LIMIT 2, but it returns an error or doesn't work as expected. Identify and fix the mistake in the query.<br><br><em><strong>Hint:</strong> Check the correct placement and usage of the LIMIT keyword in SQL syntax.</em>

select distinct food_item,restaurant from FoodOrders limit 2;