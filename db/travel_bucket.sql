DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id),
    visited BOOLEAN
    
);




-- should these be cities and countries to go with repos? it does create table though!