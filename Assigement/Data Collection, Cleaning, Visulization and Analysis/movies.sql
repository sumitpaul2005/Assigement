use ass;

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    name VARCHAR(100),
    genre VARCHAR(50),
    language VARCHAR(30),
    release_year INT,
    rating DECIMAL(2,1)
);
INSERT INTO movies (movie_id, name, genre, language, release_year, rating) VALUES
(1, 'Inception', 'Sci-Fi', 'English', 2010, 8.8),
(2, 'Avatar', 'Action', 'English', 2009, 7.9),
(3, 'Interstellar', 'Sci-Fi', 'English', 2014, 8.7),
(4, 'The Dark Knight', 'Action', 'English', 2008, 9.0),
(5, 'Titanic', 'Romance', 'English', 1997, 7.8),
(6, '3 Idiots', 'Comedy', 'Hindi', 2009, 8.4),
(7, 'Dangal', 'Drama', 'Hindi', 2016, 8.3),
(8, 'Baahubali 2', 'Action', 'Telugu', 2017, 8.2),
(9, 'Frozen', 'Animation', 'English', 2013, 7.5),
(10, 'Joker', 'Thriller', 'English', 2019, 8.5);