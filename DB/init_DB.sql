-- create database evergreen
DROP DATABASE IF EXISTS `evergreen`;
CREATE DATABASE `evergreen`;
USE `evergreen`;

-- candidates table
-- stores names and identifications
CREATE TABLE `candidates` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(255),
    `last_name` VARCHAR(255),
    `id_type` ENUM('passport', 'drivers_license') NOT NULL,
    `id_number` varchar(255) NOT NULL
);

-- test_centers table
-- info about the test centers
CREATE TABLE `test_centers` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `number_of_stations` TINYINT UNSIGNED NOT NULL
);

-- clients table
-- stores clients info
CREATE TABLE `clients` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255),
    `phone_number` VARCHAR(20),
    `creation_time` DATE
);



-- exams table
-- stores exams info
CREATE TABLE `exams` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `duration` TIME NOT NULL,
    `description` TEXT,
    `client_id` INT NOT NULL,
    FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`)
);

-- tests table
-- stores info of each test
CREATE TABLE `tests` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `exam_id` INT NOT NULL,
    `candidate_id` INT NOT NULL,
    `date` DATE NOT NULL,
    `start_time` TIME NOT NULL,
    `test_center_id` INT NOT NULL,
    `status` ENUM('Registered', 'Canceled', 'Checked in', 'In Progress', 'Completed'),
    FOREIGN KEY (`exam_id`) REFERENCES `exams` (`id`),
    FOREIGN KEY (`candidate_id`) REFERENCES `candidates` (`id`),
	FOREIGN KEY (`test_center_id`) REFERENCES `test_centers` (`id`)
);

-- create a user for server
DROP USER IF EXISTS 'evergreen_local_server'@'localhost';
CREATE USER 'evergreen_local_server'@'localhost' IDENTIFIED BY 'evergreen_local_server';
GRANT SELECT, INSERT, DELETE, UPDATE ON `evergreen`.* TO 'evergreen_local_server'@'localhost';

