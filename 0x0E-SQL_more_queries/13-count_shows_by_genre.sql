-- List all shows contained in hbtn_0d_tvshows 
-- and displays the number of shows linked to each
SELECT A.name AS genre,
      COUNT(*) AS number_of_shows
FROM tv_genres AS A
LEFT JOIN tv_show_genres AS B
ON A.id = B.genre_id
GROUP BY A.name
ORDER BY number_of_shows DESC;
