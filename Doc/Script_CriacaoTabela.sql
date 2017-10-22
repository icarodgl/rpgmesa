-- MySQL Script generated by MySQL Workbench
-- Sun Oct 22 21:17:05 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema rpgmesaDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rpgmesaDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rpgmesaDB` DEFAULT CHARACTER SET utf8 ;
USE `rpgmesaDB` ;

-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Usuario` (
  `IdUsuario` INT NOT NULL,
  `Username` VARCHAR(15) NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `DataCadastro` DATETIME NOT NULL,
  PRIMARY KEY (`IdUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Personagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Personagem` (
  `IdPersonagem` INT NOT NULL AUTO_INCREMENT,
  `IdUsuario` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `Experiencia` INT NULL,
  `Level` INT NULL,
  `Saude` INT NULL,
  `Imagem` VARCHAR(1000) NULL,
  PRIMARY KEY (`IdPersonagem`, `IdUsuario`),
  INDEX `fk_Personagem_Usuario1_idx` (`IdUsuario` ASC),
  CONSTRAINT `fk_Personagem_Usuario1`
    FOREIGN KEY (`IdUsuario`)
    REFERENCES `rpgmesaDB`.`Usuario` (`IdUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Ficha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Ficha` (
  `IdFicha` INT NOT NULL AUTO_INCREMENT,
  `IdPersonagem` INT NOT NULL,
  `Raca` VARCHAR(45) NULL,
  `Classe` VARCHAR(45) NULL,
  `Altura` INT NULL,
  `Idade` INT NULL,
  `Peso` INT NULL,
  `Sexo` VARCHAR(20) NULL,
  `Tendencia` VARCHAR(45) NULL,
  `Deslocamento` VARCHAR(45) NULL,
  `Iniciativa` INT NULL,
  `CargaMax` INT NULL,
  PRIMARY KEY (`IdFicha`, `IdPersonagem`),
  INDEX `fk_Ficha_Personagem1_idx` (`IdPersonagem` ASC),
  CONSTRAINT `fk_Ficha_Personagem1`
    FOREIGN KEY (`IdPersonagem`)
    REFERENCES `rpgmesaDB`.`Personagem` (`IdPersonagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Magia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Magia` (
  `IdMagia` INT NOT NULL AUTO_INCREMENT,
  `IdFicha` INT NOT NULL,
  `Dano` INT NULL,
  `Decaimento` INT NULL,
  `Uso` INT NULL,
  `Efeito` VARCHAR(45) NULL,
  `Nivel` INT NULL,
  `Escola` VARCHAR(45) NULL,
  `Componente` VARCHAR(45) NULL,
  `Conjuracao` INT NULL,
  PRIMARY KEY (`IdMagia`, `IdFicha`),
  UNIQUE INDEX `IdMagia_UNIQUE` (`IdMagia` ASC),
  INDEX `fk_Magia_Ficha1_idx` (`IdFicha` ASC),
  CONSTRAINT `fk_Magia_Ficha1`
    FOREIGN KEY (`IdFicha`)
    REFERENCES `rpgmesaDB`.`Ficha` (`IdFicha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Item` (
  `IdItem` INT NOT NULL AUTO_INCREMENT,
  `IdFicha` INT NOT NULL,
  `Descricao` VARCHAR(45) NULL,
  `Peso` INT NULL,
  `Efeito` VARCHAR(45) NULL,
  `Equipado` BIT(1) NULL,
  `Tempo` INT NULL,
  `Dano` INT NULL,
  `Cargas` INT NULL,
  `Acerto` INT NULL,
  `Mao` INT NULL,
  `TipoDado` INT NULL,
  `QuatDado` INT NULL,
  `Defesa` INT NULL,
  `Agilidade` INT NULL,
  `Arcano` INT NULL,
  PRIMARY KEY (`IdItem`, `IdFicha`),
  INDEX `fk_Item_Ficha1_idx` (`IdFicha` ASC),
  CONSTRAINT `fk_Item_Ficha1`
    FOREIGN KEY (`IdFicha`)
    REFERENCES `rpgmesaDB`.`Ficha` (`IdFicha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Atributo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Atributo` (
  `IdAtributo` INT NOT NULL AUTO_INCREMENT,
  `IdFicha` INT NOT NULL,
  `Forca` INT NULL,
  `Vigor` INT NULL,
  `Agilidade` INT NULL,
  `Intelecto` INT NULL,
  `Espirito` INT NULL,
  PRIMARY KEY (`IdAtributo`, `IdFicha`),
  INDEX `fk_Atributo_Ficha1_idx` (`IdFicha` ASC),
  CONSTRAINT `fk_Atributo_Ficha1`
    FOREIGN KEY (`IdFicha`)
    REFERENCES `rpgmesaDB`.`Ficha` (`IdFicha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = '	\n		';


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Historia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Historia` (
  `IdHistoria` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL,
  `Descricao` VARCHAR(45) NULL,
  `Capa` VARCHAR(45) NULL,
  PRIMARY KEY (`IdHistoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Partida`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Partida` (
  `IdPartida` INT NOT NULL AUTO_INCREMENT,
  `IdHistoria` INT NOT NULL,
  `NomeJogo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`IdPartida`, `IdHistoria`),
  INDEX `fk_Partida_Historia1_idx` (`IdHistoria` ASC),
  CONSTRAINT `fk_Partida_Historia1`
    FOREIGN KEY (`IdHistoria`)
    REFERENCES `rpgmesaDB`.`Historia` (`IdHistoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`HistoricoParticipacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`HistoricoParticipacao` (
  `IdHistoricoParticipacao` INT NOT NULL AUTO_INCREMENT,
  `IdPersonagem` INT NOT NULL,
  `IdPartida` INT NOT NULL,
  `Sucesso` INT NULL,
  `Descricao` VARCHAR(45) NULL,
  `Data` DATETIME NULL,
  PRIMARY KEY (`IdHistoricoParticipacao`, `IdPersonagem`, `IdPartida`),
  INDEX `fk_HistoricoParticipacao_Partida1_idx` (`IdPartida` ASC),
  INDEX `fk_HistoricoParticipacao_Personagem1_idx` (`IdPersonagem` ASC),
  CONSTRAINT `fk_HistoricoParticipacao_Partida1`
    FOREIGN KEY (`IdPartida`)
    REFERENCES `rpgmesaDB`.`Partida` (`IdPartida`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_HistoricoParticipacao_Personagem1`
    FOREIGN KEY (`IdPersonagem`)
    REFERENCES `rpgmesaDB`.`Personagem` (`IdPersonagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Mapa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Mapa` (
  `IdMapa` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL,
  `Imagem` VARCHAR(1000) NULL,
  PRIMARY KEY (`IdMapa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Cenario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Cenario` (
  `IdCenario` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL,
  `Imagem` VARCHAR(1000) NULL,
  `Descricao` VARCHAR(500) NULL,
  PRIMARY KEY (`IdCenario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Pericia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Pericia` (
  `IdPericia` INT NOT NULL AUTO_INCREMENT,
  `Atributo` VARCHAR(45) NULL,
  `Nivel` INT NULL,
  PRIMARY KEY (`IdPericia`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`PericiaxFicha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`PericiaxFicha` (
  `IdPericiaXFicha` INT NOT NULL AUTO_INCREMENT,
  `IdFicha` INT NOT NULL,
  `IdPericia` INT NOT NULL,
  PRIMARY KEY (`IdPericiaXFicha`, `IdFicha`, `IdPericia`),
  INDEX `fk_Pericia_has_Ficha_Ficha1_idx` (`IdFicha` ASC),
  INDEX `fk_Pericia_has_Ficha_Pericia1_idx` (`IdPericia` ASC),
  CONSTRAINT `fk_Pericia_has_Ficha_Pericia1`
    FOREIGN KEY (`IdPericia`)
    REFERENCES `rpgmesaDB`.`Pericia` (`IdPericia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pericia_has_Ficha_Ficha1`
    FOREIGN KEY (`IdFicha`)
    REFERENCES `rpgmesaDB`.`Ficha` (`IdFicha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`HistoriaxMapa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`HistoriaxMapa` (
  `IdHistoriaxMapa` INT NOT NULL AUTO_INCREMENT,
  `IdHistoria` INT NOT NULL,
  `IdMapa` INT NOT NULL,
  PRIMARY KEY (`IdHistoriaxMapa`, `IdHistoria`, `IdMapa`),
  INDEX `fk_Historia_has_Mapa_Mapa1_idx` (`IdMapa` ASC),
  INDEX `fk_Historia_has_Mapa_Historia1_idx` (`IdHistoria` ASC),
  CONSTRAINT `fk_Historia_has_Mapa_Historia1`
    FOREIGN KEY (`IdHistoria`)
    REFERENCES `rpgmesaDB`.`Historia` (`IdHistoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Historia_has_Mapa_Mapa1`
    FOREIGN KEY (`IdMapa`)
    REFERENCES `rpgmesaDB`.`Mapa` (`IdMapa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`MapaxCenario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`MapaxCenario` (
  `IdMapaxCenario` INT NOT NULL AUTO_INCREMENT,
  `IdMapa` INT NOT NULL,
  `IdCenario` INT NOT NULL,
  PRIMARY KEY (`IdMapaxCenario`, `IdMapa`, `IdCenario`),
  INDEX `fk_Mapa_has_Cenario_Cenario1_idx` (`IdCenario` ASC),
  INDEX `fk_Mapa_has_Cenario_Mapa1_idx` (`IdMapa` ASC),
  CONSTRAINT `fk_Mapa_has_Cenario_Mapa1`
    FOREIGN KEY (`IdMapa`)
    REFERENCES `rpgmesaDB`.`Mapa` (`IdMapa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mapa_has_Cenario_Cenario1`
    FOREIGN KEY (`IdCenario`)
    REFERENCES `rpgmesaDB`.`Cenario` (`IdCenario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rpgmesaDB`.`Participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rpgmesaDB`.`Participante` (
  `IdParticipante` INT NOT NULL AUTO_INCREMENT,
  `IdPartida` INT NOT NULL,
  `IdPersonagem` INT NOT NULL,
  `IdUsuario` INT NOT NULL,
  PRIMARY KEY (`IdParticipante`, `IdPartida`, `IdPersonagem`, `IdUsuario`),
  INDEX `fk_Participante_Usuario1_idx` (`IdUsuario` ASC),
  INDEX `fk_Participante_Personagem1_idx` (`IdPersonagem` ASC),
  INDEX `fk_Participante_Partida1_idx` (`IdPartida` ASC),
  CONSTRAINT `fk_Participante_Usuario1`
    FOREIGN KEY (`IdUsuario`)
    REFERENCES `rpgmesaDB`.`Usuario` (`IdUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Personagem1`
    FOREIGN KEY (`IdPersonagem`)
    REFERENCES `rpgmesaDB`.`Personagem` (`IdPersonagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Partida1`
    FOREIGN KEY (`IdPartida`)
    REFERENCES `rpgmesaDB`.`Partida` (`IdPartida`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
