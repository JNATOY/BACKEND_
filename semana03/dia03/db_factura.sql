-- MySQL Script generated by MySQL Workbench
-- Thu Aug  3 19:35:48 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_factura_g21
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_factura_g21
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_factura_g21` DEFAULT CHARACTER SET utf8 ;
USE `db_factura_g21` ;

-- -----------------------------------------------------
-- Table `db_factura_g21`.`tbl_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura_g21`.`tbl_cliente` (
  `cliente_id` INT(11) NOT NULL,
  `cliente_razon_social` VARCHAR(255) NOT NULL,
  `cliente_ruc` VARCHAR(11) NOT NULL,
  `cliente_direccion` TEXT NULL,
  PRIMARY KEY (`cliente_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura_g21`.`tbl_producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura_g21`.`tbl_producto` (
  `producto_id` INT(11) NOT NULL AUTO_INCREMENT,
  `producto_descripcion` VARCHAR(255) NOT NULL,
  `producto_precio` DOUBLE NOT NULL DEFAULT 0,
  PRIMARY KEY (`producto_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura_g21`.`tbl_factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura_g21`.`tbl_factura` (
  `factura_id` INT(11) NOT NULL AUTO_INCREMENT,
  `factura_serie` VARCHAR(10) NOT NULL,
  `factura_numero` VARCHAR(20) NOT NULL,
  `factura_fecha_emision` DATE NOT NULL,
  `factura_moneda` VARCHAR(45) NOT NULL,
  `factura_observacion` TEXT NULL,
  `factura_subtotal` DOUBLE NOT NULL,
  `factura_igv` DOUBLE NOT NULL,
  `factura_total` DOUBLE NOT NULL,
  `cliente_id` INT(11) NOT NULL,
  PRIMARY KEY (`factura_id`),
  CONSTRAINT `fk_tbl_factura_tbl_cliente`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `db_factura_g21`.`tbl_cliente` (`cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura_g21`.`tbl_factura_detalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura_g21`.`tbl_factura_detalle` (
  `factura_detalle_id` INT(11) NOT NULL AUTO_INCREMENT,
  `factura_id` INT(11) NOT NULL,
  `producto_id` INT(11) NOT NULL,
  `factura_detalle_cantidad` DOUBLE NOT NULL DEFAULT 1,
  `factura_detalle_precio` DOUBLE NOT NULL,
  PRIMARY KEY (`factura_detalle_id`),
  CONSTRAINT `fk_tbl_factura_detalle_tbl_factura1`
    FOREIGN KEY (`factura_id`)
    REFERENCES `db_factura_g21`.`tbl_factura` (`factura_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_factura_detalle_tbl_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `db_factura_g21`.`tbl_producto` (`producto_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
