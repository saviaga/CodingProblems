# Write your MySQL query statement below
SELECT s.employee_id  FROM Salaries s
LEFT JOIN Employees e
ON e.employee_id = s.employee_id
WHERE e.name is null

UNION 

SELECT e.employee_id  FROM Employees e
LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE s.salary is null
ORDER BY employee_id


