-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: Poke
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `pokes`
--

DROP TABLE IF EXISTS `pokes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pokes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `friend_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pokes_users1_idx` (`user_id`),
  CONSTRAINT `fk_pokes_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokes`
--

LOCK TABLES `pokes` WRITE;
/*!40000 ALTER TABLE `pokes` DISABLE KEYS */;
INSERT INTO `pokes` VALUES (1,2,1,'2016-06-24 10:39:22'),(2,3,1,'2016-06-24 10:39:28'),(3,4,1,'2016-06-24 10:39:32'),(4,1,2,'2016-06-24 10:39:39'),(5,3,2,'2016-06-24 10:39:48'),(6,4,2,'2016-06-24 10:39:51'),(7,1,3,'2016-06-24 10:40:36'),(8,2,3,'2016-06-24 10:40:42'),(9,1,4,'2016-06-24 10:40:54'),(10,2,1,'2016-06-24 11:56:22'),(11,2,1,'2016-06-24 11:56:49'),(12,2,1,'2016-06-24 11:56:53'),(13,2,1,'2016-06-24 11:58:18'),(14,2,1,'2016-06-24 11:58:55'),(15,2,1,'2016-06-24 12:44:27');
/*!40000 ALTER TABLE `pokes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `alias` varchar(150) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Bruce Wayne','Batman','email1@gmail.com','$2b$12$2zn90WyCz6gWMFDzFDJ5ru.RcLyUU3JDLC8/3CNQG2kDrTcdvxvLq','1985-12-25','2016-06-24 10:34:20'),(2,'Leia Organa','Princess','email2@gmail.com','$2b$12$AWVLSxg/.3O0L/1hURgaG.jUnkHtGgjwSdzfJEwkhs9qjYeTkX7eS','1980-01-25','2016-06-24 10:34:47'),(3,'Luke Skywalker','Jedi','email3@gmail.com','$2b$12$nNVHXSKQSjgryCgJ0jSc7uIK0W6em1NvoP0JfHnQ5sdK7M1yMZu/y','2011-11-25','2016-06-24 10:35:18'),(4,'Chuck Norris','Immortal','email4@gmail.com','$2b$12$i4JruUnOPXyk9cybZpeDVurzIlQ1wYRf9uzTeyu0Ke0IbJ9naOYCy','1900-01-01','2016-06-24 10:35:57');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-24 13:26:59
