SELECT Project.project_id, round(AVG(Employee.experience_years),2) AS average_years
FROM Employee
JOIN Project ON Employee.employee_id = Project.employee_id
GROUP BY Project.project_id;
