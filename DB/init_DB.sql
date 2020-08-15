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
    `creation_time` DATE,
    `client_id` INT(11) FOREIGN KEY REFERENCES `clients` (`id`)
);

-- tests table
-- stores info of each test
DROP TABLE IF EXISTS `tests`;
CREATE TABLE 'tests' (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `exam_id` INT(11) FOREIGN KEY REFERENCES `exams` (`id`),
    `candidate_id` INT(11) FOREIGN KEY REFERENCES `candidates` (`id`),
    `date` DATE NOT NULL,
    `start_time` TIME NOT NULL,
    `test_center_id` INT(11) FOREIGN KEY REFERENCES `test_centers` (`id`),
    `status` ENUM(`Registered`, `Canceled`, `Checked in`, `In Progress`, `Completed`)
);


