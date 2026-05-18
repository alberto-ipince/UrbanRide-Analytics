SELECT
    z.district,
    COUNT(t.trip_id) AS total_trips,
    ROUND(SUM(t.final_fare), 2) AS total_revenue,
    ROUND(AVG(t.final_fare), 2) AS avg_fare,
    ROUND(AVG(t.trip_satisfaction), 2) AS avg_satisfaction
FROM trips t
INNER JOIN zones z
    ON t.zone_id = z.zone_id
GROUP BY z.district
ORDER BY total_revenue DESC;