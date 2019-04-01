-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: mls_class_db
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jobData`
--

DROP TABLE IF EXISTS `jobData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobData` (
  `idjobData` int(11) NOT NULL,
  `nameJob` varchar(450) NOT NULL,
  `descriptionJob` varchar(4500) NOT NULL,
  `mailUser` varchar(45) NOT NULL,
  `iterations` int(11) NOT NULL,
  `dateInit` datetime NOT NULL,
  `dateFinish` datetime DEFAULT NULL,
  `statusJob` varchar(45) NOT NULL,
  `commentJob` varchar(4500) NOT NULL,
  `kind` varchar(45) NOT NULL,
  `nameDoc` varchar(450) NOT NULL,
  PRIMARY KEY (`idjobData`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobData`
--

LOCK TABLES `jobData` WRITE;
/*!40000 ALTER TABLE `jobData` DISABLE KEYS */;
INSERT INTO `jobData` VALUES (1553388562,'New Job Regression','Testing regression Job','david.medina@cebib.cl',0,'2019-03-23 21:49:22','2019-03-24 09:04:52','FINISH','INIT JOB','PREDICTION','data.csv'),(1553388608,'New Job classification','Description Job Class','david.medina@cebib.cl',0,'2019-03-23 21:50:08','2019-03-24 09:49:13','FINISH','INIT JOB','CLASSIFICATION','audit_risk_edit.csv'),(1553716723,'Testing job','Testing predict ','david.medina@cebib.cl',0,'2019-03-27 16:58:43','2019-03-27 16:58:43','PROCESSING','INIT JOB','CLASSIFICATION','Immunotherapy_edit.csv'),(1553799242,'123123','123123','david.medina@cebib.cl',0,'2019-03-28 15:54:02','2019-03-28 15:54:02','START','INIT JOB','CLASSIFICATION','caesarian_edit.csv');
/*!40000 ALTER TABLE `jobData` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-01  6:34:06
