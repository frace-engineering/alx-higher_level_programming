--List genries and display the number of shows linked to each
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows
