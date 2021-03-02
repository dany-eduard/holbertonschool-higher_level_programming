-- Lists the number of records witk the same score in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
