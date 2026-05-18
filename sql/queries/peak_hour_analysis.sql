SELECT

    DATEPART(HOUR, request_datetime) AS trip_hour,

    COUNT(*) AS total_trips,

    ROUND(
        AVG(final_fare),
        2
    ) AS avg_fare,

    ROUND(
        SUM(platform_revenue),
        2
    ) AS total_platform_revenue,

    ROUND(
        AVG(dynamic_multiplier),
        2
    ) AS avg_dynamic_multiplier,

    SUM(
        CASE
            WHEN surge_active = 1
            THEN 1
            ELSE 0
        END
    ) AS surge_trips

FROM trips

GROUP BY DATEPART(HOUR, request_datetime)

ORDER BY total_platform_revenue DESC;