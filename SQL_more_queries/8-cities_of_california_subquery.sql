-- Use the database passed as an argument
SELECT cities.id, cities.name
FROM cities
INNER JOIN states
ON states.id = cities.state_id
WHERE state_id = 1
