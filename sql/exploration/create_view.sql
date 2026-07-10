CREATE VIEW all_traffic AS
(
    SELECT * FROM "Friday_Afternoon_DDos"
    UNION ALL
    SELECT * FROM "Friday_Afternoon_PortScan"
    UNION ALL
    SELECT * FROM "Friday_Morning"
    UNION ALL
    SELECT * FROM "Monday_Working_Hours"
    UNION ALL
    SELECT * FROM "Thursday_Afternoon_Infilteration"
    UNION ALL
    SELECT * FROM "Thursday_Morning_WebAttacks"
    UNION ALL
    SELECT * FROM "Tuesday_Working_Hours"
    UNION ALL
    SELECT * FROM "Wednesday_Working_Hours"
);
