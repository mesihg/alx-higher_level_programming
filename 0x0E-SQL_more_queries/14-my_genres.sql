-- List all shows contained in hbtn_0d_tvshows 
-- and displays the number of shows linked to each
SELECT A.name
FROM tv_genres AS A
INNER JOIN tv_shows AS B
ON A.show_id = B.id
AND B.title = "Dexter"
ORDER BY A.name;
