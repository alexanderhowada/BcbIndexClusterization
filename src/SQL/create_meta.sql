CREATE TABLE IF NOT EXISTS time_series_meta(
    code INTEGER PRIMARY KEY,
    name TEXT,
    unit TEXT,
    frequency VARCHAR(1),
    first_value DATE,
    last_value DATE,
    source VARCHAR(255)
);