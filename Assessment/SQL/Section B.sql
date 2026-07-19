use superstore;

/* 1. Execute a query to retrieve the first 20 records from the orders table to verify data ingestion.*/

select * from orders limit 20;

/* 2. Select Order ID, Order Date, Sales, and Profit, applying a column alias to display Sales as Total_Sales.*/

select o.orderid, o.orderDate, p.sales as Total_Sales , p.profit from orders o join customer c on o.orderid = c.orderid join product p on c.customerid = p.customerid;

/* 3. Filter the dataset to isolate all high-value transactions where the Sales figure exceeds 5000.*/

select * from product where sales > 5000;

/* 4. Generate a report of the top 10 most profitable orders by sorting the records by Profit in descending order.*/

select o.*, c.*, p.* from orders o join customer c on o.orderid = c.orderid join product p on c.customerid = p.customerid order by p.profit desc;