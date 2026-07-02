create database assinmentSQL;
use assignmentsql;

create table Company ( CompanyId int primary key auto_increment, CompanyName varchar(50), Street varchar(50), City varchar(50), State varchar(50), Zip varchar(50));
create table Employee(EmployeeId int primary key auto_increment, FirstName varchar(50), LastName varchar(50), Salary decimal(10,2),HireDate date, JobTitle 	varchar(50), Email varchar(50), Phone varchar(12));
create table Contact(ContactId int primary key auto_increment, CompanyId int, foreign key (CompanyId) references Company(CompanyId), FirstName varchar(50), LastName varchar(50),Street varchar(50), City varchar(50), State varchar(50), Zip varchar(50),IsMain boolean,Email varchar(50),Phone bigint);
Create table ContactEmployee(ContactEmployeeId int primary key auto_increment, ContactId int, foreign key (ContactId) references Contact (ContactId), EmployeeId int, foreign key (EmployeeId) references Employee(EmployeeId),ContactDate date , Description varchar(50));
