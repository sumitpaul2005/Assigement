# Q1. Create two tables in your database: 'restaurants' (id, name, city) and 'dishes' (id, restaurant_id, dish_name, price). Insert at least 3 restaurants and 2-3 dishes for each restaurant.

create table restaurents1(id smallint primary key auto_increment,name varchar(50), city varchar(50));
create table dishes(did smallint primary key auto_increment, r_id smallint, foreign key (r_id) references restaurents1(id),dish_name varchar(50), price bigint); 

insert into restaurents1 (id, name, city) values(1, 'Spice Hub', 'Ahmedabad'),(2, 'Pizza World', 'Surat'),(3, 'Royal Biryani', 'Vadodara'),(4, 'Green Cafe', 'Rajkot');
insert into dishes (did, r_id, dish_name, price) values(101, 1, 'Paneer Butter Masala', 280),(102, 1, 'Butter Naan', 40),(103, 2, 'Margherita Pizza', 350),(104, 2, 'Garlic Bread', 180),(105, 3, 'Chicken Biryani', 320),(106, 3, 'Mutton Biryani', 450),(107, 1, 'Mystery Dish', 200);

# Q2. Write an SQL INNER JOIN query to display each dish along with its restaurant name and city, similar to how Zomato shows dish details with the restaurant info.

select d.dish_name,d.price,r.name,r.city from restaurents1 r inner join dishes d on r.id = d.r_id;

# Q3. Write an SQL LEFT JOIN query to list all restaurants and their dishes, showing restaurants even if they currently have no dishes on the menu.<br><br><em><strong>Hint:</strong> Use LEFT JOIN so restaurants without dishes still appear in the results with NULL for dish columns.</em>

select r.name,r.city,d.dish_name,d.price from restaurents1 r left join dishes d on r.id = d.r_id;

# Q4. Write an SQL RIGHT JOIN query to display all dishes and their restaurant names, including any dishes that might not be linked to a restaurant (simulate a data error where a dish has a restaurant_id that doesn't match any restaurant).

select d.dish_name,d.price,r.name from restaurents1 r right join dishes d on r.id = d.r_id;

# Q5. Given this scenario: You want to show a list of all playlists and the songs inside them, like Spotify. Explain which JOIN type (INNER, LEFT, or RIGHT) you would use to show all playlists, even if some are empty, and write the SQL query for it.

select p.playlist_name,s.song_name from playlists p left join songs s on p.playlist_id = s.playlist_id;