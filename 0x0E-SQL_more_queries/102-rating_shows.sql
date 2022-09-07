-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT A.title, SUM(B.rating) AS rating FROM tv_shows A
INNER JOIN tv_show_ratings B
ON A.id = B.show_id
GROUP BY A.title
ORDER BY rating;
