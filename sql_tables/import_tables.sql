CREATE DATABASE  IF NOT EXISTS `hearts_contents` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hearts_contents`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hearts_contents
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` text,
  `user_id` int NOT NULL,
  `content_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_content1_idx` (`content_id`),
  CONSTRAINT `fk_comments_content1` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`),
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'Shenanigans! All of those Digimon you listed is your own! Also, Gabumon would NOT be at the bottom!',3,2,'2023-10-30 23:34:21','2023-10-30 23:34:21'),(2,'Such a critic, sheesh... I did put Gabumon in the list, didn\'t I?',2,2,'2023-10-30 23:36:14','2023-10-30 23:36:14'),(3,'Luckily, I can tell the difference between Birdramon and Saberdramon. Also apparently Mail Birdramon is related to her? It\'s weird.',4,4,'2023-10-30 23:46:08','2023-10-30 23:46:08'),(4,'Great list, Tai!',4,2,'2023-10-30 23:46:50','2023-10-30 23:46:50'),(5,'Deep.',4,1,'2023-10-30 23:48:59','2023-10-30 23:48:59'),(6,'Matt is right, it\'s a bit too biased. Why just your own? There\'s plenty of Digimon of different attributes, levels, and fields. I probably could put my own at the top, but I don\'t want to avoid mentioning some obscure ones that I thought was neat...',5,2,'2023-10-30 23:53:23','2023-10-30 23:53:23');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `content` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `body` text,
  `author_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_content_users_idx` (`author_id`),
  CONSTRAINT `fk_content_users` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
INSERT INTO `content` VALUES (1,'Mysteries of Life','Have you always wondered what they are?','Well, I can\'t really say I know what is the mysteries of life, but I think it\'s a good question. If one would ask the principals of the question, then maybe the person would know what it means. But I know that\'s just something to speak of in theory, so I don\'t really know if that would mean much. But there\'s someone I know who probably give me a hint, but I hadn\'t seen him in years, and it\'s been so long, that I don\'t even know if he\'s alive. But then again, I don\'t really know who is alive, and I\'m not even sure if I\'m alive myself. Maybe life is a mystery to everyone, but wait a minute, that\'s the question.\r\n<br><br>Anyways, maybe the mysteries of life is something that everyone can interpret, but I think that probably wouldn\'t do. I wonder what they could be, but I guess I\'ll keep rambling until I figure out what it is. But I don\'t know, that seems a bit too stupid. Anyways, I think that\'s probably enough text from me. Maybe I\'ll write more of it in some sort of random novel project. Why am I still typing out this nonsense? I thought I hate writing. But why do I want to write novels? Good question. And I\'m still going typing this. I wonder what\'s for dinner. Did I ever say that I like eating curry? Oh and spaghetti with meatballs are also really good. I just had the most delicious curry today, though I think nearly every curry I had is rather splendid.',1,'2023-10-30 23:24:55','2023-10-30 23:25:17'),(2,'My Top 10 Favorite Digimon','Yeah! I like Digimon!','Hi, I\'m Tai, and here\'s my list of favorite Digimon.</p>\r\n<ol style=\"margin-left: 40px; margin-top: 10px; margin-bottom: 10px;\">\r\n<li>Gabumon</li>\r\n<li>Omegamon: Merciful Mode</li>\r\n<li>Blitz Greymon</li>\r\n<li>Botamon</li>\r\n<li>Metal Greymon</li>\r\n<li>Omegamon</li>\r\n<li>Koromon</li>\r\n<li>War Greymon</li>\r\n<li>Greymon</li>\r\n<li>Agumon</li>\r\n</ol>\r\n<p>And there, that\'s all of my top 10 favorites.',2,'2023-10-30 23:30:11','2023-10-30 23:31:21'),(3,'Butterfly is Overrated TBH','It\'s just my opinion, but...','TBH I think the theme song is a bit overrated. I know it\'s a classic, and I had been listening to it since I started working with Tai. But I feel like I rather listen to something else! It\'s getting quite tiring for me to listen to. I rather listen to Faction, as I think it\'s far more lit.',3,'2023-10-30 23:42:00','2023-10-30 23:42:00'),(4,'Can anyone tell the difference?','I can\'t tell the difference between a Garurumon and Gururumon.','It\'s kind of embarrassing, since my partner is Garurumon. He does insist there\'s a difference, but I really have a hard time telling whose who. I\'m sorry Gabumon.',3,'2023-10-30 23:44:34','2023-10-30 23:44:34'),(5,'Did you know?','There\'s something wack about time.','You know how there\'s Daylight Savings Time? Annoying isn\'t it? But did you know Arizona does not DST for some unexplained reason?',6,'2023-11-06 19:23:49','2023-11-06 19:23:49');
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `content_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_likes_users1_idx` (`user_id`),
  KEY `fk_likes_content1_idx` (`content_id`),
  CONSTRAINT `fk_likes_content1` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`),
  CONSTRAINT `fk_likes_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (1,1,2,'2023-10-30 23:38:37','2023-10-30 23:38:37'),(2,3,1,'2023-10-30 23:42:38','2023-10-30 23:42:38'),(3,4,2,'2023-10-30 23:46:33','2023-10-30 23:46:33'),(4,5,2,'2023-10-30 23:53:58','2023-10-30 23:53:58');
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kari','Kamiya','tailmon@gmail.com','$2b$12$ZnQVdFMv1/7LDC4TWR5BEuSG3wxWPOKpD8PGtIth3xjkujJainySC','2023-10-30 23:18:58','2023-10-30 23:18:58'),(2,'Taichi','Kamiya','agumon@gmail.com','$2b$12$ZnQVdFMv1/7LDC4TWR5BEuSG3wxWPOKpD8PGtIth3xjkujJainySC','2023-10-30 23:26:42','2023-10-30 23:26:42'),(3,'Matt','Ishida','gabumon@gmail.com','$2b$12$RjkLvFETNBZSxE9HLNcolu/hMN4qzwcVzcjIexhJcvt0ZnFdvUI4G','2023-10-30 23:33:16','2023-10-30 23:33:16'),(4,'Sora','Takenouchi','piyomon@gmail.com','$2b$12$FaBzGe7Uq5orvL68cAzpY.FZF/kN/SZo92I8fSv99xrE2u24YqY2q','2023-10-30 23:45:25','2023-10-30 23:45:25'),(5,'Koushiro','\'Izzy\' Izumi','tentomon@gmail.com','$2b$12$zW7cuEE0trlX3ly7.lnS4uBQ1TjHfVuzD0/yy4Pd1jm3FJ7oj6Ofy','2023-10-30 23:50:59','2023-10-30 23:50:59'),(6,'Zachary','Tabikh','leafyseadraco@gmail.com','$2b$12$ZI/QjP8Y1PR19kwWBTB2eelAfZ1Gxly2h0b3TQDc5OSj0qBy4nJ52','2023-11-05 16:36:58','2023-11-05 16:36:58');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `views`
--

DROP TABLE IF EXISTS `views`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `views` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_views_content1_idx` (`content_id`),
  CONSTRAINT `fk_views_content1` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `views`
--

LOCK TABLES `views` WRITE;
/*!40000 ALTER TABLE `views` DISABLE KEYS */;
INSERT INTO `views` VALUES (1,2,'2023-10-30 23:33:18','2023-10-30 23:33:18'),(2,2,'2023-10-30 23:34:21','2023-10-30 23:34:21'),(3,2,'2023-10-30 23:38:35','2023-10-30 23:38:35'),(4,2,'2023-10-30 23:38:37','2023-10-30 23:38:37'),(5,2,'2023-10-30 23:38:39','2023-10-30 23:38:39'),(6,2,'2023-10-30 23:38:39','2023-10-30 23:38:39'),(7,2,'2023-10-30 23:38:39','2023-10-30 23:38:39'),(8,2,'2023-10-30 23:38:39','2023-10-30 23:38:39'),(9,2,'2023-10-30 23:38:40','2023-10-30 23:38:40'),(10,2,'2023-10-30 23:38:40','2023-10-30 23:38:40'),(11,2,'2023-10-30 23:38:42','2023-10-30 23:38:42'),(12,2,'2023-10-30 23:38:42','2023-10-30 23:38:42'),(13,2,'2023-10-30 23:38:42','2023-10-30 23:38:42'),(14,2,'2023-10-30 23:38:43','2023-10-30 23:38:43'),(15,2,'2023-10-30 23:38:43','2023-10-30 23:38:43'),(16,2,'2023-10-30 23:38:43','2023-10-30 23:38:43'),(17,2,'2023-10-30 23:38:43','2023-10-30 23:38:43'),(18,2,'2023-10-30 23:38:43','2023-10-30 23:38:43'),(19,2,'2023-10-30 23:38:45','2023-10-30 23:38:45'),(20,2,'2023-10-30 23:38:45','2023-10-30 23:38:45'),(21,2,'2023-10-30 23:38:45','2023-10-30 23:38:45'),(22,2,'2023-10-30 23:38:46','2023-10-30 23:38:46'),(23,1,'2023-10-30 23:42:37','2023-10-30 23:42:37'),(24,1,'2023-10-30 23:42:38','2023-10-30 23:42:38'),(25,1,'2023-10-30 23:42:41','2023-10-30 23:42:41'),(26,1,'2023-10-30 23:42:42','2023-10-30 23:42:42'),(27,1,'2023-10-30 23:42:42','2023-10-30 23:42:42'),(28,1,'2023-10-30 23:42:42','2023-10-30 23:42:42'),(29,1,'2023-10-30 23:42:42','2023-10-30 23:42:42'),(30,1,'2023-10-30 23:42:43','2023-10-30 23:42:43'),(31,1,'2023-10-30 23:42:43','2023-10-30 23:42:43'),(32,1,'2023-10-30 23:42:43','2023-10-30 23:42:43'),(33,1,'2023-10-30 23:42:43','2023-10-30 23:42:43'),(34,1,'2023-10-30 23:42:43','2023-10-30 23:42:43'),(35,1,'2023-10-30 23:42:44','2023-10-30 23:42:44'),(36,1,'2023-10-30 23:42:44','2023-10-30 23:42:44'),(37,1,'2023-10-30 23:42:44','2023-10-30 23:42:44'),(38,1,'2023-10-30 23:42:44','2023-10-30 23:42:44'),(39,1,'2023-10-30 23:42:44','2023-10-30 23:42:44'),(40,1,'2023-10-30 23:42:45','2023-10-30 23:42:45'),(41,1,'2023-10-30 23:42:45','2023-10-30 23:42:45'),(42,1,'2023-10-30 23:42:45','2023-10-30 23:42:45'),(43,1,'2023-10-30 23:42:46','2023-10-30 23:42:46'),(44,4,'2023-10-30 23:45:27','2023-10-30 23:45:27'),(45,4,'2023-10-30 23:46:08','2023-10-30 23:46:08'),(46,2,'2023-10-30 23:46:31','2023-10-30 23:46:31'),(47,2,'2023-10-30 23:46:33','2023-10-30 23:46:33'),(48,2,'2023-10-30 23:46:50','2023-10-30 23:46:50'),(49,2,'2023-10-30 23:48:41','2023-10-30 23:48:41'),(50,3,'2023-10-30 23:48:42','2023-10-30 23:48:42'),(51,2,'2023-10-30 23:48:43','2023-10-30 23:48:43'),(52,3,'2023-10-30 23:48:45','2023-10-30 23:48:45'),(53,3,'2023-10-30 23:48:49','2023-10-30 23:48:49'),(54,3,'2023-10-30 23:48:50','2023-10-30 23:48:50'),(55,1,'2023-10-30 23:48:50','2023-10-30 23:48:50'),(56,1,'2023-10-30 23:48:52','2023-10-30 23:48:52'),(57,1,'2023-10-30 23:48:59','2023-10-30 23:48:59'),(58,4,'2023-10-30 23:49:28','2023-10-30 23:49:28'),(59,2,'2023-10-30 23:51:08','2023-10-30 23:51:08'),(60,2,'2023-10-30 23:53:23','2023-10-30 23:53:23'),(61,2,'2023-10-30 23:53:58','2023-10-30 23:53:58'),(62,1,'2023-10-30 23:55:56','2023-10-30 23:55:56'),(63,2,'2023-10-30 23:56:00','2023-10-30 23:56:00'),(64,2,'2023-11-05 16:35:45','2023-11-05 16:35:45'),(65,1,'2023-11-05 16:35:51','2023-11-05 16:35:51'),(66,4,'2023-11-05 16:35:54','2023-11-05 16:35:54'),(67,3,'2023-11-05 16:35:57','2023-11-05 16:35:57'),(68,1,'2023-11-05 16:36:01','2023-11-05 16:36:01'),(69,2,'2023-11-05 16:36:06','2023-11-05 16:36:06'),(70,1,'2023-11-05 16:37:24','2023-11-05 16:37:24'),(71,4,'2023-11-05 16:55:08','2023-11-05 16:55:08'),(72,1,'2023-11-05 16:58:40','2023-11-05 16:58:40'),(73,3,'2023-11-05 16:59:27','2023-11-05 16:59:27'),(74,2,'2023-11-05 16:59:59','2023-11-05 16:59:59'),(75,3,'2023-11-05 17:00:41','2023-11-05 17:00:41'),(76,1,'2023-11-05 17:00:43','2023-11-05 17:00:43'),(77,2,'2023-11-05 17:00:44','2023-11-05 17:00:44'),(78,2,'2023-11-05 17:00:46','2023-11-05 17:00:46'),(79,1,'2023-11-05 17:00:48','2023-11-05 17:00:48'),(80,1,'2023-11-06 19:20:29','2023-11-06 19:20:29'),(81,2,'2023-11-06 19:20:54','2023-11-06 19:20:54'),(82,4,'2023-11-06 19:21:02','2023-11-06 19:21:02'),(83,1,'2023-11-06 19:22:46','2023-11-06 19:22:46'),(84,2,'2023-11-06 19:25:59','2023-11-06 19:25:59'),(85,2,'2023-11-06 19:28:52','2023-11-06 19:28:52');
/*!40000 ALTER TABLE `views` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-10  5:38:41
