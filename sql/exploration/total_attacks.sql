SELECT  " Label", COUNT(*) as total
FROM all_traffic
GROUP BY " Label"
ORDER BY total DESC;