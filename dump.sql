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
-- Table structure for table `feature`
--

DROP TABLE IF EXISTS `feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feature` (
  `idfeature` int(11) NOT NULL AUTO_INCREMENT,
  `nameFeature` varchar(45) NOT NULL,
  `kind` varchar(45) NOT NULL,
  `dataSet` int(11) NOT NULL,
  PRIMARY KEY (`idfeature`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature`
--

LOCK TABLES `feature` WRITE;
/*!40000 ALTER TABLE `feature` DISABLE KEYS */;
INSERT INTO `feature` VALUES (1,'AAWT','CATEGORICAL',1558867458),(2,'Pos','CONTINUE',1558867458),(3,'AAMT','CATEGORICAL',1558867458),(4,'ChainID','CATEGORICAL',1558867458),(5,'WT_SSE','CATEGORICAL',1558867458),(6,'WT_RSA','CONTINUE',1558867458),(7,'WT_DEPTH','CONTINUE',1558867458),(8,'WT_OSP','CONTINUE',1558867458),(9,'MT_SSE','CATEGORICAL',1558867458),(10,'MT_RSA','CONTINUE',1558867458),(11,'MT_DEPTH','CONTINUE',1558867458),(12,'MT_OSP','CONTINUE',1558867458),(13,'DDG','CONTINUE',1558867458),(14,'Outcome','CATEGORICAL',1558867458),(15,'AAWT','CATEGORICAL',1558867802),(16,'Pos','CONTINUE',1558867802),(17,'AAMT','CATEGORICAL',1558867802),(18,'ChainID','CATEGORICAL',1558867802),(19,'WT_SSE','CATEGORICAL',1558867802),(20,'WT_RSA','CONTINUE',1558867802),(21,'WT_DEPTH','CONTINUE',1558867802),(22,'WT_OSP','CONTINUE',1558867802),(23,'MT_SSE','CATEGORICAL',1558867802),(24,'MT_RSA','CONTINUE',1558867802),(25,'MT_DEPTH','CONTINUE',1558867802),(26,'MT_OSP','CONTINUE',1558867802),(27,'DDG','CONTINUE',1558867802),(28,'Outcome','CATEGORICAL',1558867802),(29,'AAWT','CATEGORICAL',1558870802),(30,'Pos','CONTINUE',1558870802),(31,'AAMT','CATEGORICAL',1558870802),(32,'ChainID','CATEGORICAL',1558870802),(33,'WT_SSE','CATEGORICAL',1558870802),(34,'WT_RSA','CONTINUE',1558870802),(35,'WT_DEPTH','CONTINUE',1558870802),(36,'WT_OSP','CONTINUE',1558870802),(37,'MT_SSE','CATEGORICAL',1558870802),(38,'MT_RSA','CONTINUE',1558870802),(39,'MT_DEPTH','CONTINUE',1558870802),(40,'MT_OSP','CONTINUE',1558870802),(41,'DDG','CONTINUE',1558870802),(42,'Response','CONTINUE',1558870802),(43,'AAWT','CATEGORICAL',1558885359),(44,'Pos','CONTINUE',1558885359),(45,'AAMT','CATEGORICAL',1558885359),(46,'ChainID','CATEGORICAL',1558885359),(47,'WT_SSE','CATEGORICAL',1558885359),(48,'WT_RSA','CONTINUE',1558885359),(49,'WT_DEPTH','CONTINUE',1558885359),(50,'WT_OSP','CONTINUE',1558885359),(51,'MT_SSE','CATEGORICAL',1558885359),(52,'MT_RSA','CONTINUE',1558885359),(53,'MT_DEPTH','CONTINUE',1558885359),(54,'MT_OSP','CONTINUE',1558885359),(55,'DDG','CONTINUE',1558885359),(56,'Outcome','CATEGORICAL',1558885359),(57,'AAWT','CATEGORICAL',1558889033),(58,'Pos','CONTINUE',1558889033),(59,'AAMT','CATEGORICAL',1558889033),(60,'ChainID','CATEGORICAL',1558889033),(61,'WT_SSE','CATEGORICAL',1558889033),(62,'WT_RSA','CONTINUE',1558889033),(63,'WT_DEPTH','CONTINUE',1558889033),(64,'WT_OSP','CONTINUE',1558889033),(65,'MT_SSE','CATEGORICAL',1558889033),(66,'MT_RSA','CONTINUE',1558889033),(67,'MT_DEPTH','CONTINUE',1558889033),(68,'MT_OSP','CONTINUE',1558889033),(69,'DDG','CONTINUE',1558889033),(70,'Response','CONTINUE',1558889033),(71,'AAWT','CATEGORICAL',1558976670),(72,'Pos','CONTINUE',1558976670),(73,'AAMT','CATEGORICAL',1558976670),(74,'WT_SSE','CATEGORICAL',1558976670),(75,'WT_RSA','CONTINUE',1558976670),(76,'WT_DEPTH','CONTINUE',1558976670),(77,'WT_OSP','CONTINUE',1558976670),(78,'MT_SSE','CATEGORICAL',1558976670),(79,'MT_RSA','CONTINUE',1558976670),(80,'MT_DEPTH','CONTINUE',1558976670),(81,'MT_OSP','CONTINUE',1558976670),(82,'DDG','CONTINUE',1558976670),(83,'Outcome','CATEGORICAL',1558976670),(84,'AAWT','CATEGORICAL',1558976870),(85,'Pos','CONTINUE',1558976870),(86,'AAMT','CATEGORICAL',1558976870),(87,'WT_SSE','CATEGORICAL',1558976870),(88,'WT_RSA','CONTINUE',1558976870),(89,'WT_DEPTH','CONTINUE',1558976870),(90,'WT_OSP','CONTINUE',1558976870),(91,'MT_SSE','CATEGORICAL',1558976870),(92,'MT_RSA','CONTINUE',1558976870),(93,'MT_DEPTH','CONTINUE',1558976870),(94,'MT_OSP','CONTINUE',1558976870),(95,'DDG','CONTINUE',1558976870),(96,'Outcome','CATEGORICAL',1558976870),(97,'AAWT','CATEGORICAL',1558976925),(98,'Pos','CONTINUE',1558976925),(99,'AAMT','CATEGORICAL',1558976925),(100,'WT_SSE','CATEGORICAL',1558976925),(101,'WT_RSA','CONTINUE',1558976925),(102,'WT_DEPTH','CONTINUE',1558976925),(103,'WT_OSP','CONTINUE',1558976925),(104,'MT_SSE','CATEGORICAL',1558976925),(105,'MT_RSA','CONTINUE',1558976925),(106,'MT_DEPTH','CONTINUE',1558976925),(107,'MT_OSP','CONTINUE',1558976925),(108,'DDG','CONTINUE',1558976925),(109,'Outcome','CATEGORICAL',1558976925),(110,'AAWT','CATEGORICAL',1558976966),(111,'Pos','CONTINUE',1558976966),(112,'AAMT','CATEGORICAL',1558976966),(113,'WT_SSE','CATEGORICAL',1558976966),(114,'WT_RSA','CONTINUE',1558976966),(115,'WT_DEPTH','CONTINUE',1558976966),(116,'WT_OSP','CONTINUE',1558976966),(117,'MT_SSE','CATEGORICAL',1558976966),(118,'MT_RSA','CONTINUE',1558976966),(119,'MT_DEPTH','CONTINUE',1558976966),(120,'MT_OSP','CONTINUE',1558976966),(121,'DDG','CONTINUE',1558976966),(122,'Outcome','CATEGORICAL',1558976966),(123,'AAWT','CATEGORICAL',1558977013),(124,'Pos','CONTINUE',1558977013),(125,'AAMT','CATEGORICAL',1558977013),(126,'WT_SSE','CATEGORICAL',1558977013),(127,'WT_RSA','CONTINUE',1558977013),(128,'WT_DEPTH','CONTINUE',1558977013),(129,'WT_OSP','CONTINUE',1558977013),(130,'MT_SSE','CATEGORICAL',1558977013),(131,'MT_RSA','CONTINUE',1558977013),(132,'MT_DEPTH','CONTINUE',1558977013),(133,'MT_OSP','CONTINUE',1558977013),(134,'DDG','CONTINUE',1558977013),(135,'Outcome','CATEGORICAL',1558977013),(136,'AAWT','CATEGORICAL',1558977060),(137,'Pos','CONTINUE',1558977060),(138,'AAMT','CATEGORICAL',1558977060),(139,'WT_SSE','CATEGORICAL',1558977060),(140,'WT_RSA ','CONTINUE',1558977060),(141,'WT_DEPTH','CONTINUE',1558977060),(142,'WT_OSP','CONTINUE',1558977060),(143,'MT_SSE','CATEGORICAL',1558977060),(144,'MT_RSA','CONTINUE',1558977060),(145,'MT_DEPTH','CONTINUE',1558977060),(146,'MT_OSP','CONTINUE',1558977060),(147,'DDG','CONTINUE',1558977060),(148,'Outcome','CATEGORICAL',1558977060),(149,'AAWT','CATEGORICAL',1559055159),(150,'Pos','CONTINUE',1559055159),(151,'AAMT','CATEGORICAL',1559055159),(152,'WT_SSE','CATEGORICAL',1559055159),(153,'WT_RSA','CONTINUE',1559055159),(154,'WT_DEPTH','CONTINUE',1559055159),(155,'WT_OSP','CONTINUE',1559055159),(156,'MT_SSE','CATEGORICAL',1559055159),(157,'MT_RSA','CONTINUE',1559055159),(158,'MT_DEPTH','CONTINUE',1559055159),(159,'MT_OSP','CONTINUE',1559055159),(160,'Response','CONTINUE',1559055159),(161,'AAWT','CATEGORICAL',1559055230),(162,'Pos','CONTINUE',1559055230),(163,'AAMT','CATEGORICAL',1559055230),(164,'WT_SSE','CATEGORICAL',1559055230),(165,'WT_RSA','CONTINUE',1559055230),(166,'WT_DEPTH','CONTINUE',1559055230),(167,'WT_OSP','CONTINUE',1559055230),(168,'MT_SSE','CATEGORICAL',1559055230),(169,'MT_RSA','CONTINUE',1559055230),(170,'MT_DEPTH','CONTINUE',1559055230),(171,'MT_OSP','CONTINUE',1559055230),(172,'Response','CONTINUE',1559055230),(173,'AAWT','CATEGORICAL',1559055284),(174,'Pos','CONTINUE',1559055284),(175,'AAMT','CATEGORICAL',1559055284),(176,'WT_SSE','CATEGORICAL',1559055284),(177,'WT_RSA','CONTINUE',1559055284),(178,'WT_DEPTH','CONTINUE',1559055284),(179,'WT_OSP','CONTINUE',1559055284),(180,'MT_SSE','CATEGORICAL',1559055284),(181,'MT_RSA','CONTINUE',1559055284),(182,'MT_DEPTH','CONTINUE',1559055284),(183,'MT_OSP','CONTINUE',1559055284),(184,'Response','CONTINUE',1559055284),(185,'AAWT','CATEGORICAL',1559055347),(186,'Pos','CONTINUE',1559055347),(187,'AAMT','CATEGORICAL',1559055347),(188,'WT_SSE','CATEGORICAL',1559055347),(189,'WT_RSA','CONTINUE',1559055347),(190,'WT_DEPTH','CONTINUE',1559055347),(191,'WT_OSP','CONTINUE',1559055347),(192,'MT_SSE','CATEGORICAL',1559055347),(193,'MT_RSA','CONTINUE',1559055347),(194,'MT_DEPTH','CONTINUE',1559055347),(195,'MT_OSP','CONTINUE',1559055347),(196,'Response','CONTINUE',1559055347),(197,'AAWT','CATEGORICAL',1559055400),(198,'Pos','CONTINUE',1559055400),(199,'AAMT','CATEGORICAL',1559055400),(200,'WT_SSE','CATEGORICAL',1559055400),(201,'WT_RSA ','CONTINUE',1559055400),(202,'WT_DEPTH','CONTINUE',1559055400),(203,'WT_OSP','CONTINUE',1559055400),(204,'MT_SSE','CATEGORICAL',1559055400),(205,'MT_RSA','CONTINUE',1559055400),(206,'MT_DEPTH','CONTINUE',1559055400),(207,'MT_OSP','CONTINUE',1559055400),(208,'Response','CONTINUE',1559055400),(209,'AAWT','CATEGORICAL',1559055505),(210,'Pos','CONTINUE',1559055505),(211,'AAMT','CATEGORICAL',1559055505),(212,'WT_SSE','CATEGORICAL',1559055505),(213,'WT_RSA ','CONTINUE',1559055505),(214,'WT_DEPTH','CONTINUE',1559055505),(215,'WT_OSP','CONTINUE',1559055505),(216,'MT_SSE','CATEGORICAL',1559055505),(217,'MT_RSA','CONTINUE',1559055505),(218,'MT_DEPTH','CONTINUE',1559055505),(219,'MT_OSP','CONTINUE',1559055505),(220,'Response','CONTINUE',1559055505),(221,'AAWT','CATEGORICAL',1559055602),(222,'Pos','CONTINUE',1559055602),(223,'AAMT','CATEGORICAL',1559055602),(224,'WT_SSE','CATEGORICAL',1559055602),(225,'WT_RSA ','CONTINUE',1559055602),(226,'WT_DEPTH','CONTINUE',1559055602),(227,'WT_OSP','CONTINUE',1559055602),(228,'MT_SSE','CATEGORICAL',1559055602),(229,'MT_RSA','CONTINUE',1559055602),(230,'MT_DEPTH','CONTINUE',1559055602),(231,'MT_OSP','CONTINUE',1559055602),(232,'Response','CONTINUE',1559055602),(233,'AAWT','CATEGORICAL',1559055665),(234,'Pos','CONTINUE',1559055665),(235,'AAMT','CATEGORICAL',1559055665),(236,'WT_SSE','CATEGORICAL',1559055665),(237,'WT_RSA ','CONTINUE',1559055665),(238,'WT_DEPTH','CONTINUE',1559055665),(239,'WT_OSP','CONTINUE',1559055665),(240,'MT_SSE','CATEGORICAL',1559055665),(241,'MT_RSA','CONTINUE',1559055665),(242,'MT_DEPTH','CONTINUE',1559055665),(243,'MT_OSP','CONTINUE',1559055665),(244,'Response','CONTINUE',1559055665),(245,'X1transactiondate','CONTINUE',1559131307),(246,'X2houseage','CONTINUE',1559131307),(247,'X3distancetothenearestMRTstation','CONTINUE',1559131307),(248,'X4numberofconveniencestores','CONTINUE',1559131307),(249,'X5latitude','CONTINUE',1559131307),(250,'X6longitude','CONTINUE',1559131307),(251,'Yhousepriceofunitarea','CONTINUE',1559131307);
/*!40000 ALTER TABLE `feature` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `jobData` VALUES (1558867458,'Testing 1A22 clf','Testing 1A22 clf','david.medina@cebib.cl',0,'2019-05-26 06:44:18','2019-05-26 06:44:18','INIT','INIT JOB','CLASSIFICATION','1A22_SDM_clf.csv'),(1558867543,'Testing 1A22 clf','Testing 1A22 clf','david.medina@cebib.cl',0,'2019-05-26 06:45:43','2019-05-26 06:45:43','INIT','INIT JOB','CLASSIFICATION','1A22_SDM_clf.csv'),(1558867751,'Testing 1A22 clf','Testing 1A22 clf','david.medina@cebib.cl',0,'2019-05-26 06:49:11','2019-05-26 06:49:11','INIT','INIT JOB','CLASSIFICATION','1A22_SDM_clf.csv'),(1558867802,'Testing 1A22 clf','Testing 1A22 clf','david.medina@cebib.cl',0,'2019-05-26 06:50:02','2019-05-26 06:50:02','INIT','INIT JOB','CLASSIFICATION','1A22_SDM_clf.csv'),(1558870802,'Testing 1A22 rgx','Testing 1A22 rgx','david.medina@cebib.cl',0,'2019-05-26 09:15:28','2019-05-27 13:17:11','PROCESSING','INIT JOB','PREDICTION','1A22_SDM.csv'),(1558885359,'Testing 1A22 clf','Testing 1A22 clf','david.medina@cebib.cl',0,'2019-05-26 12:07:39','2019-05-27 13:17:14','PROCESSING','INIT JOB','CLASSIFICATION','1A22_SDM_clf.csv'),(1558889033,'Testing 1A22','Testing 1A22','david.medina@cebib.cl',0,'2019-05-26 12:44:01','2019-05-28 02:25:07','FINISH','INIT JOB','PREDICTION','1A22_SDM.csv'),(1558976670,'1A22 clf','1A22 clf','david.medina@cebib.cl',0,'2019-05-27 13:04:30','2019-05-27 13:04:30','INIT','INIT JOB','CLASSIFICATION','1A22Clf.csv'),(1558976870,'1A22 clf','1A22 clf','david.medina@cebib.cl',0,'2019-05-27 13:08:06','2019-05-27 16:48:07','FINISH','INIT JOB','CLASSIFICATION','1A22Clf.csv'),(1558976925,'1CH0 clf','1CHO clf','david.medina@cebib.cl',0,'2019-05-27 13:08:56','2019-05-27 18:03:46','FINISH','INIT JOB','CLASSIFICATION','1CHOClf.csv'),(1558976966,'1DKT clf','1DKT clf','david.medina@cebib.cl',0,'2019-05-27 13:09:42','2019-05-27 16:48:28','FINISH','INIT JOB','CLASSIFICATION','1DKTClf.csv'),(1558977013,'1FJK CLF','1FKJ CLF','david.medina@cebib.cl',0,'2019-05-27 13:10:30','2019-05-27 18:53:10','FINISH','INIT JOB','CLASSIFICATION','1FKJClf.csv'),(1558977060,'1FTG CLF','1FTG CLF','david.medina@cebib.cl',0,'2019-05-27 13:11:10','2019-05-27 18:53:00','FINISH','INIT JOB','CLASSIFICATION','1FTGClf.csv'),(1559055043,'1CH0','1CHO regression','david.medina@cebib.cl',0,'2019-05-28 10:50:43','2019-05-28 10:50:43','INIT','INIT JOB','PREDICTION','1FTGClf.csv'),(1559055159,'1CH0','1CHO regression','david.medina@cebib.cl',0,'2019-05-28 10:52:39','2019-05-28 10:52:39','INIT','INIT JOB','PREDICTION','1CHORex.csv'),(1559055230,'1CH0','1CHO regression','david.medina@cebib.cl',0,'2019-05-28 10:54:10','2019-05-28 11:14:46','FINISH','INIT JOB','PREDICTION','1CHORex.csv'),(1559055284,'1DKT','1DKT','david.medina@cebib.cl',0,'2019-05-28 10:54:52','2019-05-28 11:11:51','FINISH','INIT JOB','PREDICTION','1DKTRex.csv'),(1559055347,'1FKJ','1FKJ','david.medina@cebib.cl',0,'2019-05-28 10:56:17','2019-05-28 11:14:39','FINISH','INIT JOB','PREDICTION','1FKJRex.csv'),(1559055400,'1FTG','1FTG','david.medina@cebib.cl',0,'2019-05-28 10:56:40','2019-05-28 10:56:40','INIT','INIT JOB','PREDICTION','1FTGRex.csv'),(1559055505,'1FTG','1FTG','david.medina@cebib.cl',0,'2019-05-28 10:58:25','2019-05-28 10:58:25','INIT','INIT JOB','PREDICTION','1FTGRex.csv'),(1559055602,'1FTG','1FTG','david.medina@cebib.cl',0,'2019-05-28 11:00:02','2019-05-28 11:00:02','INIT','INIT JOB','PREDICTION','1FTGRex.csv'),(1559055665,'1FTG','1FTG','david.medina@cebib.cl',0,'2019-05-28 11:01:13','2019-05-28 11:14:26','FINISH','INIT JOB','PREDICTION','1FTGRex.csv'),(1559131122,'ElectricalGrid','ElectricalGrid','david.medina@cebib.cl',0,'2019-05-29 07:58:42','2019-05-29 07:58:42','INIT','INIT JOB','PREDICTION','1FTGRex.csv'),(1559131161,'ElectricalGrid','ElectricalGrid','david.medina@cebib.cl',0,'2019-05-29 07:59:21','2019-05-29 07:59:21','INIT','INIT JOB','PREDICTION','1FTGRex.csv'),(1559131307,'ElectricalGrid','ElectricalGrid','david.medina@cebib.cl',0,'2019-05-29 08:01:47','2019-05-29 08:01:47','INIT','INIT JOB','PREDICTION','data.csv'),(1559131361,'ElectricalGrid','ElectricalGrid','david.medina@cebib.cl',0,'2019-05-29 08:02:41','2019-05-29 08:02:41','INIT','INIT JOB','PREDICTION','data.csv');
/*!40000 ALTER TABLE `jobData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `response`
--

DROP TABLE IF EXISTS `response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `response` (
  `idResponse` int(11) NOT NULL AUTO_INCREMENT,
  `nameFeature` varchar(500) NOT NULL,
  `dataSet` int(11) NOT NULL,
  `removeElements` int(11) NOT NULL,
  `tipo` int(11) NOT NULL,
  PRIMARY KEY (`idResponse`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `response`
--

LOCK TABLES `response` WRITE;
/*!40000 ALTER TABLE `response` DISABLE KEYS */;
INSERT INTO `response` VALUES (2,'DDG',1558870802,2,2),(3,'Outcome',1558885359,2,1),(4,'Outcome',1558885359,1,1),(5,'Response',1558889033,1,2),(6,'Outcome',1558976870,1,1),(7,'Outcome',1558976925,1,1),(8,'Outcome',1558976966,1,1),(9,'Outcome',1558977013,1,1),(10,'Outcome',1558977060,1,1),(11,'Response',1559055230,1,2),(12,'Response',1559055284,1,2),(13,'Response',1559055347,1,2),(14,'Response',1559055665,1,2);
/*!40000 ALTER TABLE `response` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-04  9:20:38
