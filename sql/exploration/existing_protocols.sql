SELECT " Protocol", COUNT(*)
FROM all_traffic
GROUP BY " Protocol"
ORDER BY COUNT(*)