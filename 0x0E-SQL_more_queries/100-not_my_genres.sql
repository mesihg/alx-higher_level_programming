--  lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT A.name
FROM tv_genres AS A
WHERE A.id NOT IN (
 SELECT B.genre_id FROM tv_show_genres B
INNER JOIN tv_shows C
ON B.show_id = C.id
AND C.title = "Dexter"
)
ORDER BY A.name;
