-- lists all cities of california
-- db name passed as argument
USE hbtn_0d_usa;
-- Seleect id and name columns of the table(cities) 
SELECT id, name 
FROM cities
-- Get the state_id from another select statement on the states table
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
-- Order the result by id in ascending order
ORDER BY id ASC;
