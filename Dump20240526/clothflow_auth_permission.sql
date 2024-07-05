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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add staff',7,'add_staff'),(26,'Can change staff',7,'change_staff'),(27,'Can delete staff',7,'delete_staff'),(28,'Can view staff',7,'view_staff'),(29,'Can add account_details',8,'add_account_details'),(30,'Can change account_details',8,'change_account_details'),(31,'Can delete account_details',8,'delete_account_details'),(32,'Can view account_details',8,'view_account_details'),(33,'Can add bank_details',9,'add_bank_details'),(34,'Can change bank_details',9,'change_bank_details'),(35,'Can delete bank_details',9,'delete_bank_details'),(36,'Can view bank_details',9,'view_bank_details'),(37,'Can add leave_request',10,'add_leave_request'),(38,'Can change leave_request',10,'change_leave_request'),(39,'Can delete leave_request',10,'delete_leave_request'),(40,'Can view leave_request',10,'view_leave_request'),(41,'Can add section',11,'add_section'),(42,'Can change section',11,'change_section'),(43,'Can delete section',11,'delete_section'),(44,'Can view section',11,'view_section'),(45,'Can add category',12,'add_category'),(46,'Can change category',12,'change_category'),(47,'Can delete category',12,'delete_category'),(48,'Can view category',12,'view_category'),(49,'Can add brand',13,'add_brand'),(50,'Can change brand',13,'change_brand'),(51,'Can delete brand',13,'delete_brand'),(52,'Can view brand',13,'view_brand'),(53,'Can add product',14,'add_product'),(54,'Can change product',14,'change_product'),(55,'Can delete product',14,'delete_product'),(56,'Can view product',14,'view_product'),(57,'Can add billing',15,'add_billing'),(58,'Can change billing',15,'change_billing'),(59,'Can delete billing',15,'delete_billing'),(60,'Can view billing',15,'view_billing'),(61,'Can add customer',16,'add_customer'),(62,'Can change customer',16,'change_customer'),(63,'Can delete customer',16,'delete_customer'),(64,'Can view customer',16,'view_customer'),(65,'Can add invoice',17,'add_invoice'),(66,'Can change invoice',17,'change_invoice'),(67,'Can delete invoice',17,'delete_invoice'),(68,'Can view invoice',17,'view_invoice'),(69,'Can add invoice item',18,'add_invoiceitem'),(70,'Can change invoice item',18,'change_invoiceitem'),(71,'Can delete invoice item',18,'delete_invoiceitem'),(72,'Can view invoice item',18,'view_invoiceitem'),(73,'Can add attendance',19,'add_attendance'),(74,'Can change attendance',19,'change_attendance'),(75,'Can delete attendance',19,'delete_attendance'),(76,'Can view attendance',19,'view_attendance'),(77,'Can add return_and_refund',20,'add_return_and_refund'),(78,'Can change return_and_refund',20,'change_return_and_refund'),(79,'Can delete return_and_refund',20,'delete_return_and_refund'),(80,'Can view return_and_refund',20,'view_return_and_refund'),(81,'Can add defective',21,'add_defective'),(82,'Can change defective',21,'change_defective'),(83,'Can delete defective',21,'delete_defective'),(84,'Can view defective',21,'view_defective'),(85,'Can add advertisement',22,'add_advertisement'),(86,'Can change advertisement',22,'change_advertisement'),(87,'Can delete advertisement',22,'delete_advertisement'),(88,'Can view advertisement',22,'view_advertisement'),(89,'Can add salary',23,'add_salary'),(90,'Can change salary',23,'change_salary'),(91,'Can delete salary',23,'delete_salary'),(92,'Can view salary',23,'view_salary');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
