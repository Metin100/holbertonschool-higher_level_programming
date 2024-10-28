-- give default value for id in new table
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name varchar(256) 
)