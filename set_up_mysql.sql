-- This script prepares a MySQL server for this project
-- creates a db, usr, grant privilleges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
	    IDENTIFIED BY 'Hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_dev TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
