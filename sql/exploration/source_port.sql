SELECT  " Source Port", " Label", COUNT(*) as total
FROM all_traffic
WHERE " Label" != 'BENIGN'
GROUP BY " Source Port",  " Label"
ORDER BY total DESC;
