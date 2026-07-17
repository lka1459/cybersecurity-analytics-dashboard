SELECT " Average Packet Size", " Label", COUNT(*) AS total 
FROM all_traffic
GROUP BY  " Average Packet Size", " Label" 
HAVING COUNT(*) > 10
ORDER BY total DESC
LIMIT 15
