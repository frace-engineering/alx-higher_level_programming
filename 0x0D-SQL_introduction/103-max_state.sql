-- Display the top 3 of cities temperaturre during July and August ordered by temperature (Descending)
USE hbtn_0c_0
SELECT state, MAX(value) max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
