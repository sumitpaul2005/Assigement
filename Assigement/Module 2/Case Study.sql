use music_streaming_app;

# Q1. Write an SQL query to find the top 5 highest-rated restaurants in Koramangala that serve North Indian cuisine, using the Zomato Bangalore dataset.

create table zomato (
    id int primary key auto_increment,
    name varchar(100),
    location varchar(50),
    cuisines varchar(100),
    rate decimal(2,1)
);

insert into zomato (name, location, cuisines, rate) values
('empire restaurant', 'koramangala', 'north indian', 4.5),
('meghana foods', 'koramangala', 'north indian', 4.6),
('nagarjuna', 'koramangala', 'north indian', 4.4),
('absolute barbecue', 'koramangala', 'north indian', 4.3),
('paradise biryani', 'koramangala', 'north indian', 4.2),
('truffles', 'koramangala', 'burger, cafe', 4.7),
('beijing bites', 'koramangala', 'chinese', 4.1),
('udupi palace', 'koramangala', 'south indian', 4.0);

select name, location, cuisines, rate
from zomato
where location = 'koramangala'
and cuisines like '%north indian%'
order by rate desc
limit 5;

# Q2. Using SQL, calculate the average cost for two people for each cuisine type and list the 3 most expensive cuisines to eat in Bangalore.

create table zomato1 (
    id int primary key auto_increment,
    name varchar(100),
    cuisines varchar(100),
    approx_cost_for_two int
);

insert into zomato1 (name, cuisines, approx_cost_for_two) values
('toit', 'continental', 1800),
('karavalli', 'south indian', 2500),
('meghana foods', 'north indian', 800),
('bbq nation', 'barbecue', 1600),
('truffles', 'burger', 900),
('farzi cafe', 'north indian', 2000),
('olive beach', 'mediterranean', 3000),
('cafe coffee day', 'cafe', 600),
('mainland china', 'chinese', 1400),
('social', 'continental', 1700);

select cuisines,avg(approx_cost_for_two) as average_cost_for_two_people from zomato1 group by cuisines order by average_cost_for_two_people desc limit 3;

# Q3. Find all restaurants that offer online delivery but have a rating below 3.0, and suggest a marketing strategy to improve their ratings based on your findings.<br><br><em><strong>Hint:</strong> Look for patterns in location, cuisine, or price that might explain the low ratings.</em>

create table zomato2 (
    id int primary key auto_increment,
    name varchar(100),
    location varchar(100),
    cuisines varchar(100),
    rate decimal(2,1),
    online_order varchar(10)
);

insert into zomato2 (name, location, cuisines, rate, online_order) values
('hotel empire', 'koramangala', 'north indian', 2.8, 'yes'),
('spice garden', 'indiranagar', 'south indian', 2.6, 'yes'),
('food palace', 'btm layout', 'chinese', 2.9, 'yes'),
('tasty bites', 'jayanagar', 'north indian', 3.8, 'yes'),
('cafe delight', 'koramangala', 'continental', 2.7, 'yes'),
('biryani house', 'marathahalli', 'biryani', 2.5, 'yes'),
('pizza corner', 'whitefield', 'italian', 4.1, 'yes'),
('urban kitchen', 'indiranagar', 'chinese', 2.9, 'yes'),
('south spice', 'btm layout', 'south indian', 2.7, 'no'),
('royal restaurant', 'koramangala', 'mughlai', 2.8, 'yes');

select name, location, cuisines, rate, online_order
from zomato2
where online_order = 'yes'
and rate < 3.0;

# Q4. Write an SQL query to segment restaurants into three market segments based on average cost for two: budget (below 400), mid-range (400-800), and premium (above 800). Count how many restaurants fall into each segment.

select
    case
        when approx_cost_for_two < 400 then 'budget'
        when approx_cost_for_two between 400 and 800 then 'mid-range'
        when approx_cost_for_two > 800 then 'premium'
    end as market_segment,
    count(*) as restaurant_count
from zomato1
group by market_segment
order by restaurant_count desc;

# Q5. Use ChatGPT or Copilot to help you write an SQL query that lists the top 10 most popular restaurant chains (by number of outlets) in the dataset, then run and validate the query yourself.<br><br><em><strong>Hint:</strong> Search for 'SQL group by count example' if you get stuck.</em>

select name, count(*) as outlet_count
from zomato
group by name
order by outlet_count desc
limit 10;