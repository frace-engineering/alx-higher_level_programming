-- creates db hbtn_0d_usa and table states
-- table schema (id INT UNIQUE AUTOGENERATE NOT NULL PRIMARY KEY, name VARCHAR(256))
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
