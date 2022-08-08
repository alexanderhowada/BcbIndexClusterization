CREATE TABLE IF NOT EXISTS time_series(
    d DATE,
    series_id INTEGER,
    VALUE FLOAT,
    PRIMARY KEY (d, series_id)
);
