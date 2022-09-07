-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT A.title
FROM tv_shows AS A
WHERE A.id NOT IN (
 SELECT B.show_id FROM tv_show_genres B
INNER JOIN tv_genres C
ON B.genre_id = C.id
AND C.name = "Comedy"
)
ORDER BY A.title;
