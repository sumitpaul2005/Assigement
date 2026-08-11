use foodie_app;

# Q1. Create a table called Playlist with columns: id (INT, primary key), song_name (VARCHAR), artist (VARCHAR), and duration (INT, seconds). Insert a single row for your current favorite song.

create table Playlist (
    id int primary key,
    song_name varchar(100),
    artist varchar(100),
    duration int
);

insert into Playlist values
(1, 'tum hi ho', 'arijit singh', 262);

select * from Playlist;

# Q2. Insert 3 new rows into the Playlist table for songs you recently listened to on Spotify, including their song_name, artist, and duration.

insert into Playlist (id, song_name, artist, duration) values
(2, 'kesariya', 'arijit singh', 268),
(3, 'heeriye', 'jasleen royal', 191),
(4, 'apna bana le', 'arijit singh', 261),
(5,'teri yaad','Sonu nigam',100);
select * from Playlist;

# Q3. Update the artist name for one of your Playlist entries to fix a typo (for example, change 'Arjit Singh' to 'Arijit Singh') using the UPDATE statement with a WHERE clause.

update playlist set artist = 'Sonu Nigam' where id = 2;
select * from Playlist;

# Q4. Delete a song from the Playlist table where the duration is less than 120 seconds using the DELETE statement and a WHERE clause.<br><br><em><strong>Hint:</strong> Make sure your WHERE clause is specific so you don’t accidentally delete all rows.</em>


delete from playlist where duration < 120;
select * from Playlist;

# Q5. Write an SQL statement that would update the song_name for all songs by 'AP Dhillon' in your Playlist to add '(Remix)' at the end of the name, but only if the duration is more than 180 seconds.<br><br><em><strong>Constraint:</strong> Combine UPDATE with WHERE to target only the correct rows.</em>

update Playlist
set song_name = concat(song_name, ' (Remix)')
where artist = 'AP Dhillon'
and duration > 180;

select * from Playlist;
