SELECT ROUND(AVG(" Flow Duration")::numeric, 2) AS "Flow Duration", 
ROUND(AVG(" Total Fwd Packets")::numeric, 2) AS "Total Fwd Packets",
ROUND(AVG(" Total Backward Packets")::numeric, 2) AS "Total Bwd Packets",
ROUND(AVG("Total Length of Fwd Packets")::numeric, 2) AS "Fwd Packets Total Length",
ROUND(AVG(" Total Length of Bwd Packets")::numeric, 2) AS "Bwd Packets Total Length",
" Label" AS "Label", 
COUNT(*) AS total 
FROM all_traffic
GROUP BY " Label" 
ORDER BY total DESC
