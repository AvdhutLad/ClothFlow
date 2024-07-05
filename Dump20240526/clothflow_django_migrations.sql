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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-03-22 13:16:15.472522'),(2,'auth','0001_initial','2024-03-22 13:16:15.871012'),(3,'admin','0001_initial','2024-03-22 13:16:15.977927'),(4,'admin','0002_logentry_remove_auto_add','2024-03-22 13:16:15.983927'),(5,'admin','0003_logentry_add_action_flag_choices','2024-03-22 13:16:15.990404'),(6,'contenttypes','0002_remove_content_type_name','2024-03-22 13:16:16.046863'),(7,'auth','0002_alter_permission_name_max_length','2024-03-22 13:16:16.092695'),(8,'auth','0003_alter_user_email_max_length','2024-03-22 13:16:16.109913'),(9,'auth','0004_alter_user_username_opts','2024-03-22 13:16:16.114912'),(10,'auth','0005_alter_user_last_login_null','2024-03-22 13:16:16.156472'),(11,'auth','0006_require_contenttypes_0002','2024-03-22 13:16:16.159474'),(12,'auth','0007_alter_validators_add_error_messages','2024-03-22 13:16:16.165376'),(13,'auth','0008_alter_user_username_max_length','2024-03-22 13:16:16.211745'),(14,'auth','0009_alter_user_last_name_max_length','2024-03-22 13:16:16.261312'),(15,'auth','0010_alter_group_name_max_length','2024-03-22 13:16:16.277385'),(16,'auth','0011_update_proxy_permissions','2024-03-22 13:16:16.282694'),(17,'auth','0012_alter_user_first_name_max_length','2024-03-22 13:16:16.328525'),(18,'home','0001_initial','2024-03-22 13:16:16.346896'),(19,'sessions','0001_initial','2024-03-22 13:16:16.378683'),(20,'home','0002_remove_staff_photo_alter_staff_phone','2024-03-22 13:44:19.964514'),(21,'home','0003_alter_staff_email','2024-03-22 18:47:48.902061'),(22,'home','0004_alter_staff_staff_id','2024-03-22 19:54:26.690462'),(23,'home','0005_staff_user_alter_staff_role','2024-03-22 22:07:21.700306'),(24,'home','0006_alter_staff_user','2024-03-23 06:58:51.268789'),(25,'home','0007_alter_staff_role_alter_staff_staff_id','2024-03-24 03:33:34.454916'),(26,'home','0008_account_details','2024-03-24 09:24:39.609303'),(27,'home','0008_account_details_bank_details','2024-03-24 11:43:52.451656'),(28,'home','0009_alter_account_details_account_no_and_more','2024-03-24 12:54:34.706790'),(29,'home','0010_staff_profile_image','2024-03-25 13:51:12.575583'),(30,'home','0011_leave_request','2024-03-26 17:13:30.445675'),(31,'home','0012_leave_request_status','2024-03-27 11:05:17.997313'),(32,'home','0013_leave_request_review_by','2024-03-27 13:07:47.157075'),(33,'inventory','0001_initial','2024-03-28 09:27:43.494365'),(34,'inventory','0002_alter_section_location_alter_section_section_name','2024-03-28 09:29:17.621613'),(35,'inventory','0003_category','2024-03-28 09:34:56.480273'),(36,'inventory','0004_brand','2024-03-29 12:06:05.165467'),(37,'inventory','0005_product','2024-03-30 07:40:20.811266'),(38,'bills','0001_initial','2024-04-02 05:38:15.493553'),(39,'bills','0002_alter_billing_discount','2024-04-02 05:47:10.865651'),(40,'bills','0003_alter_billing_final_amount','2024-04-02 05:47:52.723549'),(41,'bills','0004_alter_billing_payment_mode','2024-04-02 05:56:53.801115'),(42,'bills','0005_customer','2024-04-05 06:45:43.094402'),(43,'bills','0006_invoice','2024-04-05 07:04:39.152591'),(44,'bills','0007_invoiceitem','2024-04-05 07:14:05.152182'),(45,'bills','0008_alter_invoice_after_discount_alter_invoice_discount_and_more','2024-04-05 07:55:26.312321'),(46,'bills','0009_alter_invoice_invoice_id','2024-04-05 09:20:28.478048'),(47,'attendance','0001_initial','2024-04-06 12:42:02.267726'),(48,'bills','0010_return_and_refund','2024-04-22 16:50:24.806381'),(49,'bills','0011_return_and_refund_status','2024-04-23 08:47:01.266827'),(50,'bills','0012_defective','2024-04-23 10:00:25.008923'),(51,'bills','0013_remove_defective_product_defective_product_name','2024-04-23 12:30:58.062959'),(52,'home','0014_alter_staff_email_alter_staff_first_name_and_more','2024-04-28 12:41:55.457487'),(53,'home','0015_leave_request_reject_reason','2024-04-29 09:03:02.515845'),(54,'advertisement','0001_initial','2024-04-30 09:05:45.687988'),(55,'advertisement','0002_alter_advertisement_upload_image','2024-04-30 09:12:45.969070'),(56,'home','0016_staff_status','2024-05-06 09:31:06.945031'),(57,'home','0017_account_details_base_salary_per_hr','2024-05-06 11:07:42.381046'),(58,'salary','0001_initial','2024-05-06 16:25:20.513085'),(59,'home','0018_alter_account_details_base_salary_per_hr','2024-05-06 17:06:31.841639'),(60,'salary','0002_remove_salary_attendance','2024-05-07 03:38:09.584765'),(61,'salary','0003_alter_salary_daily_working_hours_alter_salary_date_and_more','2024-05-07 03:44:22.970894');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
