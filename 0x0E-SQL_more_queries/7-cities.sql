-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL UNIQUE PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY REFERENCES states(id)) ENGINE=INNODB;
ALTER TABLE states MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT;
