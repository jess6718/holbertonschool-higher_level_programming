-- script that lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT id FROM cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
