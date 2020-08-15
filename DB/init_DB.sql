-- candidates table
-- stores names and identifications
DROP TABLE IF EXISTS `candidates`;
CREATE TABLE 'candidates' (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(255),
    `last_name` VARCHAR(255),
    'id_type' ENUM('passport', 'drivers_license') NOT NULL,
    "id_number" varchar(255) NOT NULL
);

-- test_centers table
-- info about the test centers
DROP TABLE IF EXISTS `test_centers`;
CREATE TABLE `test_centers` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `number_of_stations` TINYINT UNSIGNED NOT NULL
);

-- clients table
-- stores clients info
DROP TABLE IF EXISTS `clients`;
CREATE TABLE 'clients' (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255),
    `phone_number` VARCHAR(20),
    `creation_time` DATE
);

-- exams table
-- stores exams info
DROP TABLE IF EXISTS `exams`;
CREATE TABLE 'exams' (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `duration` TIME NOT NULL,
    `phone_number` VARCHAR(20),
    `creation_time` DATE
);

LOCK TABLES `candidates` WRITE, `tests` WRITE, `test_centers` WRITE, `exams` WRITE, `clients` WRITE;
INSERT INTO `candidates` (first_name, last_name, id_type, id_number) VALUES
('Amanda', 'Johnson', 'drivers_license', 'DL109213'),
('Brent', 'Ho', 'passport', 'Z209H892D');
UNLOCK TABLES;
-- table