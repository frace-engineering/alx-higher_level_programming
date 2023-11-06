-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
USE hbtn_0c_0
SELECT city, AVG(value) avg_temp
FROM temperatures
ORDER BY avg_temp DESC
