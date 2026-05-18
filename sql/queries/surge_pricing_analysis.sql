SELECT
    z.district,

    COUNT(*) AS total_trips,

    SUM(
        CASE
            WHEN t.surge_active = 1
            THEN 1
            ELSE 0
        END
    ) AS surge_trips,

    ROUND(
        AVG(t.dynamic_multiplier),
        2
    ) AS avg_dynamic_multiplier,

    ROUND(
        SUM(t.surge_impact),
        2
    ) AS extra_revenue_from_surge

FROM trips t

INNER JOIN zones z
    ON t.zone_id = z.zone_id

GROUP BY z.district

ORDER BY extra_revenue_from_surge DESC;