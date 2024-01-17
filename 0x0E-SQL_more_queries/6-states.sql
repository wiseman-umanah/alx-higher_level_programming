-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE states(id INT NOT NULL UNIQUE PRIMARY KEY, name VARCHAR(256)) ENGINE=INNODB;
ALTER TABLE states MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT;
