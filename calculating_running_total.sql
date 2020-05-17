/*
Description

Given a posts table that contains a created_at timestamp column write a query that returns date (without time component), a number of posts for a given date and a running (cumulative) total number of posts up until a given date. The resulting set should be ordered chronologically by date.
Desired Output

The resulting set should look similar to the following:

date       | count | total
-----------+-------+-------
2017-01-26 |    20 |    20
2017-01-27 |    17 |    37
2017-01-28 |     7 |    44
2017-01-29 |     8 |    52
...

    date - (DATE) date
    count - (INT) number of posts for a date
    total - (INT) a running (cumulative) number of posts up until a date
 */

WITH data AS (
    SELECT DATE(created_at) AS date, COUNT(*) AS count_per_date, COUNT(1)
    FROM posts
    GROUP BY 1
  )
SELECT
  date,
  count_per_date AS count,
  SUM(count::int) OVER (ORDER BY date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total
FROM data;
