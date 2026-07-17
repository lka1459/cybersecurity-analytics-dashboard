SELECT  " Destination Port", " Label", COUNT(*) as total
FROM all_traffic
WHERE " Label" != 'BENIGN'
GROUP BY " Destination Port", " Label"
ORDER BY total DESC;
