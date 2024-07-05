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
-- Table structure for table `home_staff`
--

DROP TABLE IF EXISTS `home_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_staff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` int NOT NULL,
  `password` varchar(16) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` longtext,
  `education` varchar(15) DEFAULT NULL,
  `user_id` int NOT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`staff_id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  UNIQUE KEY `home_staff_phone_bf31677a_uniq` (`phone`),
  CONSTRAINT `home_staff_user_id_0a6bf4e4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_staff`
--

LOCK TABLES `home_staff` WRITE;
/*!40000 ALTER TABLE `home_staff` DISABLE KEYS */;
INSERT INTO `home_staff` VALUES (1,'Mayur','Vijay','Patil','mayurvijaypatil2002@gmail.com',2,'mayur@123','9823357100','Jalgaon','MCA',11,'user_img/mayur.jpg','active'),(2,'avadhut','shivaji','Lad','avadhutlad@gmail.com',2,'avadhut@123','1111111114','Kolhapur','MCA',12,'user_img/Snapchat-139031144.jpg','active'),(4,'sagar','ghansham','patil','sagar@gmail.com',1,'admin@123','2222222222','Jalgaon','B.Tech',14,'user_img/IMG_20240325_130042.jpg','active'),(5,'Aniruddha','Rajesh','Kakade','anikakade@gmail.com',2,'anikakade@123','7894561230','kolhapur','MCA',16,'','active'),(6,'Sagar','ghansham','patil','sagar@gmai.com',2,'varad@123','4545749999','Kholarpur','B.Tech',19,'user_img/IMG_20240325_122218.jpg','active'),(7,'raj','Virat','Patil','Raj@gmail.com',1,'raj@123','8888888888','PUNE','B.Tech',20,'user_img/Snapchat-1771490609.jpg','active'),(11,'avadhut','shivaji','Lad','avadhutlad1919@gmail.com',2,'Avdhut@123',NULL,'','',25,'','active'),(12,'sagar','ghansham','patil','patil.sagar11898@gmail.com',1,'Sagar@123','7878787811','jalgaon','MCA',26,'','active'),(13,'MayurSTAFF','Vijay','Patil','mp7010153@gmail.com',1,'admin@123','7878787878','jalgaon','MCA',27,'','active'),(14,'amey','pandharinath','deshmukh','ameydeshmukh28@gmail.com',1,'admin@123',NULL,'','',28,'','active'),(15,'Rahul ','Trambak','Bari','rahul123@gmail.com',2,'rahul@123','8624897561','jalgaon','MCA',29,'','active');
/*!40000 ALTER TABLE `home_staff` ENABLE KEYS */;
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
