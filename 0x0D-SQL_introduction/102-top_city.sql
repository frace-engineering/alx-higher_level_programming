-- Display the top 3 of cities temperaturre during July and August ordered by temperature (Descending)
USE hbtn_0c_0
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
