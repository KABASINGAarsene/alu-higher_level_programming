-- List all privileges of the users
-- First create user_0d_1 with root privileges and user_0d_2 with specific privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

SHOW GRANTS FOR user_0d_1@'localhost';
SHOW GRANTS FOR user_0d_2@'localhost';

