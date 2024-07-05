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
-- Table structure for table `inventory_product`
--

DROP TABLE IF EXISTS `inventory_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  `purchase_date` date NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  `added_by` varchar(100) NOT NULL,
  `updated_by` varchar(100) NOT NULL,
  `update_date_time` datetime(6) NOT NULL,
  `update_note` longtext NOT NULL,
  `brand_id` int NOT NULL,
  `category_id` int NOT NULL,
  `section_id` int NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `inventory_product_brand_id_764cdfc1_fk_inventory_brand_brand_id` (`brand_id`),
  KEY `inventory_product_category_id_c907876e_fk_inventory` (`category_id`),
  KEY `inventory_product_section_id_863e502c_fk_inventory` (`section_id`),
  CONSTRAINT `inventory_product_brand_id_764cdfc1_fk_inventory_brand_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `inventory_brand` (`brand_id`),
  CONSTRAINT `inventory_product_category_id_c907876e_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_category` (`category_id`),
  CONSTRAINT `inventory_product_section_id_863e502c_fk_inventory` FOREIGN KEY (`section_id`) REFERENCES `inventory_section` (`section_id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_product`
--

LOCK TABLES `inventory_product` WRITE;
/*!40000 ALTER TABLE `inventory_product` DISABLE KEYS */;
INSERT INTO `inventory_product` VALUES (18,' Raymond Ready-to-Wear Formal Suits',10000.00,50,'2024-05-20','Raymond Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:31:59.950664','',4,18,15),(19,'Peter England Classic Formal Shirts',15000.00,50,'2024-05-20','Peter England Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:34:14.979233','',5,18,15),(20,'Van Heusen Business Casual Trousers',12000.00,46,'2024-05-20','Van Heusen Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 08:24:55.397569','',6,18,15),(21,'BIBA Anarkali Dresses',6000.00,47,'2024-05-20','BIBA Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-26 09:16:45.177319','',7,19,16),(22,'W for Women Kurta Sets',6000.00,36,'2024-05-20','W for Women Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-26 09:16:45.163324','',9,19,16),(23,'Raymond Formal Shirts',1500.00,48,'2024-05-20','Raymond Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-26 09:16:45.201808','',4,18,15),(24,'Raymond Trousers',2500.00,50,'2024-05-20','Raymond Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:38:22.290281','',4,18,15),(25,'Raymond Blazers',4500.00,45,'2024-05-20','Raymond Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 08:24:55.406726','',4,18,15),(26,'Peter England Casual T-Shirts',1200.00,50,'2024-05-20','Peter England Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:39:14.175287','',5,18,15),(27,'Peter England Trousers',2200.00,50,'2024-05-20','Peter England Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:39:39.509281','',5,18,15),(28,'Peter England Polo Shirts',2200.00,50,'2024-05-20','Peter England Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:39:58.030037','',5,18,15),(29,'Van Heusen Formal Shirts',1200.00,50,'2024-05-20','Van Heusen Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:40:45.508592','',6,18,15),(30,'Van Heusen Blazers',4200.00,50,'2024-05-20','Van Heusen Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:41:05.470758','',6,18,15),(31,'Van Heusen Sweaters',1500.00,50,'2024-05-20','Van Heusen Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:43:05.446267','',6,24,15),(32,'BIBA Salwar Suits',2500.00,50,'2024-05-20','BIBA Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:43:41.071739','',7,19,16),(33,'BIBA Kurtis',2500.00,50,'2024-05-20','BIBA Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:44:10.555788','',7,19,16),(34,'BIBA Lehenga Cholis',800.00,50,'2024-05-20','BIBA Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:44:30.541120','',7,19,16),(35,'W for Women Palazzos',1800.00,50,'2024-05-20','W for Women Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:45:19.796708','',9,19,16),(36,'W for Women Tunic',1800.00,50,'2024-05-20','W for Women Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:45:40.772977','',9,19,16),(37,'W for Women Dupattas',200.00,50,'2024-05-20','W for Women Luxury Cotton Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:47:07.401797','',9,19,16),(38,'Fabindia Handcrafted Kurtis',1200.00,50,'2024-05-20','Fabindia Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:51:18.580667','',8,19,16),(39,'Fabindia Sarees',2200.00,50,'2024-05-20','Fabindia Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:51:32.202188','',8,19,16),(40,'Fabindia Ethnic Tops',1200.00,50,'2024-05-20','Fabindia Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:51:53.453194','',8,19,16),(41,'Fabindia Salwar Kameez',1000.00,50,'2024-05-20','Fabindia Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:52:38.400268','',8,19,16),(42,'Gini & Jony Boys\' T-Shirts',800.00,50,'2024-05-20','Gini & Jony Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:53:16.010013','',10,20,17),(43,'Gini & Jony Girls\' Tops',500.00,50,'2024-05-20','Gini & Jony Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:53:30.249346','',10,20,17),(44,'Gini & Jony Boys\' Shorts',200.00,50,'2024-05-20','Gini & Jony Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 05:53:42.991683','',10,20,17),(45,'Gini & Jony Girls\' Dresses',1200.00,50,'2024-05-20','Gini & Jony Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:07:27.603656','',10,20,17),(46,'Chicco Baby Rompers',800.00,50,'2024-05-20','Chicco Baby Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:08:06.721809','',11,20,17),(47,'Chicco Onesies',800.00,50,'2024-05-20','Chicco Baby Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:08:27.781507','',11,20,17),(48,'Chicco Baby Sets',900.00,50,'2024-05-20','Chicco Baby Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:08:44.776058','',11,20,17),(49,'Chicco Sleepwear',500.00,50,'2024-05-20','Chicco Baby Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:09:50.394272','',11,20,17),(50,'Lilliput Girls\' Dresses',800.00,80,'2024-05-20','Lilliput Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:10:27.656235','',12,20,17),(51,'Lilliput Boys\' T-Shirts',600.00,80,'2024-05-20','Lilliput Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:10:45.473675','',12,20,17),(52,'Lilliput Boys\' Jeans',900.00,80,'2024-05-20','Lilliput Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:11:00.770681','',12,20,17),(53,'Lilliput Girls\' Skirts',900.00,80,'2024-05-20','Lilliput Luxury Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:11:17.528242','',12,20,17),(54,'Nike Dri-FIT Running Tops',1500.00,80,'2024-05-20','Nike Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:12:37.615557','',13,23,15),(55,'Nike Training Leggings',1200.00,40,'2024-05-20','Nike Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:13:19.827865','',13,23,16),(56,'Nike Sports Bras',1200.00,40,'2024-05-20','Nike Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:13:40.992655','',13,23,16),(57,'Adidas Track Pants',2000.00,40,'2024-05-20','Adidas Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:14:19.784312','',14,23,15),(58,'Adidas Performance T-Shirts',1200.00,60,'2024-05-20','Adidas Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:14:37.329937','',14,23,15),(59,'Adidas Sports Bras',1200.00,60,'2024-05-20','Adidas Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:14:51.116039','',14,23,16),(60,'Adidas Joggers',1800.00,60,'2024-05-20','Adidas Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:15:06.350443','',14,23,16),(61,'Swimwear from Speedo',500.00,60,'2024-05-20','Shoppers Stop Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:16:00.207927','',16,25,15),(62,'Winter Coats from Code',2500.00,60,'2024-05-20','Shoppers Stop Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:16:26.937054','',16,25,16),(63,'Evening Gowns from Haute Curry',3000.00,60,'2024-05-20','Shoppers Stop Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:17:22.853850','',16,25,16),(64,'Maternity Wear from Zivame',1800.00,60,'2024-05-20','Shoppers Stop Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:17:56.101704','',16,25,16),(65,'Winter Coats from Code ',2500.00,60,'2024-05-20','Lifestyle Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:18:55.046259','',17,25,15),(66,'Swimwear from Kappa',1500.00,60,'2024-05-20','Lifestyle Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:19:51.207163','',17,25,16),(67,'Formal Suits from Van Heusen',4500.00,60,'2024-05-20','Lifestyle Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:20:15.094284','',17,25,15),(68,'Loungewear from Ginger',2600.00,60,'2024-05-20','Lifestyle Ltd','Raj@gmail.com','Raj@gmail.com','2024-05-20 06:21:13.122934','',17,25,16);
/*!40000 ALTER TABLE `inventory_product` ENABLE KEYS */;
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
