use assignmentsql;
insert into Company(CompanyId,CompanyName,Street,City,State,Zip) values(1,'Urban Outfitters Inc.','MG Road','Ahmedabad','Gujarat',380001),
						  (2,'ABC Technologies Company','Solar Road','Ahmedabad','Gujarat',380002),
                          (3,'Tops Technologies','Maninagar','Ahmedabad','Gujarat',380023),
                          (4,'Tata Consultancy Services','TCS House','Mumbai','Maharastra',400001),
                          (5,'Infosys','Electronic City Phase 1','Bengaluru','Karnataka',560100),
                          (6,'Wipro','Sarjapur Road','Bengaluru','Karnataka',560035),
                          (7,'HCL Technologies','Sctor3','Noida','Uttar Pradesh',201301);
                          
select * from Company;

insert into Employee (EmployeeId,FirstName,LastName,Salary,HireDate,JobTitle,Email,Phone) values 
						  (101,'Sumit','Paul',52000,'2014-03-12','Software Developer','sumit@gmail.com','1256439875'),
                          (102,'Lesley','Bland',85000,'2015-04-21','Data Analyst','lesleybland@gmail.com','555111222350'),
                          (103,'Priya','Patel',75000,'2016-05-02','Web Developer','priyapatel@gmail.com','55641236789'),
                          (104,'Rahul','Verma',50000,'2025-06-20','Accountant','rahul12@gmail.com','5566329781'),
                          (105,'Jack','Lee',40000,'2025-12-12','Sales Executive','jack@gmail.com','56980014561'),
                          (106,'Arjun','Singh',49000,'2014-10-10','Doctor','singh100@gmail.com','5648956201'),
                          (107,'Rohit','Kumar',89000,'2020-12-30','Teacher','rohit@gmail.com','4562136975');

select * from Employee;

INSERT INTO Contact (ContactId, CompanyId, FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone) VALUES
(101, 1, 'Amit', 'Sharma', 'MG Road', 'Ahmedabad', 'Gujarat', '380001', 1, 'amit.sharma@gmail.com', '9876543210'),
(102, 5, 'Priya', 'Patel', 'SG Highway', 'Ahmedabad', 'Gujarat', '380015', 0, 'priya.patel@gmail.com', '9876543211'),
(103, 4, 'Rahul', 'Verma', 'Connaught Place', 'Delhi', 'Delhi', '110001', 1, 'rahul.verma@gmail.com', '9876543212'),
(104, 6, 'Neha', 'Gupta', 'Park Street', 'Kolkata', 'West Bengal', '700016', 0, 'neha.gupta@gmail.com', '9876543213'),
(105, 4, 'Arjun', 'Singh', 'Marine Drive', 'Mumbai', 'Maharashtra', '400002', 1, 'arjun.singh@gmail.com', '9876543214'),
(106, 7, 'Dianne', 'Connor', 'Brigade Road', 'Bangalore', 'Karnataka', '560001', 0, 'dianne@gmail.com', '9876543215'),
(107, 6, 'Rohit', 'Kumar', 'Boring Road', 'Patna', 'Bihar', '800001', 1, 'rohit.kumar@gmail.com', '9876543216'),
(108, 2, 'Pooja', 'Shah', 'Ring Road', 'Surat', 'Gujarat', '395002', 0, 'pooja.shah@gmail.com', '9876543217'),
(109, 7, 'Karan', 'Joshi', 'FC Road', 'Pune', 'Maharashtra', '411004', 1, 'karan.joshi@gmail.com', '9876543218'),
(110, 1, 'Anjali', 'Desai', 'Anna Nagar', 'Chennai', 'Tamil Nadu', '600040', 0, 'anjali.desai@gmail.com', '9876543219');

select * from Contact;

insert into ContactEmployee(ContactEmployeeId,ContactID,EmployeeId,ContactDate,Description) values
(1, 101, 101, '2024-01-10', 'Initial meeting with client'),
(2, 102, 102, '2024-01-12', 'Follow-up discussion'),
(3, 107, 102, '2024-01-15', 'Project requirement gathering'),
(4, 104, 104, '2024-01-18', 'Contract signing'),
(5, 105, 105, '2024-01-20', 'Client onboarding'),
(6, 101, 106, '2024-01-22', 'Support call'),
(7, 107, 103, '2024-01-25', 'Feedback session'),
(8, 108, 101, '2024-01-28', 'Issue resolution'),
(9, 109, 106, '2024-02-01', 'Performance review meeting'),
(10, 110, 103, '2024-02-05', 'Final project delivery discussion');

select * from contactemployee;
