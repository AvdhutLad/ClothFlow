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
-- Table structure for table `bills_invoiceitem`
--

DROP TABLE IF EXISTS `bills_invoiceitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills_invoiceitem` (
  `invoice_item_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `invoice_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`invoice_item_id`),
  KEY `bills_invoiceitem_invoice_id_87d31263_fk_bills_inv` (`invoice_id`),
  KEY `bills_invoiceitem_product_id_cfc66381_fk_inventory` (`product_id`),
  CONSTRAINT `bills_invoiceitem_invoice_id_87d31263_fk_bills_inv` FOREIGN KEY (`invoice_id`) REFERENCES `bills_invoice` (`invoice_id`),
  CONSTRAINT `bills_invoiceitem_product_id_cfc66381_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=271 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills_invoiceitem`
--

LOCK TABLES `bills_invoiceitem` WRITE;
/*!40000 ALTER TABLE `bills_invoiceitem` DISABLE KEYS */;
INSERT INTO `bills_invoiceitem` VALUES (265,'Van Heusen Business Casual Trousers',12000.00,4,48000.00,1112,20),(266,'Raymond Blazers',4500.00,5,22500.00,1112,25),(267,'W for Women Kurta Sets',6000.00,12,72000.00,1113,22),(268,'W for Women Kurta Sets',6000.00,2,12000.00,1114,22),(269,'BIBA Anarkali Dresses',6000.00,3,18000.00,1114,21),(270,'Raymond Formal Shirts',1500.00,2,3000.00,1114,23);
/*!40000 ALTER TABLE `bills_invoiceitem` ENABLE KEYS */;
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
