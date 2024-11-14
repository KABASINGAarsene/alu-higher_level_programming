-- Use the database passed as an argument
USE hbtn_0d_usa;

-- List cities of California, assuming we know the state_id for California
-- We first select the state_id of California and then use it to find the cities
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
