USE `evergreen`;

LOCK TABLES `candidates` WRITE, `tests` WRITE, `test_centers` WRITE, `exams` WRITE, `clients` WRITE;

INSERT INTO `candidates` (`first_name`, `last_name`, `id_type`, `id_number`) VALUES
('Amanda', 'Johnson', 'drivers_license', 'DL109213'),
('Lilian', 'Abu', 'drivers_license', 'DL0291242'),
('Julian', 'Wang', 'drivers_license', 'DL2901483'),
('Fei', 'Xie', 'passport', 'A9201923'),
('Fatima', 'Said', 'drivers_license', 'DL109213'),
('Brent', 'Ho', 'passport', 'Z209H892D');

INSERT INTO `test_centers` (`name`, `address`, `number_of_stations`) VALUES
('Maple Grove', '200 California Dr, Maple Grove', 4),
('Apple Creek', '12 Forest Ave, Apple Creek', 4);

INSERT INTO `clients` (`name`, `address`, `phone_number`, `creation_time`) VALUE
('Drawing Circle Society', '1 Circular Dr, Sphere County', '1-672-132-1241', '2020-08-10'),
('Catfish Fishing Association', '20 Riverside Ave, River City', '1-230-185-9302', '2020-08-12');

INSERT INTO `exams` (`name`, `duration`, `description`, `client_id`) VALUES
('Drawing Perfect Circle', '01:30:00', 'drawing two perfect circles using a mouse', 1),
('Drawing Concentric Circles', '06:00:00', 'drawing as many concentric circles as possible using a mouse', 1),
('Catfish Fishing License Exam', '03:00:00', 'Licensing exam to test candidate\'s knowledge of catfish fishing', 2),
('Catfish Tools License Exam', '10:00:00', 'Licensing exam to make legal tools for catfish fishing', 2);

INSERT INTO `tests` (`exam_id`, `candidate_id`, `date`, `start_time`, `test_center_id`, `status`) VALUES
(1, 1, '2020-10-13', '08:00:00', 1, 'Registered'),
(2, 6, '2020-10-13', '09:30:00', 1, 'Registered'),
(3, 4, '2020-10-13', '10:00:00', 1, 'Registered'),
(4, 3, '2020-10-13', '08:00:00', 1, 'Registered'),
(1, 2, '2020-10-13', '13:00:00', 1, 'Registered'),
(3, 5, '2020-10-13', '13:00:00', 1, 'Registered'),
(2, 1, '2020-10-13', '12:00:00', 1, 'Registered'),
(2, 5, '2020-10-19', '08:00:00', 2, 'Registered'),
(4, 1, '2020-10-19', '08:00:00', 2, 'Registered'),
(1, 4, '2020-10-13', '11:00:00', 2, 'Registered');

UNLOCK TABLES;