-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: mls_class_db
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.16.04.2

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
INSERT INTO `jobData` VALUES (1549819411,'Testing iris','Description iris','david.medina@cebib.cl',0,'2019-04-11 14:31:35','2019-04-11 15:08:03','FINISH','INIT JOB','CLASSIFICATION','iris.csv'),(1552975661,'Caesarian data set','Description Demo','david.medina@cebib.cl',0,'2019-04-11 14:33:33','2019-04-11 14:46:12','FINISH','INIT JOB','CLASSIFICATION','caesarian_edit.csv'),(1554836124,'clf','clf','david.medina@cebib.cl',0,'2019-04-09 15:55:24','2019-04-09 15:55:24','FINISH','INIT JOB','CLASSIFICATION','Immunotherapy_edit.csv'),(1554836166,'prediction','prediction','david.medina@cebib.cl',0,'2019-04-09 15:56:06','2019-04-09 15:56:06','FINISH','INIT JOB','PREDICTION','data.csv'),(1555004394,'Testing airfoil data set','Testing airfoil data set','david.medina@cebib.cl',0,'2019-04-11 14:39:54','2019-04-17 19:15:39','PROCESSING','INIT JOB','PREDICTION','airfoil_self_noise.csv'),(1555004469,'Testing electrical grid','Testing electrical grid','david.medina@cebib.cl',0,'2019-04-11 14:41:09','2019-04-17 19:15:41','PROCESSING','INIT JOB','PREDICTION','Data_for_UCI_named.csv'),(1555539299,'A Atribute VHL','A Atribue VHL','david.medina@cebib.cl',0,'2019-04-17 19:14:59','2019-04-17 19:15:44','PROCESSING','INIT JOB','CLASSIFICATION','iris.csv'),(1555539520,'A Atribute VHL','A Group','david.medina@cebib.cl',0,'2019-04-17 19:18:40','2019-04-17 19:19:14','PROCESSING','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1555539762,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:22:42','2019-04-17 19:22:51','PROCESSING','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1555539842,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:24:02','2019-04-17 19:24:39','FINISH','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1555539988,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:26:28','2019-04-17 19:37:43','FINISH','INIT JOB','CLASSIFICATION','B_Attribute.csv'),(1555540830,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:40:30','2019-04-17 19:41:22','FINISH','INIT JOB','CLASSIFICATION','C_Attribute.csv'),(1555540950,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:42:31','2019-04-17 19:42:54','FINISH','INIT JOB','CLASSIFICATION','F_Attribute.csv'),(1555541052,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:44:12','2019-04-17 19:44:38','FINISH','INIT JOB','CLASSIFICATION','H_Attribute.csv'),(1555541125,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:45:25','2019-04-17 19:45:58','FINISH','INIT JOB','CLASSIFICATION','M_Attribute.csv'),(1555541211,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:46:51','2019-04-17 19:46:57','PROCESSING','INIT JOB','CLASSIFICATION','N_Attribute.csv'),(1555541264,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:47:44','2019-04-17 19:48:27','FINISH','INIT JOB','CLASSIFICATION','O_Attribute.csv'),(1555541378,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:49:38','2019-04-17 19:50:21','FINISH','INIT JOB','CLASSIFICATION','P_Attribute.csv'),(1555541489,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:51:29','2019-04-17 19:52:53','FINISH','INIT JOB','CLASSIFICATION','R_Attribute.csv'),(1555541700,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:55:00','2019-04-17 19:55:11','PROCESSING','INIT JOB','CLASSIFICATION','T_Attribute.csv'),(1555541775,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:56:15','2019-04-17 19:56:41','FINISH','INIT JOB','CLASSIFICATION','T_Attribute.csv'),(1555541830,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:57:10','2019-04-17 19:57:34','FINISH','INIT JOB','CLASSIFICATION','U_Attribute.csv'),(1555541932,'123','123','david.medina@cebib.cl',0,'2019-04-17 19:58:52','2019-04-17 19:59:37','FINISH','INIT JOB','CLASSIFICATION','Z_Attribute.csv'),(1555542085,'A Atribute VHL','A Group','david.medina@cebib.cl',0,'2019-04-17 20:01:25','2019-04-18 00:08:53','FINISH','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1555542111,'B Atribute VHL','B Group','david.medina@cebib.cl',0,'2019-04-17 20:01:51','2019-04-17 22:34:01','FINISH','INIT JOB','CLASSIFICATION','B_Attribute.csv'),(1555542132,'C Atribute VHL','C group','david.medina@cebib.cl',0,'2019-04-17 20:02:12','2019-04-22 15:17:49','FINISH','INIT JOB','CLASSIFICATION','C_Attribute.csv'),(1555542157,'F Atribute VHL','F group','david.medina@cebib.cl',0,'2019-04-17 20:02:37','2019-04-17 22:30:30','FINISH','INIT JOB','CLASSIFICATION','F_Attribute.csv'),(1555957247,'Testing full','Testing full','david.medina@cebib.cl',0,'2019-04-22 15:20:47','2019-04-22 15:24:45','FINISH','INIT JOB','CLASSIFICATION','dataCSV.csv'),(1555960466,'Testing VHL','Testing VHL','david.medina@cebib.cl',0,'2019-04-22 16:14:26','2019-04-22 16:15:14','PROCESSING','INIT JOB','CLASSIFICATION','dataCSV.csv'),(1555963157,'A Atribute VHL','A Atribue VHL','david.medina@cebib.cl',0,'2019-04-22 16:59:17','2019-04-22 17:34:42','FINISH','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1555968688,'Testing Full VHL','Testing Full VHL','david.medina@cebib.cl',0,'2019-04-22 18:31:28','2019-04-22 21:42:30','FINISH','INIT JOB','CLASSIFICATION','dataCSV.csv'),(1556376546,'A Atribute VHL','A Atribue VHL','david.medina@cebib.cl',0,'2019-04-27 11:49:06','2019-04-27 12:14:23','FINISH','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1556376569,'B Atribute VHL','B Group','david.medina@cebib.cl',0,'2019-04-27 11:49:29','2019-04-27 12:48:55','FINISH','INIT JOB','CLASSIFICATION','B_Attribute.csv'),(1556376591,'C Atribute VHL','C group','david.medina@cebib.cl',0,'2019-04-27 11:49:51','2019-04-27 12:13:26','FINISH','INIT JOB','CLASSIFICATION','C_Attribute.csv'),(1556376801,'F Atribute VHL','F group','david.medina@cebib.cl',0,'2019-04-27 11:53:21','2019-04-27 12:13:42','FINISH','INIT JOB','CLASSIFICATION','F_Attribute.csv'),(1556380438,'H Group','H group','david.medina@cebib.cl',0,'2019-04-27 12:53:58','2019-04-27 12:56:57','PROCESSING','INIT JOB','CLASSIFICATION','H_Attribute.csv'),(1556380457,'M group','M group','david.medina@cebib.cl',0,'2019-04-27 12:54:17','2019-04-27 13:38:20','FINISH','INIT JOB','CLASSIFICATION','M_Attribute.csv'),(1556380493,'O group','O group','david.medina@cebib.cl',0,'2019-04-27 12:54:53','2019-04-27 13:38:39','FINISH','INIT JOB','CLASSIFICATION','O_Attribute.csv'),(1556380516,'P group','P group','david.medina@cebib.cl',0,'2019-04-27 12:55:16','2019-04-27 13:37:53','FINISH','INIT JOB','CLASSIFICATION','P_Attribute.csv'),(1556827080,'B Atribute VHL','B Group','david.medina@cebib.cl',0,'2019-05-02 16:58:00','2019-05-02 18:21:16','FINISH','INIT JOB','CLASSIFICATION','B_Attribute.csv'),(1556917169,'A Atribute VHL','A Atribue VHL','david.medina@cebib.cl',0,'2019-05-03 17:59:29','2019-05-03 20:36:30','FINISH','INIT JOB','CLASSIFICATION','A_Attribute.csv'),(1556917506,'B Atribute VHL','B Group','david.medina@cebib.cl',0,'2019-05-03 18:05:06','2019-05-03 19:36:06','FINISH','INIT JOB','CLASSIFICATION','B_Attribute.csv'),(1556917529,'C Atribute VHL','C group','david.medina@cebib.cl',0,'2019-05-03 18:05:29','2019-05-03 19:26:49','FINISH','INIT JOB','CLASSIFICATION','C_Attribute.csv'),(1556917552,'C Atribute VHL','C group','david.medina@cebib.cl',0,'2019-05-03 18:05:52','2019-05-03 19:36:26','FINISH','INIT JOB','CLASSIFICATION','F_Attribute.csv');
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

-- Dump completed on 2019-05-04 13:24:18
