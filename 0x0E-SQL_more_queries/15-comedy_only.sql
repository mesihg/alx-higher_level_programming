-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT A.title
FROM tv_shows AS A
INNER JOIN tv_show_genres B
ON A.id = B.show_id
INNER JOIN tv_genre AS C
ON B.genre_id = C.id
AND C.name = "Comedy"
ORDER BY A.title;
