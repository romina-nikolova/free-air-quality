CREATE TABLE "repo"."table"(
    date_time TIMESTAMP WITHOUT TIME ZONE,
    pm1 DOUBLE PRECISION,
    pm2_5 DOUBLE PRECISION,
    pm4 DOUBLE PRECISION,
    pm10 DOUBLE PRECISION,
    typical_size DOUBLE PRECISION,

    PRIMARY KEY (measure_date, measure_type)
);
