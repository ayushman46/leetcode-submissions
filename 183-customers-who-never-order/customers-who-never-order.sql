Select c.name as customers from Customers c
left join orders o 
on c.id = o.customerId
where o.customerId IS NULL