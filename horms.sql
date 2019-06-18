-- MySQL dump 10.17  Distrib 10.3.14-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: horms
-- ------------------------------------------------------
-- Server version	10.3.14-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (2,'pbkdf2_sha256$120000$OqmTzVxsMl0Z$n+vvPAzHixBeHHEXyZ+eFKLmijAx5TFIm8EbDnTyeK8=','christopher','shoo','chris@gmail.com','',1,1,1,'2019-03-11 07:08:51.000000','2019-03-11 07:10:11.907840'),(7,'pbkdf2_sha256$120000$072lQjxDqQDM$tOHImE9An/VV3OPKmv3QkKZYcggia2pG/iaT6uE/UqU=','michael','assey','omakei96@gmail.com','',1,0,0,'2019-03-16 05:03:45.180559','2019-03-16 05:06:21.522741'),(8,'pbkdf2_sha256$150000$56XhBT5ePYVh$qxzP9nSEVC0kAw/2QpDTsDvZFMBs64L6/XSgzHb950A=','christopher','shoo','admin@horms.org','',1,1,1,'2019-05-05 07:38:43.000000','2019-06-09 13:55:11.943004'),(19,'pbkdf2_sha256$150000$OPuHpIoUCzSV$YcEiBsULbwnkZoj97S8iwjylLIka75zYMlR+alZtmCU=','christopher','shoo','christopherbenson17@gmail.com','',1,0,0,'2019-05-05 14:03:55.487551','2019-05-16 23:16:04.650394'),(20,'pbkdf2_sha256$150000$iwcyGQ5OfFuD$UOrAS9bKXWPIjkIUNK4rqG4NObKII5mHnxkkJjBlojE=','chris','heheheh','hdhdhdh@gmail.com','',0,0,0,'2019-05-05 14:16:12.693992','2019-05-05 14:16:12.694005'),(21,'pbkdf2_sha256$150000$3QVm8nopr7Dm$pPj+4WC38MoptFMC6xgIwrQvkFb9Wxq02294iGbHS0k=','bdbdhh','hdhdh','yyye@gmail.com','',0,0,0,'2019-05-05 14:18:02.793300','2019-05-05 14:18:02.793334'),(22,'pbkdf2_sha256$150000$Z81XmginlLXk$r2eozvhNiNy8naB8mKrPTKJ+iaLYWsz8hcuTJDBNTKc=','hdhdhdh','hdhdhdh','hdhdh@gmail.com','',0,0,0,'2019-05-05 14:19:21.433911','2019-05-05 14:19:21.433930'),(23,'pbkdf2_sha256$150000$o4BxKeXli5zN$s1rRbcVmuPy3A4drYWuPWIZ05IEG6zu1qlOz2CL/Z8o=','hdhdh','hdhdhd','hdhdh@hdhd.com','',1,0,0,'2019-05-05 14:25:05.147748','2019-05-06 15:37:54.452938'),(24,'pbkdf2_sha256$150000$lkGkbgSrS5Ds$gBpNXStZjwzVl9yu23gW1+otZT9VvEB7u6MWTN5Ic/8=','hdhdhdh','hdhdhd','lalalalalueue@gmail.com','',0,0,0,'2019-05-05 14:31:43.121451','2019-05-05 14:31:43.121474'),(25,'pbkdf2_sha256$150000$fne8shXBAnPq$6dRjGGBhrvUCHeLKAh7SE4bdE/LQZdUYPjb9SOpQN4E=','hdhdhd','hdhdhd','pqpqpqpqp@gmail.com','',0,0,0,'2019-05-05 14:33:41.014659','2019-05-05 14:33:41.014677'),(26,'pbkdf2_sha256$150000$VHKs7u9CRpV1$xIe5xINY7eA1ZbTx9qz9+yy8t5xd03xlRsHeIiVj69c=','musty','hdhdh','hdhhdhdhjsks@gmail.com','',1,0,0,'2019-05-06 02:27:41.809714','2019-05-06 02:27:41.809763'),(27,'pbkdf2_sha256$150000$Z52j0DXZhgRL$KaUyuztP+vAvHGFC7FMyNYGma1hkTGRl2TljqJ8hJ0c=','joan','henry','jhenry081@gmail.com','',1,0,0,'2019-05-06 05:21:14.052587','2019-05-06 05:21:14.052596'),(28,'pbkdf2_sha256$150000$SDjLtNli0wTw$cwg+FgTw2m/YoIalZyIah2XDtlgF9PMAutAfyvihWHM=','Mustapha','Hamisi','mustapha@gmail.com','',1,1,1,'2019-05-16 23:17:27.919139','2019-05-16 23:37:15.599527'),(29,'pbkdf2_sha256$150000$51RYLVR7iSNN$nQrsccH9qWzLo7k254ITAP1O7hIV/TLDg5DpQSBT1Ow=','john','liam','crystalsproducts@gmail.com','',1,0,0,'2019-05-16 23:54:10.456041','2019-05-16 23:55:22.102833'),(30,'pbkdf2_sha256$150000$hyz5oTckNpuU$kpZu8AL5OimcytqMZHdIeoWV6LfTCngwpxyOXO/I41U=','Lotti','Hamza','lott.champs@gmail.com','',1,0,0,'2019-05-17 01:37:17.601079','2019-05-17 01:38:20.249742');
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_picture` varchar(100) DEFAULT NULL,
  `bio` longtext DEFAULT NULL,
  `activation_key` int(11) DEFAULT NULL,
  `activation_key_expirity` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_userprofile_user_id_92240672_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

LOCK TABLES `accounts_userprofile` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES (6,'',NULL,41357,'2019-03-18 05:03:45.352309',7),(17,'',NULL,30989,'2019-05-18 23:09:37.055815',19),(18,'',NULL,2352,'2019-05-07 14:16:12.870315',20),(19,'',NULL,3018,'2019-05-07 14:18:02.964815',21),(20,'',NULL,3042,'2019-05-07 14:19:21.613018',22),(21,'',NULL,2424,'2019-05-07 14:25:05.326237',23),(22,'',NULL,2801,'2019-05-07 14:31:43.290955',24),(23,'',NULL,2945,'2019-05-07 14:33:41.192433',25),(24,'',NULL,496654,'2019-05-08 02:27:42.892833',26),(25,'',NULL,751705,'2019-05-08 05:21:14.277776',27),(26,'',NULL,743700,'2019-05-18 23:54:10.660160',29),(27,'',NULL,729115,'2019-05-19 01:37:17.780397',30),(28,'users/2019/06/09/cropped-1366-768-414147.jpg','',-1,'2019-06-09 22:31:50.000000',8);
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add custom user',1,'add_customuser'),(2,'Can change custom user',1,'change_customuser'),(3,'Can delete custom user',1,'delete_customuser'),(4,'Can view custom user',1,'view_customuser'),(5,'Can add user profile',2,'add_userprofile'),(6,'Can change user profile',2,'change_userprofile'),(7,'Can delete user profile',2,'delete_userprofile'),(8,'Can view user profile',2,'view_userprofile'),(9,'Can add log entry',3,'add_logentry'),(10,'Can change log entry',3,'change_logentry'),(11,'Can delete log entry',3,'delete_logentry'),(12,'Can view log entry',3,'view_logentry'),(13,'Can add permission',4,'add_permission'),(14,'Can change permission',4,'change_permission'),(15,'Can delete permission',4,'delete_permission'),(16,'Can view permission',4,'view_permission'),(17,'Can add group',5,'add_group'),(18,'Can change group',5,'change_group'),(19,'Can delete group',5,'delete_group'),(20,'Can view group',5,'view_group'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add Hall',8,'add_hall'),(30,'Can change Hall',8,'change_hall'),(31,'Can delete Hall',8,'delete_hall'),(32,'Can view Hall',8,'view_hall'),(33,'Can add Living place',9,'add_livingplace'),(34,'Can change Living place',9,'change_livingplace'),(35,'Can delete Living place',9,'delete_livingplace'),(36,'Can view Living place',9,'view_livingplace'),(37,'Can add Office',10,'add_office'),(38,'Can change Office',10,'change_office'),(39,'Can delete Office',10,'delete_office'),(40,'Can view Office',10,'view_office'),(41,'Can add Place',11,'add_place'),(42,'Can change Place',11,'change_place'),(43,'Can delete Place',11,'delete_place'),(44,'Can view Place',11,'view_place'),(45,'Can add Image of a place',12,'add_placeimage'),(46,'Can change Image of a place',12,'change_placeimage'),(47,'Can delete Image of a place',12,'delete_placeimage'),(48,'Can view Image of a place',12,'view_placeimage'),(49,'Can add joan hostel',13,'add_joanhostel'),(50,'Can change joan hostel',13,'change_joanhostel'),(51,'Can delete joan hostel',13,'delete_joanhostel'),(52,'Can view joan hostel',13,'view_joanhostel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-03-11 07:10:24.667982','1','christopherbenson17@gmail.com',3,'',1,2),(2,'2019-03-11 07:19:34.189859','3','christopherbenson17@gmail.com',3,'',1,2),(3,'2019-03-13 03:54:49.671425','1','Nyumba ya kupanga',1,'[{\"added\": {}}]',11,2),(4,'2019-03-13 03:55:34.265399','1','Nyumba ya kupanga',1,'[{\"added\": {}}]',9,2),(5,'2019-03-13 03:58:25.502331','1','Nyumba ya kupanga',1,'[{\"added\": {}}]',12,2),(6,'2019-03-13 03:58:32.325326','2','Nyumba ya kupanga',1,'[{\"added\": {}}]',12,2),(7,'2019-03-13 03:58:43.540234','3','Nyumba ya kupanga',1,'[{\"added\": {}}]',12,2),(8,'2019-03-16 05:03:39.654102','6','omakei96@gmail.com',3,'',1,2),(9,'2019-05-05 07:39:55.292087','4','christopherbenson17@gmail.com',3,'',1,8),(10,'2019-05-05 07:39:55.349517','5','cristwinshoo@gmail.com',3,'',1,8),(11,'2019-05-05 13:37:31.518097','9','christopkherbenson17@gmail.com',3,'',1,8),(12,'2019-05-05 13:37:31.566850','10','christopherbenfs@gmail.com',3,'',1,8),(13,'2019-05-05 14:02:53.019308','11','christopherbenson17@gmail.com',3,'',1,8),(14,'2019-05-05 14:02:53.093239','12','shoo@gmail.com',3,'',1,8),(15,'2019-05-05 14:02:53.182572','13','bdbd@gmail.com',3,'',1,8),(16,'2019-05-05 14:02:53.227320','14','hdhdh@gmail.com',3,'',1,8),(17,'2019-05-05 14:02:53.271742','15','hdhdhbcbcb@gmail.com',3,'',1,8),(18,'2019-05-05 14:02:53.316518','16','hdhdhdhdhd@gmail.com',3,'',1,8),(19,'2019-05-05 14:02:53.361279','17','eliot@gmail.com',3,'',1,8),(20,'2019-05-05 14:02:53.405774','18','bzbdb@gmail.com',3,'',1,8),(21,'2019-05-06 05:15:26.722260','1','changombe',1,'[{\"added\": {}}]',13,8),(22,'2019-05-06 05:15:39.330457','2','dit',1,'[{\"added\": {}}]',13,8),(23,'2019-05-06 15:32:19.102660','23','hdhdh@hdhd.com',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',1,8),(24,'2019-05-12 15:26:41.191226','9','dsfasdfs',1,'[{\"added\": {}}]',11,8),(25,'2019-05-12 15:26:56.395869','10','fsfds',1,'[{\"added\": {}}]',11,8),(26,'2019-05-12 15:27:12.053441','11','sdfsdf',1,'[{\"added\": {}}]',11,8),(27,'2019-05-13 00:33:44.559404','12','Kinyerezi',1,'[{\"added\": {}}]',11,8),(28,'2019-05-13 00:47:09.519744','12','Kinyerezi',3,'',11,8),(29,'2019-05-13 00:47:09.607487','11','sdfsdf',3,'',11,8),(30,'2019-05-13 00:47:09.651758','10','fsfds',3,'',11,8),(31,'2019-05-13 00:47:09.696313','9','dsfasdfs',3,'',11,8),(32,'2019-05-13 00:47:09.740843','8','mbagala',3,'',11,8),(33,'2019-05-13 00:48:26.709310','13','Nyumba ya inapangishwa',1,'[{\"added\": {}}]',11,8),(34,'2019-05-13 00:49:18.691327','14','Office for rent',1,'[{\"added\": {}}]',11,8),(35,'2019-05-13 00:50:03.117493','15','Hall for renting',1,'[{\"added\": {}}]',11,8),(36,'2019-05-13 01:21:48.427905','1','Nyumba ya inapangishwa',1,'[{\"added\": {}}]',9,8),(37,'2019-05-13 01:23:42.457158','1','Office for rent',1,'[{\"added\": {}}]',10,8),(38,'2019-05-13 01:24:28.256123','1','Hall for renting',1,'[{\"added\": {}}]',8,8),(39,'2019-05-13 04:21:09.072218','1','Nyumba ya inapangishwa',1,'[{\"added\": {}}]',12,8),(40,'2019-05-16 23:17:28.190306','28','mustapha@gmail.com',1,'[{\"added\": {}}]',1,8),(41,'2019-05-16 23:17:47.123578','28','mustapha@gmail.com',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"is_staff\", \"is_superuser\", \"is_active\"]}}]',1,8),(42,'2019-06-09 22:31:53.006637','28','admin@horms.org',1,'[{\"added\": {}}]',2,8);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'accounts','customuser'),(2,'accounts','userprofile'),(3,'admin','logentry'),(5,'auth','group'),(4,'auth','permission'),(6,'contenttypes','contenttype'),(8,'homs','hall'),(13,'homs','joanhostel'),(9,'homs','livingplace'),(10,'homs','office'),(11,'homs','place'),(12,'homs','placeimage'),(7,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-11 06:46:10.490332'),(2,'contenttypes','0002_remove_content_type_name','2019-03-11 06:46:11.552575'),(3,'auth','0001_initial','2019-03-11 06:46:15.863032'),(4,'auth','0002_alter_permission_name_max_length','2019-03-11 06:46:16.579081'),(5,'auth','0003_alter_user_email_max_length','2019-03-11 06:46:16.639158'),(6,'auth','0004_alter_user_username_opts','2019-03-11 06:46:16.690227'),(7,'auth','0005_alter_user_last_login_null','2019-03-11 06:46:16.747554'),(8,'auth','0006_require_contenttypes_0002','2019-03-11 06:46:16.791371'),(9,'auth','0007_alter_validators_add_error_messages','2019-03-11 06:46:16.847591'),(10,'auth','0008_alter_user_username_max_length','2019-03-11 06:46:16.904922'),(11,'auth','0009_alter_user_last_name_max_length','2019-03-11 06:46:16.958773'),(12,'accounts','0001_initial','2019-03-11 06:46:22.990833'),(13,'accounts','0002_delete_systeminfo','2019-03-11 06:46:23.237834'),(14,'admin','0001_initial','2019-03-11 06:46:25.069417'),(15,'admin','0002_logentry_remove_auto_add','2019-03-11 06:46:25.117841'),(16,'admin','0003_logentry_add_action_flag_choices','2019-03-11 06:46:25.170031'),(17,'sessions','0001_initial','2019-03-11 06:46:25.808387'),(18,'accounts','0003_auto_20190311_0709','2019-03-11 07:09:53.858095'),(19,'accounts','0004_remove_customuser_user_role','2019-03-11 11:41:22.306337'),(20,'homs','0001_initial','2019-03-13 03:45:38.763798'),(21,'homs','0002_auto_20190313_0350','2019-03-13 03:50:18.584916'),(22,'homs','0003_auto_20190313_0350','2019-03-13 03:50:37.414627'),(23,'homs','0004_auto_20190313_0354','2019-03-13 03:54:30.047160'),(24,'homs','0005_placeimage_image','2019-03-13 03:57:59.331570'),(25,'homs','0006_auto_20190313_0358','2019-03-13 03:58:10.390206'),(26,'homs','0007_auto_20190313_0735','2019-03-13 07:35:46.763686'),(27,'auth','0010_alter_group_name_max_length','2019-05-05 07:33:41.206433'),(28,'auth','0011_update_proxy_permissions','2019-05-05 07:33:41.273861'),(29,'homs','0008_joanhostel','2019-05-06 05:15:00.595374'),(30,'homs','0009_place_cover_photo','2019-05-13 04:22:08.067222'),(31,'homs','0010_auto_20190513_0436','2019-05-13 04:36:46.983656'),(32,'homs','0011_auto_20190609_1226','2019-06-09 12:26:55.685735');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('02gzusn9h7b6x0kes53r1f9eeyc7drbi','MzY1NjdlMzQ3MmMxNmEzOTQ1YWM5ZGMzODFhZmM2YzRkNDg0YzcyOTp7Il9hdXRoX3VzZXJfaWQiOiIyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGMwYTEzYjRiMzFjNmFiNWI2MmZkMTM0Zjk5NTVkY2E0ZjBhNzY4ZSJ9','2019-05-31 01:27:50.465338'),('1d2gurxa42t7n36kggirg7u4e5wc0mho','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-30 23:13:42.036582'),('1jzdk0u1c06rbierl2t4xmypjmgduz01','YTllYzk1YWE4ZDIwM2FjOTkxZGZiMDc0NzRiMDEzODU5MzYyMTVjZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwMjhiMzhkYzExMTRjNGNmZDQ5YWYxNzFkMzBhMDQ4ZGM4NzY2OTk1In0=','2019-03-30 05:05:31.860019'),('2z1s8p9yccg4gb1akh0u5vxbijxmk1hl','ZGYzYjI3ZDkwNTRiYmQwZTA5YjQyNjZlY2RhZjBlMTNlMzE1NmFlNDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZGZhNWI4MDkzMDgzYTllNDEyZjQ4NjUxOGY5MGNlYjFmZjgxZmU2In0=','2019-05-26 15:27:12.545980'),('59nenxgx2nqn2qiklnwajabafe1xfzfr','Zjk5YjZkOWZhYTExMWQ2YWNhZjE3NmNjMDQ0OTI1MTA3YjlhNmYxODp7InVzZXJuYW1lIjoiaGRoZGhAaGRoZC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJmMjAzYjg1ZTUyNTc5MWU3ZmM1ZDdiNWI3OWYzN2Q2MzgxZTRjN2YifQ==','2019-05-20 15:37:54.509831'),('5bd0gl1omz9r5mzjv8vbvisi20kym3kg','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-30 23:16:04.707635'),('5bm3jd68m75ckqidq2g2pp860855clpv','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-26 12:16:32.535700'),('82l98nlc4nx4jktzzqzwvup6zwd1v2iy','NzEwNWMwMTNjYmUwOTJiNDIyZTlmZDU4MjU3MjliMzRiOWQ1YTA5Mzp7InVzZXJuYW1lIjoibXVzdGFwaGFAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9pZCI6IjI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YzBhMTNiNGIzMWM2YWI1YjYyZmQxMzRmOTk1NWRjYTRmMGE3NjhlIn0=','2019-05-30 23:37:15.659391'),('92tnpthhgl5tkq4pqtlmcr1h8q6eowgu','Y2NlMzMxZmE4M2MyZTYyYzdhMmQ2NGZlZWQ5MmZhM2JmMWIwM2M3Nzp7InVzZXJuYW1lIjoiY3J5c3RhbHNwcm9kdWN0c0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImI3MDEwYWUwOWMwNDdmMjViNGZmNGExY2FlNDRmZTQ1MmYxNGQ5NmUifQ==','2019-05-30 23:55:22.228087'),('bxkie0hwj6orqsul72d2bc9herq14qwg','ZGYzYjI3ZDkwNTRiYmQwZTA5YjQyNjZlY2RhZjBlMTNlMzE1NmFlNDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZGZhNWI4MDkzMDgzYTllNDEyZjQ4NjUxOGY5MGNlYjFmZjgxZmU2In0=','2019-06-06 13:47:05.248691'),('ea1sb5h40ofmcjybcovf31witmgocq5h','Zjk5YjZkOWZhYTExMWQ2YWNhZjE3NmNjMDQ0OTI1MTA3YjlhNmYxODp7InVzZXJuYW1lIjoiaGRoZGhAaGRoZC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJmMjAzYjg1ZTUyNTc5MWU3ZmM1ZDdiNWI3OWYzN2Q2MzgxZTRjN2YifQ==','2019-05-20 15:37:45.226128'),('ftijwmg372jrzb2xhrct8biqnzu5kijb','ZGYzYjI3ZDkwNTRiYmQwZTA5YjQyNjZlY2RhZjBlMTNlMzE1NmFlNDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZGZhNWI4MDkzMDgzYTllNDEyZjQ4NjUxOGY5MGNlYjFmZjgxZmU2In0=','2019-06-23 22:31:53.577902'),('gv4l8tc5okaw6pe10f6m9pf9cgxu4dli','NjRiOTQxNTVhZTJlOTFjZGExZGVkOTU5YjRmMzYxNDU4ZDZmOTU5YTp7InVzZXJuYW1lIjoibG90dC5jaGFtcHNAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9pZCI6IjMwIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlOTY3NGJiMDgyNGFkZmZlMjM2ZDNkMTg0ZjYyODBhMDc0OWEzNzgyIn0=','2019-05-31 01:38:20.340216'),('ibiqccej7pcrhom7lx9k3njgw660nwu6','ZGYzYjI3ZDkwNTRiYmQwZTA5YjQyNjZlY2RhZjBlMTNlMzE1NmFlNDp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZGZhNWI4MDkzMDgzYTllNDEyZjQ4NjUxOGY5MGNlYjFmZjgxZmU2In0=','2019-05-20 05:16:12.879732'),('izpz5hptkpjtk48k06fqjqksqqfr7dyc','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-26 00:49:53.597417'),('lin379pjzvq0s50q724akwf5071qw7f8','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-30 23:11:59.001022'),('my12vkkq0xrb2fx93yntgyqmovrs8ch8','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-26 07:32:16.244458'),('q35dhkikgc71blc4u1b11vrnelmv7oj1','Zjk5YjZkOWZhYTExMWQ2YWNhZjE3NmNjMDQ0OTI1MTA3YjlhNmYxODp7InVzZXJuYW1lIjoiaGRoZGhAaGRoZC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJmMjAzYjg1ZTUyNTc5MWU3ZmM1ZDdiNWI3OWYzN2Q2MzgxZTRjN2YifQ==','2019-05-20 15:37:50.139514'),('wuak1yqhu7y2iqqvwdbpmqdbuwvq8jpj','NDM5N2U5YTE4OTQ1NDRiNmEzZGEwYjkwNmU3NWY2Yjc1NTM4ODk5ZDp7InVzZXJuYW1lIjoiY2hyaXN0b3BoZXJiZW5zb24xN0BnbWFpbC5jb20iLCJfYXV0aF91c2VyX2lkIjoiMTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjU1Yzg2NzMyMjcyZjM2MmNkZmE4NTI1ZTNhMGZjZGQ4NmNmM2UzMWIifQ==','2019-05-30 23:03:10.565569');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_hall`
--

DROP TABLE IF EXISTS `homs_hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_hall` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `square_meters` varchar(30) NOT NULL,
  `parcking_place` int(11) NOT NULL,
  `descritpion` longtext NOT NULL,
  `price` varchar(255) NOT NULL,
  `payment_terms` varchar(300) NOT NULL,
  `place_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `place_id` (`place_id`),
  KEY `homs_hall_place_i_545741_idx` (`place_id`),
  CONSTRAINT `homs_hall_place_id_a8a9fdc1_fk_homs_place_id` FOREIGN KEY (`place_id`) REFERENCES `homs_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_hall`
--

LOCK TABLES `homs_hall` WRITE;
/*!40000 ALTER TABLE `homs_hall` DISABLE KEYS */;
INSERT INTO `homs_hall` VALUES (1,'700',1,'The FlatList component displays a scrolling list of changing, but similarly structured, data. FlatList works well for long lists of data, where the number of items might change over time. Unlike the more generic ScrollView, the FlatList only renders elements that are currently showing on the screen, not all the elements at once.','1,000,000','per day',15);
/*!40000 ALTER TABLE `homs_hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_joanhostel`
--

DROP TABLE IF EXISTS `homs_joanhostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_joanhostel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `number_of_rooms` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_joanhostel`
--

LOCK TABLES `homs_joanhostel` WRITE;
/*!40000 ALTER TABLE `homs_joanhostel` DISABLE KEYS */;
INSERT INTO `homs_joanhostel` VALUES (1,'changombe','changombe',2),(2,'dit','post',5);
/*!40000 ALTER TABLE `homs_joanhostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_livingplace`
--

DROP TABLE IF EXISTS `homs_livingplace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_livingplace` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rooms` int(11) NOT NULL,
  `master_rooms` int(11) NOT NULL,
  `bathrooms` int(11) NOT NULL,
  `electricity` int(11) NOT NULL,
  `water` int(11) NOT NULL,
  `parcking_place` int(11) NOT NULL,
  `descritpion` longtext NOT NULL,
  `price` varchar(255) NOT NULL,
  `payment_terms` varchar(300) NOT NULL,
  `place_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `place_id` (`place_id`),
  KEY `homs_living_place_i_8ae63e_idx` (`place_id`),
  CONSTRAINT `homs_livingplace_place_id_537d68c2_fk_homs_place_id` FOREIGN KEY (`place_id`) REFERENCES `homs_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_livingplace`
--

LOCK TABLES `homs_livingplace` WRITE;
/*!40000 ALTER TABLE `homs_livingplace` DISABLE KEYS */;
INSERT INTO `homs_livingplace` VALUES (1,4,1,2,1,1,1,'The FlatList component displays a scrolling list of changing, but similarly structured, data. FlatList works well for long lists of data, where the number of items might change over time. Unlike the more generic ScrollView, the FlatList only renders elements that are currently showing on the screen, not all the elements at once.','200,000','Per moth',13);
/*!40000 ALTER TABLE `homs_livingplace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_office`
--

DROP TABLE IF EXISTS `homs_office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_office` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rooms` int(11) NOT NULL,
  `square_meters` varchar(30) NOT NULL,
  `parcking_place` int(11) NOT NULL,
  `descritpion` longtext NOT NULL,
  `price` varchar(255) NOT NULL,
  `payment_terms` varchar(300) NOT NULL,
  `place_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `place_id` (`place_id`),
  KEY `homs_office_place_i_e6887c_idx` (`place_id`),
  CONSTRAINT `homs_office_place_id_67c339a1_fk_homs_place_id` FOREIGN KEY (`place_id`) REFERENCES `homs_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_office`
--

LOCK TABLES `homs_office` WRITE;
/*!40000 ALTER TABLE `homs_office` DISABLE KEYS */;
INSERT INTO `homs_office` VALUES (1,2,'55',1,'The FlatList component displays a scrolling list of changing, but similarly structured, data. FlatList works well for long lists of data, where the number of items might change over time. Unlike the more generic ScrollView, the FlatList only renders elements that are currently showing on the screen, not all the elements at once.','350,000','per month',14);
/*!40000 ALTER TABLE `homs_office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_place`
--

DROP TABLE IF EXISTS `homs_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_place` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `location_description` longtext NOT NULL,
  `place_type` int(11) NOT NULL,
  `uploaded_on` date NOT NULL,
  `status` int(11) NOT NULL,
  `construction_year` varchar(5) NOT NULL,
  `user_id` int(11) NOT NULL,
  `cover_photo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `homs_place_title_2fcde5_idx` (`title`),
  KEY `homs_place_place_t_fcb769_idx` (`place_type`),
  KEY `homs_place_user_id_3c3698_idx` (`user_id`),
  CONSTRAINT `homs_place_user_id_65f9d74d_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_place`
--

LOCK TABLES `homs_place` WRITE;
/*!40000 ALTER TABLE `homs_place` DISABLE KEYS */;
INSERT INTO `homs_place` VALUES (13,'Nyumba ya inapangishwa','Ubungo','You may not be familiar with SwitchNavigator yet. The purpose of SwitchNavigator is to only ever show one screen at a time. By default, it does not handle back actions and it resets routes to their default state when you switch away. This is the exact behavior that we want from the authentication flow: when users sign in, we want to throw away the state of the authentication flow and unmount all of the screens',1,'2019-05-13',2,'2000',19,'images/place/2019/21/13/_E5A3126.jpg'),(14,'Office for rent','Posta','You may not be familiar with SwitchNavigator yet. The purpose of SwitchNavigator is to only ever show one screen at a time. By default, it does not handle back actions and it resets routes to their default state when you switch away. This is the exact behavior that we want from the authentication flow: when users sign in, we want to throw away the state of the authentication flow and unmount all of the screens',3,'2019-05-13',1,'2015',2,'images/place/2019/21/13/_E5A3126.jpg'),(15,'Hall for renting','Tazara','You may not be familiar with SwitchNavigator yet. The purpose of SwitchNavigator is to only ever show one screen at a time. By default, it does not handle back actions and it resets routes to their default state when you switch away. This is the exact behavior that we want from the authentication flow: when users sign in, we want to throw away the state of the authentication flow and unmount all of the screens',4,'2019-05-13',3,'2011',27,'images/place/2019/21/13/_E5A3126.jpg');
/*!40000 ALTER TABLE `homs_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homs_placeimage`
--

DROP TABLE IF EXISTS `homs_placeimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homs_placeimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `place_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `homs_placei_place_i_37fde6_idx` (`place_id`),
  CONSTRAINT `homs_placeimage_place_id_5fdfefe6_fk_homs_place_id` FOREIGN KEY (`place_id`) REFERENCES `homs_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homs_placeimage`
--

LOCK TABLES `homs_placeimage` WRITE;
/*!40000 ALTER TABLE `homs_placeimage` DISABLE KEYS */;
INSERT INTO `homs_placeimage` VALUES (1,13,'images/place/2019/21/13/_E5A3126.jpg');
/*!40000 ALTER TABLE `homs_placeimage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-11  7:24:39
