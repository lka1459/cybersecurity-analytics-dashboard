SELECT ROUND(
        AVG("Flow Bytes/s") FILTER (
            WHERE "Flow Bytes/s" NOT IN (
                'Infinity'::double precision,
                '-Infinity'::double precision,
                'NaN'::double precision
            )
        )::numeric,
        2
    ) AS avg_flow_bytes_per_second,
ROUND (
    AVG(" Flow Packets/s") FILTER (
        WHERE "Flow Bytes/s" NOT IN (
                'Infinity'::double precision,
                '-Infinity'::double precision,
                'NaN'::double precision
            )
        )::numeric,
        2
    ) AS avg_flow_packets_per_second,
" Label" AS label, 
COUNT(*) AS total 
FROM all_traffic
WHERE " Label" IS NOT NULL
  AND TRIM(" Label") <> ''
GROUP BY " Label"
ORDER BY total DESC
