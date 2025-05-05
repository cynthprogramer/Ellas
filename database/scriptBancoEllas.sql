-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ellasbanco
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
-- Table structure for table `avaliacao`
--

DROP TABLE IF EXISTS `avaliacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacao` (
  `id_avaliacao` int NOT NULL AUTO_INCREMENT,
  `id_postagem` int NOT NULL,
  `id_usuaria` int NOT NULL,
  `texto_avaliacao` varchar(250) DEFAULT NULL,
  `id_denuncia` int NOT NULL,
  PRIMARY KEY (`id_avaliacao`,`id_postagem`,`id_usuaria`,`id_denuncia`),
  UNIQUE KEY `id_avaliacao_UNIQUE` (`id_avaliacao`),
  UNIQUE KEY `id_postagem_UNIQUE` (`id_postagem`),
  KEY `fk_idUsuariaAvaliacao_idx` (`id_usuaria`),
  KEY `fk_idPostagem_idx` (`id_postagem`),
  KEY `fk_idDenuncia_idx` (`id_denuncia`),
  CONSTRAINT `fk_idDenuncia` FOREIGN KEY (`id_denuncia`) REFERENCES `denuncia` (`id_denuncia`),
  CONSTRAINT `fk_idPostagemAvaliacao` FOREIGN KEY (`id_postagem`) REFERENCES `postagem` (`idpostagem`),
  CONSTRAINT `fk_idUsuariaAvaliacao` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacao`
--

LOCK TABLES `avaliacao` WRITE;
/*!40000 ALTER TABLE `avaliacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `avaliacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentario`
--

DROP TABLE IF EXISTS `comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentario` (
  `id_comentario` int NOT NULL AUTO_INCREMENT,
  `id_usuaria` int NOT NULL,
  `id_postagem` int NOT NULL,
  `texto_comentario` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_comentario`,`id_usuaria`,`id_postagem`),
  UNIQUE KEY `id_comentario_UNIQUE` (`id_comentario`),
  UNIQUE KEY `id_usuaria_UNIQUE` (`id_usuaria`),
  UNIQUE KEY `id_postagem_UNIQUE` (`id_postagem`),
  CONSTRAINT `fk_idPostagemComentario` FOREIGN KEY (`id_postagem`) REFERENCES `postagem` (`idpostagem`),
  CONSTRAINT `fk_idUsuariaComentario` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentario`
--

LOCK TABLES `comentario` WRITE;
/*!40000 ALTER TABLE `comentario` DISABLE KEYS */;
/*!40000 ALTER TABLE `comentario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `denuncia`
--

DROP TABLE IF EXISTS `denuncia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `denuncia` (
  `id_denuncia` int NOT NULL AUTO_INCREMENT,
  `id_postagem` int NOT NULL,
  `id_usuaria` int NOT NULL,
  `id_comentario` int NOT NULL,
  `titulo_denuncia` varchar(50) DEFAULT NULL,
  `texto_denuncia` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_denuncia`,`id_postagem`,`id_usuaria`,`id_comentario`),
  UNIQUE KEY `id_denuncia_UNIQUE` (`id_denuncia`),
  UNIQUE KEY `id_postagem_UNIQUE` (`id_postagem`),
  KEY `fk_idUsuariaDenuncia_idx` (`id_usuaria`),
  KEY `fk_idComentarioDenunciado_idx` (`id_comentario`),
  CONSTRAINT `fk_idComentarioDenunciado` FOREIGN KEY (`id_comentario`) REFERENCES `comentario` (`id_comentario`),
  CONSTRAINT `fk_idPostagemDenunciada` FOREIGN KEY (`id_postagem`) REFERENCES `postagem` (`idpostagem`),
  CONSTRAINT `fk_idUsuariaDenuncia` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `denuncia`
--

LOCK TABLES `denuncia` WRITE;
/*!40000 ALTER TABLE `denuncia` DISABLE KEYS */;
/*!40000 ALTER TABLE `denuncia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postagem`
--

DROP TABLE IF EXISTS `postagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postagem` (
  `idpostagem` int NOT NULL AUTO_INCREMENT,
  `data_postagem` datetime NOT NULL,
  `titulo` varchar(40) NOT NULL,
  `texto` varchar(250) NOT NULL,
  `id_usuaria` int NOT NULL,
  PRIMARY KEY (`idpostagem`,`id_usuaria`),
  UNIQUE KEY `idpostagem_UNIQUE` (`idpostagem`),
  UNIQUE KEY `data_postagem_UNIQUE` (`data_postagem`),
  UNIQUE KEY `id_usuaria_UNIQUE` (`id_usuaria`),
  KEY `fk_idUsuaria_idx` (`id_usuaria`),
  CONSTRAINT `fk_idUsuariaPostagem` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postagem`
--

LOCK TABLES `postagem` WRITE;
/*!40000 ALTER TABLE `postagem` DISABLE KEYS */;
/*!40000 ALTER TABLE `postagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postagem_curtida`
--

DROP TABLE IF EXISTS `postagem_curtida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postagem_curtida` (
  `id_usuaria` int NOT NULL,
  `id_postagem` int NOT NULL,
  PRIMARY KEY (`id_usuaria`,`id_postagem`),
  UNIQUE KEY `id_usuaria_UNIQUE` (`id_usuaria`),
  UNIQUE KEY `id_postagem_UNIQUE` (`id_postagem`),
  KEY `fk_idPostagem_idx` (`id_postagem`),
  CONSTRAINT `fk_idPostagemCurtida` FOREIGN KEY (`id_postagem`) REFERENCES `postagem` (`idpostagem`),
  CONSTRAINT `fk_idUsuariaPostagemCurtida` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postagem_curtida`
--

LOCK TABLES `postagem_curtida` WRITE;
/*!40000 ALTER TABLE `postagem_curtida` DISABLE KEYS */;
/*!40000 ALTER TABLE `postagem_curtida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postagem_removida`
--

DROP TABLE IF EXISTS `postagem_removida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postagem_removida` (
  `justificativa` varchar(250) NOT NULL,
  `id_usuaria` int NOT NULL,
  `id_postagem` int NOT NULL,
  `id_avaliacao` int NOT NULL,
  PRIMARY KEY (`id_usuaria`,`id_postagem`,`id_avaliacao`),
  UNIQUE KEY `id_postagem_UNIQUE` (`id_postagem`),
  UNIQUE KEY `id_usuaria_UNIQUE` (`id_usuaria`),
  UNIQUE KEY `id_avaliacao_UNIQUE` (`id_avaliacao`),
  KEY `fk_idUsuaria_idx` (`id_usuaria`),
  KEY `fk_idPostagem_idx` (`id_postagem`),
  CONSTRAINT `fk_idAvaliacaoRemove` FOREIGN KEY (`id_avaliacao`) REFERENCES `avaliacao` (`id_avaliacao`),
  CONSTRAINT `fk_idPostagemRemovida` FOREIGN KEY (`id_postagem`) REFERENCES `postagem` (`idpostagem`),
  CONSTRAINT `fk_idUsuariaPostagemRemovida` FOREIGN KEY (`id_usuaria`) REFERENCES `usuaria` (`id_usuaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postagem_removida`
--

LOCK TABLES `postagem_removida` WRITE;
/*!40000 ALTER TABLE `postagem_removida` DISABLE KEYS */;
/*!40000 ALTER TABLE `postagem_removida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuaria`
--

DROP TABLE IF EXISTS `usuaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuaria` (
  `id_usuaria` int NOT NULL AUTO_INCREMENT,
  `matricula` int NOT NULL,
  `username` varchar(15) NOT NULL,
  `descricao` varchar(250) NOT NULL,
  `role` mediumtext NOT NULL,
  PRIMARY KEY (`id_usuaria`),
  UNIQUE KEY `id_usuaria_UNIQUE` (`id_usuaria`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuaria`
--

LOCK TABLES `usuaria` WRITE;
/*!40000 ALTER TABLE `usuaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuaria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-28 14:33:10
