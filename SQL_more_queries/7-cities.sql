-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,          -- id is auto-generated, unique, and cannot be null
    state_id INT NOT NULL,                          -- state_id is a foreign key that references states.id
    name VARCHAR(256) NOT NULL,                     -- name is a non-null string (up to 256 characters)
    PRIMARY KEY (id),                               -- id is the primary key
    FOREIGN KEY (state_id) REFERENCES states(id)    -- foreign key constraint
);
