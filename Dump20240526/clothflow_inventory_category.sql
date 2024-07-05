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
-- Table structure for table `inventory_category`
--

DROP TABLE IF EXISTS `inventory_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `section_id` int NOT NULL,
  PRIMARY KEY (`category_id`),
  KEY `inventory_category_section_id_0c9da8a9_fk_inventory` (`section_id`),
  CONSTRAINT `inventory_category_section_id_0c9da8a9_fk_inventory` FOREIGN KEY (`section_id`) REFERENCES `inventory_section` (`section_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_category`
--

LOCK TABLES `inventory_category` WRITE;
/*!40000 ALTER TABLE `inventory_category` DISABLE KEYS */;
INSERT INTO `inventory_category` VALUES (18,'Men\'s Clothing','Men\'s Clothing. like \r\nSuits\r\nShirts\r\nTrousers\r\nJackets',15),(19,'Women\'s Clothing','Women\'s clothing like \r\nDresses\r\nTops and Blouses\r\nSkirts\r\nPants',16),(20,'Children\'s Clothing','Children\'s Clothing like \r\nBoys\' Clothing (shirts, pants, shorts)\r\nGirls\' Clothing (dresses, tops, skirts)',17),(21,'Activewear','Products like \r\nWorkout Tops\r\nLeggings\r\nSports Bras\r\nJoggers\r\nAthletic Shorts',15),(22,'Activewear','Porduct like \r\nWorkout Tops\r\nLeggings\r\nSports Bras\r\nJoggers\r\nAthletic Shorts',16),(23,'Activewear','Porduct like \r\nWorkout Tops\r\nLeggings\r\nSports Bras\r\nJoggers\r\nAthletic Shorts',17),(24,'Seasonal and Specialty Clothing','Seasonal and Specialty Clothing like \r\nswimsuits, trunks , sweaters, thermal wear, winter coats',15),(25,'Seasonal and Specialty Clothing','porduct like sweaters, thermal wear, winter coats',16),(26,'Seasonal and Specialty Clothing','porduct like sweaters, thermal wear, winter coats',17);
/*!40000 ALTER TABLE `inventory_category` ENABLE KEYS */;
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
