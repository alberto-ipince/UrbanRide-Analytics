SELECT

    DATENAME(MONTH, request_datetime) AS month_name,

    z.district,

    ROUND(
        SUM(t.platform_revenue),
        2
    ) AS monthly_revenue,

    RANK() OVER (

        PARTITION BY DATENAME(MONTH, request_datetime)

        ORDER BY
            SUM(t.platform_revenue) DESC

    ) AS zone_rank

FROM trips t

INNER JOIN zones z
    ON t.zone_id = z.zone_id

GROUP BY
    DATENAME(MONTH, request_datetime),
    z.district

ORDER BY
    month_name,
    zone_rank;