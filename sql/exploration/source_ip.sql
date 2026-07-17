SELECT  " Source IP", " Label", COUNT(*) as total
FROM all_traffic
WHERE " Label" != 'BENIGN'
GROUP BY " Source IP",  " Label"
ORDER BY total DESC