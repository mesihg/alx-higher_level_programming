-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT A.name,
 SUM(C.rate) AS rating
FROM tv_genres A
INNER JOIN tv_show_genres B
ON A.id = B.genre_id
INNER JOIN tv_show_ratings C
ON B.show_id = C.show_id
GROUP BY A.name
ORDER BY rating DESC;
