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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$DLUL7wfPcSH2479y1fXdWQ$IOs7sGjcvQ3zKpsU6QfFMIyCfudDux/Q1/6bbtFDd10=','2024-05-26 12:25:38.242617',1,'admin@gmail.com','Vidya','Lad','admin@gmail.com',1,1,'2024-03-22 13:20:56.000000'),(11,'pbkdf2_sha256$720000$Fk7LGEW4pwTFSHurC2tGhQ$vpGlgNp4BWUnnqc/G6Ozhi6m91y2o9q/y0CVk97GGxI=','2024-05-26 12:26:09.014330',0,'mayurvijaypatil2002@gmail.com','Mayur','Patil','mayurvijaypatil2002@gmail.com',0,1,'2024-03-23 07:00:42.243540'),(12,'pbkdf2_sha256$720000$lPt7Be9ZdT9DqOyhmvFiZO$2480ZhD4vegY1Uo3PKf9r97ejkkDxjmVKKUhTsr2pYE=','2024-03-31 09:43:24.147961',0,'avadhutlad@gmail.com','avadhut','lad','avadhutlad@gmail.com',0,1,'2024-03-23 07:02:07.290420'),(14,'pbkdf2_sha256$720000$9GReRpzVyL2ZkzaoqiLP8d$ou2o/ij/8CFb/FKGuyjF5JjytRZM4qtSz0CF6vWRyHU=','2024-04-29 09:22:27.458283',0,'sagar@gmail.com','sagar','patil','sagar@gmail.com',0,1,'2024-03-23 07:50:20.138473'),(16,'pbkdf2_sha256$720000$G7Ar7qXDfkaPOIpNJpEiKs$bKASrgIuYXvZBkfqRjdL/MYZ0T7LX3qGFI5trFRtQrc=','2024-03-31 10:30:55.944017',0,'anikakade@gmail.com','Aniruddha','Kakade','anikakade@gmail.com',0,1,'2024-03-23 07:52:12.837159'),(19,'pbkdf2_sha256$720000$9JCz5wDHXl3IHfr1KtBrWg$7XDl43bw3EuLMeSzxxsxFRfsWHoTariDhleUzmjXwWo=','2024-04-26 17:19:18.850581',0,'varad@gmai.com','varad','chkrawar','varad@gmai.com',0,1,'2024-03-23 17:38:44.066778'),(20,'pbkdf2_sha256$720000$N0C2lhv8jOoK8V32wTzaXe$uuuSn/MOl0XTMD80ejzjP0fQu1HNghnCoFCXIxUldf8=','2024-05-26 12:26:31.098227',0,'Raj@gmail.com','Raj','Patil','Raj@gmail.com',0,1,'2024-03-27 11:02:10.311875'),(25,'pbkdf2_sha256$720000$UK8VZCxKxuRaZc6VGB7cmI$lOiuPvkwcYH+3Z2M+z4GZGMmoVf3snFKdprIthAjGPQ=','2024-04-29 10:03:03.006091',0,'avadhutlad1919@gmail.com','avadhut','Lad','avadhutlad1919@gmail.com',0,1,'2024-04-28 14:19:17.823300'),(26,'pbkdf2_sha256$720000$q4xxfLY168pFtjXWaqB8fy$XLjenG7e3WgG3lF5ghvZx+ArNOUqHu4cuoZ72ASOELc=','2024-05-07 15:51:42.115053',0,'patil.sagar11898@gmail.com','sagar','patil','patil.sagar11898@gmail.com',0,1,'2024-04-29 09:42:46.587778'),(27,'pbkdf2_sha256$720000$80edLxTP7J4SdouqIYj69h$t/ZceuZkakCbnJN8CLkefYCSRsPNWAk0cW/mHq017ZI=','2024-05-06 09:47:11.429485',0,'mp7010153@gmail.com','MayurSTAFF','Patil','mp7010153@gmail.com',0,1,'2024-05-06 09:37:59.776534'),(28,'pbkdf2_sha256$720000$IPQXw9FrGLt4nOmwLzGvbB$nvm9tP8aOxrFx6RGkqfJqMAlHBohi8WC7bLEZFExRRI=',NULL,0,'ameydeshmukh28@gmail.com','amey','deshmukh','ameydeshmukh28@gmail.com',0,1,'2024-05-20 07:32:10.895396'),(29,'pbkdf2_sha256$720000$hRSTE5jlBPm0LOQsyDrS52$pBD713vBHtRjGVQhNjZxhkaNdxisHChRwXblTPvCKf4=','2024-05-21 04:33:26.696432',0,'rahul123@gmail.com','Rahul ','Bari','rahul123@gmail.com',0,1,'2024-05-20 14:47:48.520417');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
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
