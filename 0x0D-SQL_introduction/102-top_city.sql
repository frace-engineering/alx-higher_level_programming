-- Display the top 3 of cities temperaturre during July and August ordered by temperature (Descending)
USE hbtn_0c_0
SELECT city, AVG(value) avg_temp
FROM temperatures
GROUP BY city
WHERE month = July OR month = August
ORDER BY avg_temp DESC
