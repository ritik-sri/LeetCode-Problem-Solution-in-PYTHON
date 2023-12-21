SELECT
    Products.product_name,
    SUM(Orders.unit) AS unit
FROM
    Products
JOIN
    Orders ON Products.product_id = Orders.product_id
WHERE
    Orders.order_date >= '2020-02-01' AND Orders.order_date < '2020-03-01'
GROUP BY
    Orders.product_id
HAVING
    unit >= 100;
