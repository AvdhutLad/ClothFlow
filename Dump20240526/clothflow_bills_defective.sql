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
-- Table structure for table `bills_defective`
--

DROP TABLE IF EXISTS `bills_defective`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills_defective` (
  `defective_id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `description` longtext NOT NULL,
  `transaction_id` int NOT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`defective_id`),
  KEY `bills_defective_transaction_id_419383fa_fk_bills_ret` (`transaction_id`),
  CONSTRAINT `bills_defective_transaction_id_419383fa_fk_bills_ret` FOREIGN KEY (`transaction_id`) REFERENCES `bills_return_and_refund` (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills_defective`
--

LOCK TABLES `bills_defective` WRITE;
/*!40000 ALTER TABLE `bills_defective` DISABLE KEYS */;
INSERT INTO `bills_defective` VALUES (1,3,'Exchange Request for reject. ',11,'Pants'),(3,3,'Exchange Request accepted form admin',12,'Pants'),(4,5,'Exchange Request for approved form admin',14,'Shirst'),(5,5,'Exchange Request for approved form admin',14,'Shirst'),(6,5,'Exchange Request for approved form admin.',14,'Shirst'),(7,3,'Exchange Request accepted form admin',16,'Pants'),(8,3,'Exchange Request accepted form admin',16,'Pants'),(9,2,'Hi Mayur Patill,\n\nWe\'re pleased to inform you that your return/refund/exchange request for the following item(s) has been approved:\n\nProduct Name: Pants\nQuantity: 2\n\nTo complete the 2024-04-28, please visit our shop at Shri Collection between 2024-05-13 and Exchange. Be sure to bring a copy of your invoice or a form of identification to verify your request.\n\nIf you have any questions or need further assistance, feel free to contact us at 9657827062.\n\nThank you for choosing Shri Collection. We look forward to assisting you.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',17,'Pants'),(10,2,'Hi Mayur Patill,\n\nWe\'re pleased to inform you that your return/refund/exchange request for the following item(s) has been approved:\n\nProduct Name: Pants\nQuantity: 2\n\nTo complete the 2024-04-28, please visit our shop at Shri Collection between 2024-05-13 and Exchange. Be sure to bring a copy of your invoice or a form of identification to verify your request.\n\nIf you have any questions or need further assistance, feel free to contact us at 9657827062.\n\nThank you for choosing Shri Collection. We look forward to assisting you.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',17,'Pants'),(11,2,'Hi Mayur Patill,\n\nWe\'re pleased to inform you that your Exchange request for the following item(s) has been approved:\n\nProduct Name: Pants\nQuantity: 2\n\nTo complete the 2024-04-28, please visit our shop at Shri Collection between 2024-05-13 and Exchange. Be sure to bring a copy of your invoice or a form of identification to verify your request.\n\nIf you have any questions or need further assistance, feel free to contact us at 9657827062.\n\nThank you for choosing Shri Collection. We look forward to assisting you.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',17,'Pants'),(12,2,'Hi avadhut shivaji Lad,\n\nWe\'re pleased to inform you that your Exchange request for the following item(s) has been approved.\n\nProduct Name: Shirst\nQuantity: 2\n\nTo complete the 2024-04-28, please visit our shop at Shri Collection between 2024-05-13 and Exchange. Be sure to bring a copy of your invoice or a form of identification to verify your request.\n\nIf you have any questions or need further assistance, feel free to contact us at 9657827062.\n\nThank you for choosing Shri Collection. We look forward to assisting you.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',23,'Shirst'),(13,3,'Hi avadhut shivaji Lad,\n\nAfter reviewing your Exchange request for the following item(s), we regret to inform you that it has been rejected:\n\nProduct Name: Denim Jeans \nQuantity: 3\n\nReason for Rejection: Exchange Request for reject from Admin. Reason Testing.\n\nIf you believe this decision is incorrect or you have additional information that could change our assessment, please contact us at 9657827062. Our team will be happy to assist you.\n\nWe apologize for any inconvenience this may cause and appreciate your understanding.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',24,'Denim Jeans '),(14,2,'Hi Mayur Patill,\n\nAfter reviewing your Exchange request for the following item(s), we regret to inform you that it has been rejected:\n\nProduct Name: Denim Jeans \nQuantity: 2\n\nReason for Rejection: Exchange Request for reject from Admin. Reason Testing.\n\nIf you believe this decision is incorrect or you have additional information that could change our assessment, please contact us at 9657827062. Our team will be happy to assist you.\n\nWe apologize for any inconvenience this may cause and appreciate your understanding.\n\nBest regards,\nVidya Shivaji Lad\nFounder/Owner\nShri Collection',21,'Denim Jeans '),(15,2,'Exchange Request for reject from Admin. Reason Testing.',21,'Denim Jeans '),(16,1,'reject reason from admin',25,'W for Women Kurta Sets');
/*!40000 ALTER TABLE `bills_defective` ENABLE KEYS */;
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
