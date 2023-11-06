-- Display the top 3 of cities temperaturre during July and August ordered by temperature (Descending)
USE hbtn_0c_0
SELECT city, MAX(value) max_temp
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY state ASC
LIMIT 3;
