-- Create the database if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,  -
    name VARCHAR(256) NOT NULL,         
    PRIMARY KEY (id)                      
);
