-- First use of a subquerie to retrieve id from another table
-- Script to list all cities of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
