SELECT QUERY_NAME, ROUND(AVG(RATING/POSITION), 2) AS QUALITY, ROUND(SUM(CASE WHEN RATING < 3 THEN 1 ELSE 0 END)/COUNT(RATING)*100, 2) AS POOR_QUERY_PERCENTAGE FROM QUERIES GROUP BY QUERY_NAME