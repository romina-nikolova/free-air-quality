WITH sps30 AS (
SELECT
  1 as time,
  latitude,
  longitude,
  AVG(pm2_5) as pm2_5
FROM
  "rominanikolova1/ObedientSmashing"."location_table"
JOIN "rominanikolova1/ObedientSmashing"."sps30"
ON TRUE
WHERE $__timeFilter(date_time) AND data_source = 'sps30'
GROUP BY  1,2, 3),

scraped AS (
SELECT
  1 as time,
  latitude,
  longitude,
  AVG(pm2_5) as pm2_5
FROM
  "rominanikolova1/ObedientSmashing"."location_table"
JOIN "rominanikolova1/ObedientSmashing"."meow2"
ON TRUE
WHERE $__timeFilter(measure_date) AND data_source = 'Vazrajdane'
GROUP BY 1,2, 3
)

SELECT * from sps30
UNION SELECT * FROM scraped;

