-- list the number of records with same score in the second_table
-- Records are sorted in descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
