# 1. Install MySQL or PostgreSQL on your system and create a new database named 'music_streaming_app' using the command line or GUI tool of your choice.

create database music_streaming_app;
use music_streaming_app;

# 2. Inside the 'music_streaming_app' database, create a table called 'playlists' with columns: playlist_id (integer, primary key), name (varchar), and created_by (varchar).

create table playlists(playlist_id smallint primary key auto_increment, name varchar(50), created_by varchar(50));

# 3. Insert three sample rows into the 'playlists' table representing playlists like 'Bollywood Hits', 'Chill Vibes', and 'Workout Mix', each created by a different user.

INSERT INTO playlists (playlist_id, name, created_by)
VALUES(1, 'Bollywood Hits', 'Amit'),(2, 'Chill Vibes', 'Priya'),(3, 'Workout Mix', 'Rahul');

select * from playlists;

# 4. Write an SQL SELECT query to display all playlists created by the user 'Amit' from the 'playlists' table.<br><br><em><strong>Hint:</strong> Use the WHERE clause to filter by the 'created_by' column.</em>

select * from playlists where created_by = "Amit";

# 5. Open ChatGPT or Copilot and ask it to explain the difference between a table, a row, and a column in SQL using an example from a food delivery app like Zomato. Paste the explanation you receive into your assignment.

/*Imagine Zomato has a table called Orders.

Order_ID	Customer_Name	Restaurant	Total_Amount
101				Amit		Domino's	450
102				Priya		McDonald's	320
103				Rahul		KFC			560

Table: A table is a collection of related data organized into rows and columns. In this example, Orders is the table that stores all order information.
Row: A row represents one complete record in the table. For example, the row (101, Amit, Domino's, 450) represents one order placed by Amit.
Column: A column represents a specific type of information for every record. For example, Customer_Name stores the names of customers, while Restaurant stores the restaurant names.

In simple terms:

Table = The entire Orders list.
Row = One customer's order.
Column = One category of information (such as Customer_Name or Total_Amount).*/