-- script create a root user like user
CREATE USER IF NOT EXISTS 'user_0d_1'IDENTIFIED BY 'user_0d_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
