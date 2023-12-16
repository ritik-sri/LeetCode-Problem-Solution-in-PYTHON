SELECT date_id, make_name, count(distinct(lead_id)) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
