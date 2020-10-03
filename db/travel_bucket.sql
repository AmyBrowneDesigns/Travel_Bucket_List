DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES country(id)
);


-- should these be cities and countries to go with repos? it does create table though!