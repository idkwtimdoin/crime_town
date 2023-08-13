-- init mySQL database

-- CREATE SCHEMA
CREATE SCHEMA IF NOT EXISTS mkultra;

-- CREATE USER
CREATE USER IF NOT EXISTS 'bush'@'%' IDENTIFIED BY 'lonegunman';
GRANT ALL PRIVILEGES ON mkultra.* to 'bush'@'%'
