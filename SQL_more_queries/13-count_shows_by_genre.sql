-- SQL code to show null statements
SELECT 
g.name AS genre, COUNT(m.genre_id) AS number_of_shows
FROM 
tv_show_genres AS m
INNER JOIN 
tv_genres as g 
ON 
m.show_id=g.id
GROUP BY 
g.id
ORDER BY 
number_of_shows DESC