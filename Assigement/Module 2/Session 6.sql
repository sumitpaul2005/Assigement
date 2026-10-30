use music_streaming_app;

# Q1. Write an SQL query to display all products from a 'products' table and sort them by price in ascending order, similar to how Flipkart lists items from lowest to highest price.

SELECT * FROM Orders as Products ORDER BY total_amt ASC;

# Q2. Modify your previous query to show the top 5 most expensive products using ORDER BY with DESC and LIMIT.

select * from Orders order by total_amt desc limit 5;

# Q3. Given a 'movies' table with columns 'title', 'release_year', and 'rating', write an SQL query to list all movies sorted first by release_year in descending order (latest first), then by rating in descending order (highest rated first).

create table movies(title varchar(50), release_date date, rating smallint);

insert into movies (title, release_date, rating) values('3 Idiots', '2009-12-25', 9),('KGF Chapter 2', '2022-04-14', 8),('RRR', '2022-03-25', 9);

select * from movies order by release_date desc , rating desc;

# Q4. Write an SQL query to display the first 10 restaurants from a 'restaurants' table, sorted alphabetically by name, just like Zomato's A-Z listing.<br><br><em><strong>Hint:</strong> Use ORDER BY with LIMIT.</em>

select * from restaurants order by name asc limit 10;

# Q5. Suppose you want to display the top 3 trending songs from a 'songs' table based on play_count, but if two songs have the same play_count, the more recently added song should come first. Write the SQL query to achieve this.<br><br><em><strong>Hint:</strong> Use ORDER BY with multiple columns.</em>

create table songs (id smallint primary key auto_increment,title varchar(100),artist varchar(100),play_count smallint,added_date date);

insert into songs (id, title, artist, play_count, added_date) values(1, 'Kesariya', 'Arijit Singh', 9500, '2024-01-15'),(2, 'Apna Bana Le', 'Arijit Singh', 12000, '2024-03-10'),(3, 'Heeriye', 'Arijit Singh', 12000, '2024-05-20'),(4, 'Raataan Lambiyan', 'Jubin Nautiyal', 8700, '2024-02-18'),(5, 'Tum Hi Ho', 'Arijit Singh', 15000, '2024-04-25');

select * from songs order by play_count desc, added_date desc limit 3;