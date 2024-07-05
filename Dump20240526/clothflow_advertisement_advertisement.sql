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
-- Table structure for table `advertisement_advertisement`
--

DROP TABLE IF EXISTS `advertisement_advertisement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `advertisement_advertisement` (
  `advertisement_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `upload_image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `clauses` longtext NOT NULL,
  `upload_date` datetime(6) NOT NULL,
  PRIMARY KEY (`advertisement_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advertisement_advertisement`
--

LOCK TABLES `advertisement_advertisement` WRITE;
/*!40000 ALTER TABLE `advertisement_advertisement` DISABLE KEYS */;
INSERT INTO `advertisement_advertisement` VALUES (5,'advertisement title 3','2024-04-30','2024-05-08','/8713543.jpg','desc','terms and conditions.','2024-04-30 09:51:53.885091'),(6,'advertisement title 1','2024-04-30','2024-05-08','/09-3.jpg','desc 1','term and conditions 1','2024-04-30 10:09:04.629406'),(7,'advertisement title 2','2024-04-30','2024-05-08','/CeCrU.jpg','desc 2','term and condition 2','2024-04-30 10:09:40.593975'),(8,'advertisement title 4','2024-05-01','2024-05-08','/images.jpeg','desc4','terms and conditions 4','2024-04-30 10:10:32.637099'),(9,'Being Gentleman','2024-05-20','2024-06-01','/5502536_2871042.jpg','Get expert fashion guidance to find the perfect suit for any occasion','Consultations are by appointment only and subject to availability.\r\nAll advice provided is based on current fashion trends and individual preferences.\r\nNo refunds or exchanges on custom-tailored suits unless due to fitting errors.\r\nClients are responsible for providing accurate measurements and information.','2024-05-20 07:08:14.042909'),(10,'Slay Cosy ','2024-05-20','2024-06-01','/9005948_4069490.jpg','Discover your ideal t-shirt with our personalized style tips and recommendations.','Consultations are available by appointment and subject to availability.\r\nRecommendations are based on current fashion trends and individual preferences.\r\nNo refunds or exchanges on custom-printed t-shirts unless due to printing errors.\r\nClients must provide accurate size and design information.','2024-05-20 07:15:31.480754'),(11,'Summer Sale ','2024-05-20','2024-06-01','/9417145_4163215.jpg','Enjoy unbeatable discounts on your favorite summer styles during our exclusive Summer Sale!','Offers valid while supplies last and on selected items only.\r\nDiscounts cannot be combined with other promotions or applied to previous purchases.\r\nAll sales are final; no returns or exchanges unless items are defective.\r\nSale dates and terms are subject to change without prior notice.','2024-05-20 07:20:19.497841'),(13,' Perfect Travel Attire Made Easy','2024-05-20','2024-06-01','/13403837_5207614.jpg','Find the perfect travel attire with our expert style recommendations for comfort and fashion on the go.','Advice is provided by appointment and subject to availability.\r\nRecommendations are tailored to individual preferences and travel needs.\r\nNo refunds or exchanges on personalized travel outfits unless due to manufacturing defects.\r\nClients must provide accurate travel details and size information.','2024-05-20 07:26:08.735023');
/*!40000 ALTER TABLE `advertisement_advertisement` ENABLE KEYS */;
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
