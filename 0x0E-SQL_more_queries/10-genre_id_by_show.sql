-- lists all shows contained in hbtn_0d_tvshows
-- db name will be passed as an argument
USE hbtn_0d_tvshows;
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id 
FROM tv_shows 
INNER JOIN tv_show_genres 
ON tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
