-- creating table with using unique constraint
CREATE TABLE IF NOT EXISTS unique_id(
id INT default 1 UNIQUE,
name varchar(256) 
)