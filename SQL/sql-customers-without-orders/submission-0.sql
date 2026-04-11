-- Write your query below
SELECT
name 
FROM customers left join orders on customers.id = orders.customer_id
where orders.id is null