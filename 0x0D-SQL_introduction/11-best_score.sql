-- script to display contents of second_table sorted by score
SELECT score, name
 FROM second_table
 WHERE score >= 10
 ORDER BY score DESC;
