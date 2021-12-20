CREATE TABLE "repo"."table"(
    measure_date TIMESTAMP WITHOUT TIME ZONE,
    measure_type VARCHAR,
    so2 DOUBLE PRECISION,
    no2 DOUBLE PRECISION,
    no1 DOUBLE PRECISION,
    co2 DOUBLE PRECISION,
    o3 DOUBLE PRECISION,
    pm10 DOUBLE PRECISION,
    benzene DOUBLE PRECISION,
    pm2_5 DOUBLE PRECISION,

    PRIMARY KEY (measure_date, measure_type)
);
