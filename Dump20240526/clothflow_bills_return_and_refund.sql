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
-- Table structure for table `bills_return_and_refund`
--

DROP TABLE IF EXISTS `bills_return_and_refund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills_return_and_refund` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `action` varchar(10) NOT NULL,
  `reason` longtext NOT NULL,
  `return_amount` decimal(10,2) NOT NULL,
  `rejected_reason` longtext,
  `transaction_complete_date` date DEFAULT NULL,
  `customer_id` int NOT NULL,
  `invoice_id` int NOT NULL,
  `status` longtext,
  PRIMARY KEY (`transaction_id`),
  KEY `bills_return_and_ref_customer_id_1feb324c_fk_bills_cus` (`customer_id`),
  KEY `bills_return_and_ref_invoice_id_298eb9e1_fk_bills_inv` (`invoice_id`),
  CONSTRAINT `bills_return_and_ref_customer_id_1feb324c_fk_bills_cus` FOREIGN KEY (`customer_id`) REFERENCES `bills_customer` (`customer_id`),
  CONSTRAINT `bills_return_and_ref_invoice_id_298eb9e1_fk_bills_inv` FOREIGN KEY (`invoice_id`) REFERENCES `bills_invoice` (`invoice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills_return_and_refund`
--

LOCK TABLES `bills_return_and_refund` WRITE;
/*!40000 ALTER TABLE `bills_return_and_refund` DISABLE KEYS */;
INSERT INTO `bills_return_and_refund` VALUES (9,'2024-04-23','Pants',2,'exchange','Exchange request',0.00,'Exchange Request for reject. ','2024-04-22',1,1104,'approved'),(10,'2024-04-23','Shirst',3,'refund','Return reason.',1000.00,'reject message for return reason ','2024-04-15',1,1103,'approved'),(11,'2024-04-23','Pants',3,'exchange','Exchange reason.',0.00,'Exchange Request for reject. ','2024-04-05',2,1094,'canceled'),(12,'2024-04-24','Pants',3,'exchange','Exchage Reson.',0.00,NULL,'2024-04-05',2,1094,'approved'),(13,'2024-04-24','T-Shirsts',5,'refund','refund request reason from staff',1200.00,NULL,'2024-04-05',2,1094,'approved'),(14,'2024-04-24','Shirst',5,'exchange','Exchange request form staff',0.00,NULL,'2024-04-05',2,1094,'approved'),(15,'2024-04-24','Pants',5,'refund','Retrun Amount 5500 from staff ',5500.00,NULL,'2024-04-11',1,1100,'approved'),(16,'2024-04-28','Pants',3,'exchange','I want to exchange reason.',0.00,NULL,'2024-04-11',1,1100,'approved'),(17,'2024-04-28','Pants',2,'exchange','return reason.',0.00,NULL,'2024-04-11',1,1100,'approved'),(18,'2024-04-28','Pants',2,'refund','refund reason.',2000.00,NULL,'2024-04-06',1,1095,'canceled'),(19,'2024-04-28','Shirst',2,'exchange','Exchange reason.',0.00,NULL,'2024-04-15',1,1103,'pending'),(20,'2024-04-28','Shirst',3,'exchange','exchange reason.',0.00,NULL,'2024-04-06',1,1095,'pending'),(21,'2024-04-28','Denim Jeans ',2,'exchange','exchange reason.',0.00,'Exchange Request for reject from Admin. Reason Testing.','2024-04-06',1,1095,'canceled'),(22,'2024-04-28','T-Shirsts',4,'refund','Size not Appropriate for me.',15000.00,NULL,'2024-04-05',2,1094,'approved'),(23,'2024-04-28','Shirst',2,'exchange','Exchange reason approve\r\n',0.00,NULL,'2024-04-28',3,1107,'approved'),(24,'2024-04-28','Denim Jeans ',3,'exchange','Exchange reason reject',0.00,'testing','2024-04-28',3,1107,'canceled'),(25,'2024-05-26','W for Women Kurta Sets',1,'exchange','exchange reason form customer.',0.00,'reject reason from admin','2024-05-26',4,1114,'canceled');
/*!40000 ALTER TABLE `bills_return_and_refund` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:42:28
