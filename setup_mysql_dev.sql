-- create two databases and and user=hbnb_dev
-- grant all privileges to hbnb_dev_db and select for performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
