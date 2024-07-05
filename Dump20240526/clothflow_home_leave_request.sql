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
-- Table structure for table `home_leave_request`
--

DROP TABLE IF EXISTS `home_leave_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_leave_request` (
  `leave_id` int NOT NULL AUTO_INCREMENT,
  `reason` longtext,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `staff_id` int NOT NULL,
  `status` longtext,
  `review_by` longtext,
  `reject_reason` longtext,
  PRIMARY KEY (`leave_id`),
  KEY `home_leave_request_staff_id_42ea088b_fk_home_staff_staff_id` (`staff_id`),
  CONSTRAINT `home_leave_request_staff_id_42ea088b_fk_home_staff_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `home_staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_leave_request`
--

LOCK TABLES `home_leave_request` WRITE;
/*!40000 ALTER TABLE `home_leave_request` DISABLE KEYS */;
INSERT INTO `home_leave_request` VALUES (14,'This is cancled  request form sagar patil ','2024-03-27','2024-03-31',7,'approved','HR','staff request accetpf'),(16,'Raj cancled leave request ','2024-03-27','2024-03-30',7,'canceled','HR','staff request accetpf'),(18,'HR leave for pending to admin','2024-03-27','2024-03-30',1,'approved','Admin','staff request accetpf'),(19,'HR mayur leave for cancled ','2024-03-27','2024-03-27',1,'canceled','Admin','staff request accetpf'),(20,'HR leave for approval for admin','2024-03-27','2024-03-30',1,'approved','Admin','staff request accetpf'),(21,'Leave Request form sagar patil ','2024-03-27','2024-03-28',4,'approved','Admin','staff request accetpf'),(22,'Demo','2024-03-29','2024-03-30',4,'approved','HR','staff request accetpf'),(23,'HR mayur leave request ','2024-04-01','2024-04-02',1,'canceled','Admin','reject leave requuest '),(24,'Demo','2024-04-02','2024-04-02',7,'approved','HR','staff request accetpf'),(25,'Testing Reason for leaving. For Accept','2024-04-29','2024-04-30',12,'pending','HR','Accept leave requst.'),(26,'Testing Reason for leaving.  For Canceled. ','2024-05-01','2024-05-03',12,'pending','HR','Testing the leave request rejected reason form Email. '),(27,'Testing Reason for leaving.  For Canceled. ','2024-04-29','2024-04-30',11,'canceled','Admin','reject reason for leave.'),(28,'Testing Reason for leaving.  For Accept.','2024-05-02','2024-05-05',11,'approved','Admin','Testing Reason for leaving. For Accepting the Request.'),(29,'Wedding','2024-05-21','2024-05-31',7,'pending',NULL,NULL),(30,'I am not felling well. ','2024-05-21','2024-05-23',15,'pending',NULL,NULL),(31,'brother weeding ','2024-05-26','2024-05-27',1,'canceled','Admin','leave reject form admin due to working load');
/*!40000 ALTER TABLE `home_leave_request` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:42:27
