-- creating database and table with specific constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
 id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
 name varchar(256) NOT NULL
)
