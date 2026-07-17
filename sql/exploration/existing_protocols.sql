SELECT " Protocol", COUNT(*) AS total
FROM all_traffic
GROUP BY " Protocol"
ORDER BY total