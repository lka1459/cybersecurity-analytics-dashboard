SELECT " Timestamp"::date AS attack_day, " Label", COUNT(*) AS total 
FROM all_traffic
WHERE " Label" != 'BENIGN'
GROUP BY attack_day, " Label"
ORDER BY total DESC