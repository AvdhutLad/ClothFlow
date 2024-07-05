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
-- Table structure for table `home_account_details`
--

DROP TABLE IF EXISTS `home_account_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_account_details` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(200) DEFAULT NULL,
  `branch_name` varchar(200) DEFAULT NULL,
  `ifsc_code` varchar(11) DEFAULT NULL,
  `account_no` varchar(16) DEFAULT NULL,
  `pan_no` varchar(10) DEFAULT NULL,
  `adhar_no` varchar(12) DEFAULT NULL,
  `staff_id_id` int NOT NULL,
  `base_salary_per_hr` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `pan_no` (`pan_no`),
  UNIQUE KEY `adhar_no` (`adhar_no`),
  UNIQUE KEY `account_no` (`account_no`),
  KEY `home_account_details_staff_id_id_50fa149a_fk_home_staff_staff_id` (`staff_id_id`),
  CONSTRAINT `home_account_details_staff_id_id_50fa149a_fk_home_staff_staff_id` FOREIGN KEY (`staff_id_id`) REFERENCES `home_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_account_details`
--

LOCK TABLES `home_account_details` WRITE;
/*!40000 ALTER TABLE `home_account_details` DISABLE KEYS */;
INSERT INTO `home_account_details` VALUES (3,'KOTAK','Dadawadi','SBIN0003327','4555555555555555','ABCDE1234F','444444444444',2,'70'),(4,'SBI','Dadawadi','SBIN0003328','4444444444444444','ABCDE1234A','111111111111',1,'80'),(5,'SBI','Dadawadi','SBIN0003329','2222222222222222','ABCDE1234B','222222222222',5,'100'),(6,'SBI','Dadawadi','SBIN0001327','4555555555555511','ABCDE1224F',NULL,6,'80'),(7,'KOTAK','Dadawadi','SBIN0002327','4555555555555512','ABCDE1124F',NULL,7,'60'),(8,'KOTAK','Dadawadi','SBIN0002527','4555555555555517','ABCDE1924F',NULL,12,'80'),(9,'KOTAK','Dadawadi','SBIN0002927','4555555555555527','ABCDE1824F',NULL,13,'70'),(10,'KOTAK','Dadawadi','SBIN0002627','5465465454654564','ABCDE1724F',NULL,15,'90'),(11,'KOTAK','Dadawadi','SBIN0002727','8787885887487487','ABRDE1724F',NULL,14,'80');
/*!40000 ALTER TABLE `home_account_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:42:30
