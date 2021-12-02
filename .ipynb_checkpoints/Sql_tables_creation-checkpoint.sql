DROP DATABASE gans;

CREATE DATABASE gans;

USE gans;
-- DROP TABLE flights;
-- DROP TABLE cities;
-- DROP TABLE weather;
CREATE TABLE IF NOT EXISTS cities (

    City VARCHAR(200),
    Country VARCHAR(200),
    Population INT,
    Country_code VARCHAR(3),
    CityCountry VARCHAR(204),
    Airport_name VARCHAR(200),
    icao VARCHAR(5),
    PRIMARY KEY(CityCountry)
);


CREATE TABLE IF NOT EXISTS flights (
	flight_id INT NOT NULL AUTO_INCREMENT,
    From_city VARCHAR(200),
    Arrival_Local_time DATETIME,
    Arrival_UTC_time DATETIME,
    Terminal VARCHAR(200),
    Airline VARCHAR (200),
    Flight_number VARCHAR(20),
    Aircraft_model VARCHAR(200),
    CityCountry VARCHAR(200),
    icao VARCHAR(5),
    PRIMARY KEY(flight_id),
    FOREIGN KEY (CityCountry) REFERENCES cities(CityCountry)
    
);

CREATE TABLE IF NOT EXISTS weather (
	weather_id INT NOT NULL AUTO_INCREMENT,
    Date_Time DATETIME,
	Temperature FLOAT,       
	Feels_like FLOAT,      
	Humidity INT,         
	Weather VARCHAR(200),       
	Clouds INT,         
	Wind_speed FLOAT,
	Rain VARCHAR(100),
	Snow VARCHAR(100),
	CityCountry VARCHAR(200),
    PRIMARY KEY(weather_id),
    FOREIGN KEY (CityCountry) REFERENCES cities(CityCountry)
);



