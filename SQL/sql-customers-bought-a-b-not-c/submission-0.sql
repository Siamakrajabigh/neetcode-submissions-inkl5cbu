SELECT
c.customer_id,
c.customer_name
from 
customers c 
where c.customer_id IN (select customer_id from orders where product_name like 'A')
        AND c.customer_id IN (select customer_id from orders where product_name like 'B')
        AND c.customer_id NOT IN (select customer_id from orders where product_name like 'C')
order by customer_name