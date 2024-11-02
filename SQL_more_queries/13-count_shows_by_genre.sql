-- name selection and the using inner join
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres WHERE tv_show_genres.genre_id =tv_genres.id
GROUP BY genre HAVING COUNT(tv_show_genres.genre_id) > 0
ORDER BY number_of_shows DESC;
