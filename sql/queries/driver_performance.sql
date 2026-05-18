SELECT TOP 15

    d.driver_name,

    d.primary_zone,

    COUNT(t.trip_id) AS total_trips,

    ROUND(
        SUM(t.driver_earnings),
        2
    ) AS total_driver_earnings,

    ROUND(
        AVG(t.driver_rating),
        2
    ) AS avg_driver_rating,

    ROUND(
        AVG(t.trip_satisfaction),
        2
    ) AS avg_trip_satisfaction

FROM trips t

INNER JOIN drivers d
    ON t.driver_id = d.driver_id

WHERE t.ride_status = 'Completed'

GROUP BY
    d.driver_name,
    d.primary_zone

ORDER BY total_driver_earnings DESC;