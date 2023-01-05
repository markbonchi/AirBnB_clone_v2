-- This script prepares a MySQL server for this project
-- creates a db, usr, grant privilleges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
	    IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON *.* TO 'hbnb_dev'@'localhost';
