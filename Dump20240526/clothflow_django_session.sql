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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0umpubanq74or7x7qwh0os2kfwyji5e9','.eJxVjMsOwiAQRf-FtSEMjwIu3fsNZAYGWzU0Ke3K-O_apAvd3nPOfYmE2zqmrfOSpiLOAsTpdyPMD247KHdst1nmua3LRHJX5EG7vM6Fn5fD_TsYsY_fGg1wVVp5j1BidJl5AO8DUKao9RCr0QGKc6Rtro6dtRBVQELjMpIR7w_UZzeZ:1rqsKK:7BrAX1uFHk4RLzmjWS2TS4gwJXhjvXfjT_tZDNBL5LA','2024-04-14 10:22:12.076360'),('3q9syvaj0k8yhezq6bbfn5y0egliqola','.eJxVjDEOwjAMRe-SGUV2ksbAyM4ZKid2SQGlUtNOiLtDpQ6w_vfef5me16X0a9O5H8WcDaI5_I6J80PrRuTO9TbZPNVlHpPdFLvTZq-T6POyu38HhVv51sSCPpBE8cGxp6gqLuchOQSmpCABOo0oAjj41EHuMMMJaAh0dJHM-wMSAzfn:1rrDpE:UzMkhjA9ZXgUzwSV2Ek1DMdTuli9Ioo4HLS1kxGueAE','2024-04-15 09:19:32.764496'),('47gqn5q3xs4xmh1qehax365812deolps','.eJxVjMsOwiAQRf-FtSEMjwIu3fsNZAYGWzU0Ke3K-O_apAvd3nPOfYmE2zqmrfOSpiLOAsTpdyPMD247KHdst1nmua3LRHJX5EG7vM6Fn5fD_TsYsY_fGg1wVVp5j1BidJl5AO8DUKao9RCr0QGKc6Rtro6dtRBVQELjMpIR7w_UZzeZ:1rnw2m:2yRK6cnsdBS6bhIXQjKzfV3XTChwqX0NfyNy_KuqEOk','2024-04-06 07:43:56.659203'),('7mx7vi8w5sq3qogq26gsch16dmkrv598','.eJxVjMsOwiAQRf-FtSEMjwIu3fsNZAYGWzU0Ke3K-O_apAvd3nPOfYmE2zqmrfOSpiLOAsTpdyPMD247KHdst1nmua3LRHJX5EG7vM6Fn5fD_TsYsY_fGg1wVVp5j1BidJl5AO8DUKao9RCr0QGKc6Rtro6dtRBVQELjMpIR7w_UZzeZ:1s0Phc:bhn7Qu3cKmkouW2qL18K-XuhKCA3As6PYtleP3aDdzo','2024-05-10 17:49:40.179727'),('7nh8fyw6c8mzgdw0sdv5pzrz99u8lm7b','.eJxVjMsOwiAQRf-FtSEMjwIu3fsNZAYGWzU0Ke3K-O_apAvd3nPOfYmE2zqmrfOSpiLOAsTpdyPMD247KHdst1nmua3LRHJX5EG7vM6Fn5fD_TsYsY_fGg1wVVp5j1BidJl5AO8DUKao9RCr0QGKc6Rtro6dtRBVQELjMpIR7w_UZzeZ:1rolD2:5byqkSr8zD1XLuUYwWTPQu0zoWYCK1SxaR54la-49Sc','2024-04-08 14:21:56.479866'),('9bdyckqeefmpmumedac4a5sljj2cw3hd','.eJxVjDEOwjAMRe-SGUV2ksbAyM4ZKid2SQGlUtNOiLtDpQ6w_vfef5me16X0a9O5H8WcDaI5_I6J80PrRuTO9TbZPNVlHpPdFLvTZq-T6POyu38HhVv51sSCPpBE8cGxp6gqLuchOQSmpCABOo0oAjj41EHuMMMJaAh0dJHM-wMSAzfn:1rqrej:0NbMMbxcYgGXc6UP0UZMJd_Qc5wd1NXOT6D8YtKH9A0','2024-04-14 09:39:13.977465'),('cbrp78yopbgdg5er8m8b8wjndzoqc04t','.eJxVjMsOwiAQRf-FtSEMjwIu3fsNZAYGWzU0Ke3K-O_apAvd3nPOfYmE2zqmrfOSpiLOAsTpdyPMD247KHdst1nmua3LRHJX5EG7vM6Fn5fD_TsYsY_fGg1wVVp5j1BidJl5AO8DUKao9RCr0QGKc6Rtro6dtRBVQELjMpIR7w_UZzeZ:1rod5a:Nl_LXUiZiescChil8ceneXpUBO-ENtQQWosHd_lGrG8','2024-04-08 05:41:42.084975'),('f2zym0t53k3dywtxqlmo9ufn5jbek3ly','.eJxVjEEOwiAQRe_C2hAgGSgu3XsGMjMMUjUlKe2q8e62SRe6_e-9v6mE61LT2mVOY1ZX5Yy6_I6E_JLpIPmJ06NpbtMyj6QPRZ-063vL8r6d7t9BxV73WgxJMLn4EF0UB1AQSYiAA7AdCkOgyFbs4GKR7KkY8ZQJTBTcW_X5AjhWObg:1s2afB:SNhISa4AAwsFVteuTB45ogD2R8HCXEw1S8RnVLhUagY','2024-05-16 17:56:09.124786'),('y2z2c4xhpdaz26an5uhxg3jehj8h15rt','.eJxVjEEOwiAQRe_C2hAgGSgu3XsGMjMMUjUlKe2q8e62SRe6_e-9v6mE61LT2mVOY1ZX5Yy6_I6E_JLpIPmJ06NpbtMyj6QPRZ-063vL8r6d7t9BxV73WgxJMLn4EF0UB1AQSYiAA7AdCkOgyFbs4GKR7KkY8ZQJTBTcW_X5AjhWObg:1sBCxL:VQSjMt46krWPdp5OyQ3g78B042dmoBby5kqdNP7tixg','2024-06-09 12:26:31.103363');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
