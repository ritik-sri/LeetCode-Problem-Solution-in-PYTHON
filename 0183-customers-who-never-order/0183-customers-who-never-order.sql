
select name as Customers from Customers
where id NOT IN ( select customerId from Orders) ;

