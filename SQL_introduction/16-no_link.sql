-- Using group by and order by and NOT NULL statement
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
