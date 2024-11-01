-- module will use join and not view
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
GROUP BY cities.id, cities.name, states.name
ORDER BY cities.id ASC;
