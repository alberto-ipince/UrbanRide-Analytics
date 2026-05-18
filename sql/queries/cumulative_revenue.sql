SELECT

    CAST(request_datetime AS DATE) AS request_date,

    ROUND(
        SUM(platform_revenue),
        2
    ) AS daily_revenue,

    ROUND(
        SUM(
            SUM(platform_revenue)
        ) OVER (
            ORDER BY CAST(request_datetime AS DATE)
        ),
        2
    ) AS cumulative_revenue

FROM trips

GROUP BY CAST(request_datetime AS DATE)

ORDER BY request_date;