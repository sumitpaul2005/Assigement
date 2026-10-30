use music_streaming_app;

# Q1. Create a table named Playlists with columns: id, user_id, playlist_name, and total_likes. Insert at least 8 sample rows with different users and playlists, making sure some playlists have the same user_id.

create table playlists1 (
    id int primary key auto_increment,
    user_id int,
    playlist_name varchar(100),
    total_likes int
);

insert into playlists1 (id, user_id, playlist_name, total_likes) values
(1, 101, 'workout hits', 520),
(2, 102, 'chill vibes', 310),
(3, 101, 'morning motivation', 450),
(4, 103, 'bollywood beats', 780),
(5, 104, 'lo-fi study', 260),
(6, 102, 'road trip songs', 690),
(7, 105, 'party mix', 910),
(8, 103, 'romantic melodies', 540);

select * from playlists1;

# Q2. Write a SQL query using ROW_NUMBER() and the OVER() clause to assign a unique row number to each playlist, ordered by total_likes in descending order.

select *,row_number() over(order by total_likes desc) as row_num from playlists1; 

# Q3. Use the RANK() function with the OVER() clause to rank all playlists by total_likes, and display the playlist_name, user_id, total_likes, and their rank.

select *, rank() over(order by total_likes desc) as Ranks from playlists1;

# Q4. Write a SQL query using DENSE_RANK() and PARTITION BY user_id to rank each user's playlists by total_likes, showing playlist_name, user_id, total_likes, and dense rank.<br><br><em><strong>Hint:</strong> This will show how popular each playlist is within each user's account, similar to how Spotify might rank your top playlists.</em>

select *, dense_rank() over(partition by user_id order by total_likes desc) as Dense_ranks from playlists1;

# Q5. Imagine you want to show the top 2 playlists per user based on total_likes, like Spotify's 'Your Top Playlists' feature. Write a query using a window function to select only the top 2 playlists for each user.

select
    playlist_name,
    user_id,
    total_likes
from (
    select
        playlist_name,
        user_id,
        total_likes,
        row_number() over (
            partition by user_id
            order by total_likes desc
        ) as rn
    from playlists1
) p
where rn <= 2
order by user_id, total_likes desc;