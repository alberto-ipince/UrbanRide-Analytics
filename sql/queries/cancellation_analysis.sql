SELECT

    cancellation_reason,

    COUNT(*) AS total_cancellations,

    ROUND(
        AVG(waiting_time_min),
        2
    ) AS avg_waiting_time,

    ROUND(
        AVG(dynamic_multiplier),
        2
    ) AS avg_dynamic_multiplier,

    ROUND(
        SUM(final_fare),
        2
    ) AS potential_lost_revenue

FROM trips

WHERE ride_status = 'Cancelled'

GROUP BY cancellation_reason

ORDER BY total_cancellations DESC;