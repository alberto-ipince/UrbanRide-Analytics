SELECT

    c.customer_segment,

    COUNT(t.trip_id) AS total_trips,

    ROUND(
        SUM(t.final_fare),
        2
    ) AS total_revenue,

    ROUND(
        AVG(t.trip_satisfaction),
        2
    ) AS avg_trip_satisfaction,

    ROUND(
        AVG(t.dynamic_multiplier),
        2
    ) AS avg_dynamic_multiplier,

    ROUND(
        AVG(t.customer_rating),
        2
    ) AS avg_customer_rating

FROM trips t

INNER JOIN customers c
    ON t.customer_id = c.customer_id

GROUP BY c.customer_segment

ORDER BY total_revenue DESC;