-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL
-- CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities(
	id INT NOT NULL UNIQUE PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY REFERENCES states(id)) ENGINE=INNODB;
