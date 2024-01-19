-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
CREATE TEMPORARY TABLE temp_comedy_shows AS
SELECT show_id
FROM tv_show_genres
WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- Select all shows without the genre 'Comedy'
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM temp_comedy_shows)
ORDER BY tv_shows.title ASC;
