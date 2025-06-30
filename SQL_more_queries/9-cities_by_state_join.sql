-- List all cities with their corresponding state names using a single SELECT with JOIN

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
