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
-- Table structure for table `home_bank_details`
--

DROP TABLE IF EXISTS `home_bank_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_bank_details` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(200) NOT NULL,
  `branch_name` varchar(200) NOT NULL,
  `ifsc_code` varchar(11) NOT NULL,
  `account_no` varchar(16) NOT NULL,
  `pan_no` varchar(10) NOT NULL,
  `adhar_no` varchar(12) NOT NULL,
  `bank_staff_id_id` int NOT NULL,
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `account_no` (`account_no`),
  UNIQUE KEY `pan_no` (`pan_no`),
  UNIQUE KEY `adhar_no` (`adhar_no`),
  KEY `home_bank_details_bank_staff_id_id_85499ace_fk_home_staf` (`bank_staff_id_id`),
  CONSTRAINT `home_bank_details_bank_staff_id_id_85499ace_fk_home_staf` FOREIGN KEY (`bank_staff_id_id`) REFERENCES `home_staff` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_bank_details`
--

LOCK TABLES `home_bank_details` WRITE;
/*!40000 ALTER TABLE `home_bank_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_bank_details` ENABLE KEYS */;
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
