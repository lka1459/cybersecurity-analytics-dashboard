SELECT  " Destination IP", " Label", COUNT(*) as total
FROM all_traffic
WHERE " Label" != 'BENIGN'
GROUP BY " Destination IP",  " Label"
ORDER BY total DESC