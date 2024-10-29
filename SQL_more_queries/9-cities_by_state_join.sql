-- Only use one SELECT statement
SELECT cities.id, cities.name, states.name
from cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id