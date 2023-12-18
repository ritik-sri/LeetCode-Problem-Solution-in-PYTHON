SELECT stock_name,
       (SUM(CASE WHEN operation = 'Sell' THEN price END) - SUM(CASE WHEN operation ='Buy' THEN price END)) AS capital_gain_loss
FROM Stocks 
GROUP BY stock_name;
