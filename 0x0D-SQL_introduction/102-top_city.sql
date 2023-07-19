SELECT city,avg_temp FROM (SELECT city,
 AVG(value) AS avg_temp
 FROM temperatures
 WHERE month = 7 OR month = 8
 GROUP BY city
 ORDER BY avg_temp  results LIMIT 3;
