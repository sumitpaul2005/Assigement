

# Q1. Install MySQL Community Server or SQLite on your system and verify the installation by connecting to the database using the command line or a GUI tool like MySQL Workbench or DB Browser for SQLite.

# Q2. Create a new database named 'foodie_app' to simulate a Zomato-style backend.

create database foodie_app;

# Q3. Write a CREATE TABLE statement to define a 'restaurants' table in the 'foodie_app' database with the following columns: id (integer, primary key), name (varchar/character, max 100), cuisine (varchar/character, max 50), rating (decimal, e.g., 4.5), and location (varchar/character, max 100).

use foodie_app;

create table restaurants (
    id int primary key auto_increment,
    name varchar(100),
    cuisine varchar(50),
    rating decimal(2,1),
    location varchar(100)
);

insert into restaurants (id, name, cuisine, rating, location) values
(1, 'dominos', 'italian', 4.5, 'mumbai'),
(2, 'biryani blues', 'indian', 4.2, 'delhi'),
(3, 'pizza hut', 'italian', 4.0, 'pune'),
(4, 'barbeque nation', 'indian', 4.6, 'bangalore'),
(5, 'wow momo', 'chinese', 4.3, 'kolkata');

# Q4. Design and create a 'users' table for a Flipkart-style app with columns: user_id (primary key), username, email, phone_number, and created_at (date/time). Pick appropriate data types for each column.<br><br><em><strong>Hint:</strong> Think about which columns should be unique and which data types best fit email and phone numbers.</em>

create table users (
    user_id int primary key auto_increment,
    username varchar(50) not null,
    email varchar(100) not null unique,
    phone_number varchar(15) not null unique,
    created_at datetime default current_timestamp
);

insert into users (username, email, phone_number) values
('rahul', 'rahul@gmail.com', '9876543210'),
('priya', 'priya@gmail.com', '9876543211'),
('amit', 'amit@gmail.com', '9876543212'),
('neha', 'neha@gmail.com', '9876543213'),
('rohit', 'rohit@gmail.com', '9876543214');

# Q5. Intentionally make a mistake in your CREATE TABLE statement (such as missing a comma or using an unsupported data type), run it, and then fix the error based on the message you receive.<br><br><em><strong>Hint:</strong> Take a screenshot of the error and the corrected SQL statement for your records.</em>

create table users2 (
    user_id int primary key auto_increment,
    username varchar(50)
    email varchar(100) unique,
    phone_number varchar(15) unique,
    created_at datetime default current_timestamp
);

# ERROR 1064 (42000): You have an error in your SQL syntax...-- 

create table users2 (
    user_id int primary key auto_increment,
    username varchar(50),
    email varchar(100) unique,
    phone_number varchar(15) unique,
    created_at datetime default current_timestamp
);
