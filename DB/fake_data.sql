
LOCK TABLES `candidates` WRITE, `tests` WRITE, `test_centers` WRITE, `exams` WRITE, `clients` WRITE;

INSERT INTO `candidates` (first_name, last_name, id_type, id_number) VALUES
('Amanda', 'Johnson', 'drivers_license', 'DL109213'),
('Brent', 'Ho', 'passport', 'Z209H892D');

UNLOCK TABLES;