-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
CREATE TEMPORARY TABLE temp_linked_genres AS
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- Select all genres not linked to 'Dexter'
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT genre_id FROM temp_linked_genres)
ORDER BY tv_genres.name ASC;
