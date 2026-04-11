
SELECT
employee_id,
case 
when employee_id%2 != 0 and name NOT LIKE 'M%' 
THEN salary
ELSE 0 
END
As bonus
from employees
order by employee_id