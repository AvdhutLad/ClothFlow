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
-- Table structure for table `inventory_brand`
--

DROP TABLE IF EXISTS `inventory_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_brand` (
  `brand_id` int NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_brand`
--

LOCK TABLES `inventory_brand` WRITE;
/*!40000 ALTER TABLE `inventory_brand` DISABLE KEYS */;
INSERT INTO `inventory_brand` VALUES (1,'HRX','Hritik Roshan '),(2,'Being Human by sk','Salman Khan Desc edit.'),(4,'Raymond','Known for its suits, shirts, and trousers.'),(5,'Peter England',' Offers a wide range of men\'s formal and casual wear.'),(6,'Van Heusen','Popular for formal shirts, trousers, and jackets.\r\n'),(7,'BIBA','Famous for ethnic wear including dresses, tops, and skirts.'),(8,'Fabindia',': Known for traditional Indian wear and fusion outfits.'),(9,'W for Women',' Offers a variety of ethnic and fusion wear.'),(10,'Gini & Jony','Popular for boys\' and girls\' clothing'),(11,'Chicco','Known for baby clothing and accessories.'),(12,'Lilliput',' Offers a wide range of kids\' apparel.'),(13,'Nike','Provides a variety of workout tops, leggings, and sports bras.\r\n'),(14,'Adidas','Known for athletic shorts, joggers, and other activewear.'),(15,'Puma','Known for athletic shorts, joggers, and other activewear.'),(16,'Shoppers Stop','Offers a variety of brands under one roof including swimwear, winter wear, and formal wear.'),(17,'Lifestyle ','Another multi-brand retailer offering a range of seasonal and specialty clothing.');
/*!40000 ALTER TABLE `inventory_brand` ENABLE KEYS */;
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
