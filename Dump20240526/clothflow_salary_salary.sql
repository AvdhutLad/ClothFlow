-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: clothflow
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `salary_salary`
--

DROP TABLE IF EXISTS `salary_salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_salary` (
  `salary_id` int NOT NULL AUTO_INCREMENT,
  `based_salary` int NOT NULL,
  `daily_working_hours` double NOT NULL,
  `month_hours` double NOT NULL,
  `penalty_hours` double NOT NULL,
  `penalty_amount` decimal(10,2) NOT NULL,
  `extra_time` double NOT NULL,
  `bonus_amount` decimal(10,2) NOT NULL,
  `total_salary` decimal(10,2) NOT NULL,
  `gross_salary` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `account_id` int NOT NULL,
  `staff_id` int NOT NULL,
  PRIMARY KEY (`salary_id`),
  KEY `salary_salary_account_id_fe105cb7_fk_home_acco` (`account_id`),
  KEY `salary_salary_staff_id_b13fbc09_fk_home_staff_staff_id` (`staff_id`),
  CONSTRAINT `salary_salary_account_id_fe105cb7_fk_home_acco` FOREIGN KEY (`account_id`) REFERENCES `home_account_details` (`account_id`),
  CONSTRAINT `salary_salary_staff_id_b13fbc09_fk_home_staff_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `home_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary_salary`
--

LOCK TABLES `salary_salary` WRITE;
/*!40000 ALTER TABLE `salary_salary` DISABLE KEYS */;
INSERT INTO `salary_salary` VALUES (3,70,10,26,0,0.00,2.819999999999993,276.36,18397.17,18673.53,'2024-05-07',3,2),(4,80,10,26,12.919999999999987,103.36,0,0.00,19766.67,19663.31,'2024-05-07',4,1),(5,70,10,26,0,0.00,2.819999999999993,276.36,18397.17,18673.53,'2024-05-07',3,2),(6,80,10,26,12.92,103.36,0,0.00,19766.67,19663.31,'2024-05-07',4,1),(7,70,10,26,0,0.00,2.82,276.36,18397.17,18673.53,'2024-05-07',3,2),(8,80,10,26,12.92,103.36,0,0.00,19766.67,19663.31,'2024-05-07',4,1),(9,60,10,26,0,0.00,1.18,99.12,15671.00,15770.12,'2024-05-20',7,7),(10,80,10,26,0,0.00,0.73,81.76,20858.67,20940.43,'2024-05-20',6,6),(11,80,10,26,12.88,103.04,0,0.00,19769.33,19666.29,'2024-05-20',4,1),(12,70,10,26,0,0.00,1.42,139.16,18299.17,18438.33,'2024-05-20',3,2),(13,70,10,26,0,0.00,1.42,139.16,18299.17,18438.33,'2024-05-26',3,2),(14,70,10,26,0,0.00,9.6,940.80,18872.00,19812.80,'2024-05-26',3,2),(15,80,10,26,0,0.00,1.52,170.24,20921.33,21091.57,'2024-05-26',8,12),(16,70,10,26,0,0.00,9.6,940.80,18872.00,19812.80,'2024-05-26',3,2);
/*!40000 ALTER TABLE `salary_salary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:42:29
