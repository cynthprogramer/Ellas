-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema fwoman
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema fwoman
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `fwoman` DEFAULT CHARACTER SET utf8 ;
USE `fwoman` ;

-- -----------------------------------------------------
-- Table `fwoman`.`usuaria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`usuaria` (
  `id_usuaria` INT NOT NULL AUTO_INCREMENT,
  `matricula` INT NOT NULL,
  `username` VARCHAR(15) NOT NULL,
  `descricao` VARCHAR(250) NOT NULL,
  `role` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id_usuaria`),
  UNIQUE INDEX `id_usuaria_UNIQUE` (`id_usuaria` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`postagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`postagem` (
  `idpostagem` INT NOT NULL AUTO_INCREMENT,
  `data_postagem` DATETIME NOT NULL,
  `titulo` VARCHAR(40) NOT NULL,
  `texto` VARCHAR(250) NOT NULL,
  `id_usuaria` INT NOT NULL,
  PRIMARY KEY (`idpostagem`, `id_usuaria`),
  INDEX `fk_idUsuaria_idx` (`id_usuaria` ASC) VISIBLE,
  UNIQUE INDEX `idpostagem_UNIQUE` (`idpostagem` ASC) VISIBLE,
  UNIQUE INDEX `data_postagem_UNIQUE` (`data_postagem` ASC) VISIBLE,
  UNIQUE INDEX `id_usuaria_UNIQUE` (`id_usuaria` ASC) VISIBLE,
  CONSTRAINT `fk_idUsuariaPostagem`
    FOREIGN KEY (`id_usuaria`)
    REFERENCES `fwoman`.`usuaria` (`id_usuaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`avaliacao_denunciada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`avaliacao_denunciada` (
  `fk_avaliacao` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`fk_avaliacao`),
  UNIQUE INDEX `fk_avaliacao_UNIQUE` (`fk_avaliacao` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`denuncia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`denuncia` (
  `id_denuncia` INT NOT NULL AUTO_INCREMENT,
  `titulo_denuncia` VARCHAR(50) NULL,
  `texto_denuncia` VARCHAR(100) NULL,
  PRIMARY KEY (`id_denuncia`),
  UNIQUE INDEX `id_denuncia_UNIQUE` (`id_denuncia` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`avaliacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`avaliacao` (
  `comentarios` VARCHAR(230) NULL,
  `data_comentario` DATETIME NOT NULL,
  `id_usuaria` INT NOT NULL,
  `avaliacao` VARCHAR(50) NOT NULL,
  `id_avaliacao` INT NOT NULL AUTO_INCREMENT,
  `id_postagem` INT NOT NULL,
  PRIMARY KEY (`id_avaliacao`, `id_postagem`, `id_usuaria`, `avaliacao`),
  UNIQUE INDEX `id_avaliacao_UNIQUE` (`id_avaliacao` ASC) VISIBLE,
  INDEX `fk_idUsuariaAvaliacao_idx` (`id_usuaria` ASC) VISIBLE,
  INDEX `fk_idPostagem_idx` (`id_postagem` ASC) VISIBLE,
  INDEX `fk_AvaliacaoDenunciada_idx` (`avaliacao` ASC) VISIBLE,
  UNIQUE INDEX `id_postagem_UNIQUE` (`id_postagem` ASC) VISIBLE,
  UNIQUE INDEX `avaliacao_UNIQUE` (`avaliacao` ASC) VISIBLE,
  CONSTRAINT `fk_idUsuariaAvaliacao`
    FOREIGN KEY (`id_usuaria`)
    REFERENCES `fwoman`.`usuaria` (`id_usuaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idPostagemAvaliacao`
    FOREIGN KEY (`id_postagem`)
    REFERENCES `fwoman`.`postagem` (`idpostagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AvaliacaoDenunciada`
    FOREIGN KEY (`avaliacao`)
    REFERENCES `fwoman`.`avaliacao_denunciada` (`fk_avaliacao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idAvaliacaoDenuncia`
    FOREIGN KEY (`id_avaliacao`)
    REFERENCES `fwoman`.`denuncia` (`id_denuncia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`postagem_curtida`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`postagem_curtida` (
  `id_usuaria` INT NOT NULL,
  `id_postagem` INT NOT NULL,
  PRIMARY KEY (`id_usuaria`, `id_postagem`),
  INDEX `fk_idPostagem_idx` (`id_postagem` ASC) VISIBLE,
  UNIQUE INDEX `id_usuaria_UNIQUE` (`id_usuaria` ASC) VISIBLE,
  UNIQUE INDEX `id_postagem_UNIQUE` (`id_postagem` ASC) VISIBLE,
  CONSTRAINT `fk_idUsuariaPostagemCurtida`
    FOREIGN KEY (`id_usuaria`)
    REFERENCES `fwoman`.`usuaria` (`id_usuaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idPostagemCurtida`
    FOREIGN KEY (`id_postagem`)
    REFERENCES `fwoman`.`postagem` (`idpostagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fwoman`.`postagem_removida`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fwoman`.`postagem_removida` (
  `justificativa` VARCHAR(200) NOT NULL,
  `id_usuaria` INT NOT NULL,
  `id_postagem` INT NOT NULL,
  INDEX `fk_idUsuaria_idx` (`id_usuaria` ASC) VISIBLE,
  INDEX `fk_idPostagem_idx` (`id_postagem` ASC) VISIBLE,
  PRIMARY KEY (`id_usuaria`, `id_postagem`),
  UNIQUE INDEX `id_postagem_UNIQUE` (`id_postagem` ASC) VISIBLE,
  UNIQUE INDEX `id_usuaria_UNIQUE` (`id_usuaria` ASC) VISIBLE,
  CONSTRAINT `fk_idUsuariaPostagemRemovida`
    FOREIGN KEY (`id_usuaria`)
    REFERENCES `fwoman`.`usuaria` (`id_usuaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idPostagemRemovida`
    FOREIGN KEY (`id_postagem`)
    REFERENCES `fwoman`.`postagem` (`idpostagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
