use superstore;

/* 1. What is the functional difference between SELECT * and specifying column names, and when is each preferred?*/

select * from customer;

/* 2. Which keyword renames a column in the output, and does this alias change the actual table structure in the database?*/

select sales as Total_Sales from product;

/* 3. Why does wrapping a numeric value in quotes (e.g., '5000') in a WHERE clause create a data type conflict in SQL?*/

select sales from product where sales > '5000';

/* 4. Contrast the results of ORDER BY Profit DESC versus ASC when the goal is to identify the top 10 most profitable orders.*/

select customerName, state, postalCode from customer order by postalCode desc;

/* 6. Explain the logical execution order of a query containing SELECT, WHERE, ORDER BY, and LIMIT clauses.*/

SELECT Sales FROM product WHERE Sales > 5000 ORDER BY Sales DESC LIMIT 10;