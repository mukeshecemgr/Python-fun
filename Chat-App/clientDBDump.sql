-- MySQL dump 10.13  Distrib 8.0.15, for osx10.13 (x86_64)
--
-- Host: localhost    Database: ClientDB
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `7091728998`
--

DROP TABLE IF EXISTS `7091728998`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `7091728998` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) DEFAULT NULL,
  `contacts` varchar(16) NOT NULL,
  `status` enum('Online','Offline') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `7091728998`
--

LOCK TABLES `7091728998` WRITE;
/*!40000 ALTER TABLE `7091728998` DISABLE KEYS */;
/*!40000 ALTER TABLE `7091728998` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_7091728998`
--

DROP TABLE IF EXISTS `usr_7091728998`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `usr_7091728998` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(128) DEFAULT NULL,
  `contacts` varchar(16) NOT NULL,
  `status` enum('Online','Offline') NOT NULL,
  `reply_status` enum('no','yes') NOT NULL,
  `message` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_7091728998`
--

LOCK TABLES `usr_7091728998` WRITE;
/*!40000 ALTER TABLE `usr_7091728998` DISABLE KEYS */;
INSERT INTO `usr_7091728998` VALUES (1,'Sun Dec  6 11:21:45 2020','9884465581','Online','no','Hi Mukesh'),(2,'Sun Dec  6 11:22:10 2020','9884465582','Online','no','Hello Mukesh'),(3,'Sun Dec  6 11:22:36 2020','9884465583','Online','no','jddjh jdsjd'),(4,'Sun Dec  6 11:22:46 2020','9884465584','Online','no','yri ndhf shye hl'),(5,'Sun Dec  6 11:22:54 2020','9884465584','Online','no','hdhdhhd nhsh'),(6,'Sun Dec  6 11:23:18 2020','9884465581','Online','no','google'),(7,'Sun Dec  6 11:23:24 2020','9884465584','Online','no','Bingoooo'),(8,'Sun Dec  6 11:23:30 2020','9884465582','Online','no','Yahooooo'),(9,'Sun Dec  6 11:23:35 2020','9884465583','Online','no','Stop'),(10,'Sun Dec  6 11:23:39 2020','9884465584','Online','no','Bye'),(11,'Sun Dec  6 11:23:48 2020','9884465584','Online','no','Good Morning'),(12,'Sun Dec  6 11:23:52 2020','9884465584','Online','no','good'),(13,'Sun Dec  6 11:23:55 2020','9884465584','Online','no','ggfh');
/*!40000 ALTER TABLE `usr_7091728998` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-06 18:35:41
