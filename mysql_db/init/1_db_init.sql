-- init mySQL database

-- CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS crimes;

-- CREATE USER
CREATE USER IF NOT EXISTS 'criminal'@'%' IDENTIFIED BY 'secretpw';
GRANT ALL PRIVILEGES ON crimes.* to 'criminal'@'%'
