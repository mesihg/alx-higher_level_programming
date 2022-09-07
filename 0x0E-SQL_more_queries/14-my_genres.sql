--  lists all genres of the show Dexter
SELECT A.name
FROM tv_genres AS A
INNER JOIN tv_show_genres B
ON A.id = B.genre_id
INNER JOIN tv_shows AS C
ON B.show_id = C.id
AND C.title = "Dexter"
ORDER BY A.name;
