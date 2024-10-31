-- Using group by to return count in desc order
SELECT name, COUNT(name) AS prenom 
FROM second_table
WHERE name IS NOT NULL
GROUP BY name 
ORDER BY prenom DESC;
