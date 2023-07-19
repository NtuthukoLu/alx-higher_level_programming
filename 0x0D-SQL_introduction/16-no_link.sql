-- lists all records of second_table in DB
SELECT score, name FROM second_table
 WHERE name != ''
 ORDER BY score DESC;
