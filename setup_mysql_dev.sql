-- create two databases and and user=hbnb_dev
-- grant ll privileges to hbnb_dev_db and select for performance_schema

CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'loclhost';
FLUSH PRIVILEGES;
CREATE database IF NOT EXISTS performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'loclhost';
FLUSH PRIVILEGES;
