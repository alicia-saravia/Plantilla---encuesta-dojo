-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojos` ;

-- -----------------------------------------------------
-- Schema dojos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos` DEFAULT CHARACTER SET utf8 ;
USE `dojos` ;

-- -----------------------------------------------------
-- Table `dojos`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `ubicacion` VARCHAR(45) NULL,
  `idioma` VARCHAR(45) NULL,
  `comentario` VARCHAR(255) NULL,
  `creado_en` DATETIME NULL DEFAULT now(),
  `actualizado_en` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;