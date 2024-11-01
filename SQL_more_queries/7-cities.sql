-- module creates a database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, FOREIGN KEY(state_id) INT NOT NULL REFERENCES states(id), name VARCHAR(256) NOT NULL); 
