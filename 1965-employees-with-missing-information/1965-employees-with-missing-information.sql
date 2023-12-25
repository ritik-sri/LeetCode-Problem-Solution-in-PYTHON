SELECT
    id AS employee_id
FROM (
    SELECT
        e.employee_id AS id,
        e.name,
        s.salary
    FROM
        Employees e
    LEFT JOIN
        Salaries s ON e.employee_id = s.employee_id
    UNION
    SELECT
        s.employee_id AS id,
        e.name,
        s.salary
    FROM
        Employees e
    RIGHT JOIN
        Salaries s ON e.employee_id = s.employee_id
) AS combined
WHERE
    name IS NULL OR salary IS NULL
ORDER BY
    id;
