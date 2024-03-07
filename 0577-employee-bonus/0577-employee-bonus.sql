SELECT Employee.name, Bonus.bonus 
FROM Employee 
left JOIN Bonus 
ON Employee.empId = Bonus.empId 
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;
