#1. Create DB in mysql using command
#mysql -u root -p (then enter password)
#CREATE DATABASE [name of DB - here we'll calll it todoapp]
#USE todoapp;

CREATE TABLE items (
item_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
item VARCHAR(200) NOT NULL,
uploaded_file VARCHAR(200)
);

SHOW tables;
DROP TABLE items;
DESCRIBE items;






