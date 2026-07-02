use assinmentsql;
update Employee set Phone = '2155558800' where FirstName = 'Lesley' and LastName = 'Bland';

update Company set CompanyName = 'Urban Outfitters' where companyName = 'Urban Outfitters Inc.';

DELETE FROM ContactEmployee
WHERE ContactID IN (
    SELECT ContactID
    FROM Contact
    WHERE FirstName = 'Dianne'
      AND LastName = 'Connor'
)
or EmployeeID IN (
    SELECT EmployeeID
    FROM Employee
    WHERE FirstName = 'Jack'
      AND LastName = 'Lee'
);

select e.FirstName,e.LastName from
 Employee e join contactemployee ce on e.EmployeeId = ce.EmployeeId 
 join Contact c on c.ContactId = ce.ContactId 
 join Company co on c.CompanyId = co.CompanyId 
 where co.CompanyName = 'Toll Brothers';
 
 select * from Company where CompanyName like 'I__o%';
