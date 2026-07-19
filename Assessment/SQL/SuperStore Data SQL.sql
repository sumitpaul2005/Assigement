create database SuperStore;
use SuperStore;
/*Row ID => Unique ID for each row.
Order ID => Unique Order ID for each Customer.
Order Date => Order Date of the product.
Ship Date => Shipping Date of the Product.
Ship Mode=> Shipping Mode specified by the Customer.
Customer ID => Unique ID to identify each Customer.
Customer Name => Name of the Customer.
Segment => The segment where the Customer belongs.
Country => Country of residence of the Customer.
City => City of residence of of the Customer.
State => State of residence of the Customer.
Postal Code => Postal Code of every Customer.
Region => Region where the Customer belong.
Product ID => Unique ID of the Product.
Category => Category of the product ordered.
Sub-Category => Sub-Category of the product ordered.
Product Name => Name of the Product
Sales => Sales of the Product.
Quantity => Quantity of the Product.
Discount => Discount provided.
Profit => Profit/Loss incurred.*/
create table orders(orderid int primary key auto_increment,orderDate date, shipDate date,
shipMode varchar(50));

create table customer(customerid bigint primary key auto_increment,orderid int,
foreign key (orderid) references orders(orderid), customerName varchar(50), segment varchar(50), country varchar(50), 
city varchar(50), state varchar(50), postalCode int, region varchar(50));

create table product(productid bigint primary key auto_increment,customerid bigint,foreign key (customerid) references customer(customerid),
category varchar(100),sub_category varchar(100), productName varchar(100),sales decimal(65,2), quantity bigint, discount int, profit int);